#!/usr/bin/env python3
"""
Turn the chapter source into the knowledge set the teacher-support bot reads.

The bot must answer from the edition that was *published*, not from whatever is
in the working tree, so this runs from build.sh alongside the PDF and the HTML
and stamps its output with the same git fingerprint. Four artifacts, one version
number: that is the whole point of generating rather than hand-writing.

    content/chapters/*.md  ->  knowledge/markdown/*.md  ->  knowledge/chunks.jsonl

The markdown is written to disk and the chunks are parsed back out of it, rather
than both being emitted from one in-memory model. Two reasons. The chunks then
cannot describe text the markdown does not contain, so the two outputs cannot
drift. And it forces the markdown to be *self-sufficient* -- everything the
chunks need has to be expressible in the prose -- which is exactly the property
required if the markdown is ever handed to a hosted retrieval service that
parses and chunks documents itself and keeps none of our structure.

Which of the two you use depends on where retrieval lives:

  * hosted library (upload documents, it chunks them) -> knowledge/markdown/
  * retrieval we build ourselves                      -> knowledge/chunks.jsonl

Chapters are written for print and carry constructs that are meaningless or
harmful in a chat window, so the conversion is not a copy:

  * Image captions survive as prose, labelled "Figure:", with the resolved URL
    beside them. Captions are 11% of the book and, since the captioning work
    finished, they are instruction rather than decoration -- "note that the port
    dropdown reads port1" is the answer to a real question. The URL is inline
    rather than held as metadata so that it survives someone else's chunker.
  * files/ links become absolute URLs, by the same rule as tools/abs-links.lua,
    so the bot can hand over the handout instead of mentioning that one exists.
  * Internal cross-references flatten to their link text. In print xref.lua
    expands these to "(Figure 9.23, on page 131)", which is noise in a chat
    window; the phrase "see Getting started with the robot" is the useful part.
  * Callouts are labelled. Per word they are the highest-value content in the
    book -- the accumulated gotchas -- so they are marked for retrieval to
    weight rather than left as anonymous blockquotes.
  * Tables stay verbatim. The port table and the materials lists are lookup
    data and prose-flattening destroys them.
  * Revision notes, pandoc attributes and LaTeX machinery are dropped.

Chapter *numbers* are deliberately absent. Pandoc computes them from
--number-sections, so they shift whenever a chapter is reordered; the titles are
stable and are what a teacher would say out loud.

    python3 tools/knowledge.py            # write ../bot/knowledge
    python3 tools/knowledge.py --quiet    # for use in build.sh
    python3 tools/knowledge.py --out DIR
"""
import os, re, sys, json, glob

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(HERE, "content", "chapters")
DEFAULT_OUT = os.path.join(os.path.dirname(HERE), "bot", "knowledge")

# A section this short cannot stand on its own once retrieved -- 64 of them are
# under 40 words and one is nothing but an image -- so it folds into its parent
# rather than becoming a fragment that matches a query and then says nothing.
MIN_WORDS = 40

COMMENT = re.compile(r"<!--.*?-->", re.S)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
ATTR = re.compile(r"\s*\{[^}]*\}\s*$")
# One level of nesting on the left, because captions contain links.
IMAGE = re.compile(r"!\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)]*)\)(?:\{[^}]*\})?")
LINK = re.compile(r"(?<!!)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)]*)\)")
CALLOUT_KIND = re.compile(r"^\*\*(Note|Tip|Warning|Caution)\*\*\s*$", re.I)

# How a figure is written into the markdown, and how it is read back out. The
# two must stay in step, so they are defined together.
FIGURE_OUT = "Figure: {caption} ([image]({url}))"
# Leading whitespace allowed: six figures sit inside numbered-list items and
# are indented to match, which an unanchored-to-margin pattern would miss.
FIGURE_IN = re.compile(r"^[ \t]*Figure: (.*?) \(\[image\]\((\S+)\)\)\s*$", re.M)


def slug(text):
    """Anchor a book link would use. Same rule as tools/check-links.py, so the
    overlay can point at a section by the anchor the chapters already use."""
    t = ATTR.sub("", text).strip().lower()
    t = re.sub(r"[*`_]", "", t)
    t = re.sub(r"[^\w\s-]", "", t)
    return re.sub(r"\s+", "-", t).strip("-")


def resolve(target, base):
    """files/ paths and images are relative to content/, which resolves to
    nothing once the knowledge set is read from anywhere else."""
    if not base:
        return target
    if re.match(r"^(files|images)/", target):
        return base.rstrip("/") + "/" + target
    return target


def label_callouts(lines):
    """Label `> **Note**` blockquotes and unwrap them.

    A blockquote in a chat window reads as a quotation from somewhere else,
    which is exactly wrong: these are the book speaking in its own voice about
    something that will bite you.
    """
    out, i = [], 0
    while i < len(lines):
        if not lines[i].startswith(">"):
            out.append(lines[i])
            i += 1
            continue
        block = []
        while i < len(lines) and lines[i].startswith(">"):
            block.append(re.sub(r"^>\s?", "", lines[i]))
            i += 1
        while block and not block[0].strip():
            block.pop(0)
        kind = "Aside"
        if block and CALLOUT_KIND.match(block[0].strip()):
            kind = CALLOUT_KIND.match(block[0].strip()).group(1).capitalize()
            block.pop(0)
            while block and not block[0].strip():
                block.pop(0)
        body = "\n".join(block).strip()
        if body:
            out.append(f"**{kind}:** {body}")
    return out


def convert(path, base, edition, fingerprint):
    """One chapter of source -> one self-contained markdown document."""
    raw = COMMENT.sub("", open(path, encoding="utf-8").read())

    text = "\n".join(label_callouts(raw.split("\n")))

    # Images before links: the image markup contains a link-shaped tail.
    def swap_image(m):
        caption, target = m.group(1).strip(), m.group(2).strip()
        return FIGURE_OUT.format(caption=caption, url=resolve(target, base))

    text = IMAGE.sub(swap_image, text)

    # Link syntax is kept rather than flattened to "label (url)", so the
    # markdown still renders as markdown and so the figure markup this pass
    # walks over -- [image](url), written just above -- survives unchanged.
    def swap_link(m):
        label, target = m.group(1), m.group(2).strip()
        if not target or target.startswith("#"):
            return label  # a cross-reference; the phrase is the useful part
        url = resolve(target, base)
        return f"[{label}]({url})" if url.startswith("http") else label

    text = LINK.sub(swap_link, text)

    # Strip pandoc attributes from headings, keep the headings themselves: they
    # are the breadcrumb, and in the markdown they are already in the right
    # place, so nothing has to be added for a foreign chunker to see them.
    lines, chapter = [], None
    for line in text.split("\n"):
        m = HEADING.match(line)
        if m:
            title = ATTR.sub("", m.group(2)).strip()
            if len(m.group(1)) == 1 and chapter is None:
                chapter = title
            lines.append("#" * len(m.group(1)) + " " + title)
        else:
            lines.append(line)

    body = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    front = (f"---\nchapter: {json.dumps(chapter, ensure_ascii=False)}\n"
             f"source: {os.path.basename(path)}\n"
             f"edition: {json.dumps(edition)}\n"
             f"fingerprint: {json.dumps(fingerprint)}\n---\n\n")
    return chapter, front + body + "\n"


def read_front(text):
    """Split YAML front matter from the body. Only the four keys we write."""
    m = re.match(r"^---\n(.*?)\n---\n+", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.strip()
            try:
                v = json.loads(v)
            except json.JSONDecodeError:
                pass
            meta[k.strip()] = v
    return meta, text[m.end():]


def words(text):
    """Prose length. Table rows are lookup data, not prose, and counting them
    would keep a two-line section alive purely because it holds a wide table."""
    prose = [l for l in text.split("\n") if not l.strip().startswith("|")]
    return len(" ".join(prose).split())


def chunk(md_text, md_name):
    """One generated markdown document -> retrieval chunks.

    Read back out of the file rather than carried over from convert(), so a
    chunk can never claim text the uploaded markdown does not contain.

    Breadcrumbs are not optional. The prose says "the robot", "the sensor",
    "the dial" constantly with the referent sitting in the heading, so a chunk
    retrieved without its heading path is often ambiguous about which sensor it
    is even discussing.
    """
    meta, body = read_front(md_text)
    chapter = meta.get("chapter") or md_name
    source = meta.get("source", md_name)

    secs, cur = [], None
    for line in body.split("\n"):
        m = HEADING.match(line)
        if m:
            level, title = len(m.group(1)), m.group(2).strip()
            if level == 1:
                cur = {"level": 1, "title": None, "body": []}
                secs.append(cur)
                continue
            cur = {"level": level, "title": title, "body": []}
            secs.append(cur)
            continue
        if cur is not None:
            cur["body"].append(line)

    def finish(s):
        t = re.sub(r"\n{3,}", "\n\n", "\n".join(s["body"])).strip()
        imgs = [{"caption": c, "url": u} for c, u in FIGURE_IN.findall(t)]
        # Every figure carries an [image](...) link of its own; those are
        # already accounted for above and would otherwise be counted twice.
        links = [{"text": a, "url": b} for a, b in LINK.findall(t)
                 if a != "image" and b.startswith("http")]
        return t, imgs, links

    chunks, stack, pending = [], [], None
    for s in secs:
        title, level = s["title"], s["level"]
        if title is None:
            trail = []
        else:
            stack = stack[: max(0, level - 2)]
            stack.append(title)
            trail = list(stack)

        text, imgs, links = finish(s)
        short = words(text) < MIN_WORDS

        # Fold upward: a heading with almost nothing under it is a signpost for
        # the section that follows, and belongs with it rather than alone.
        if short and chunks:
            prev = chunks[-1]
            head = f"### {title}\n\n" if title else ""
            prev["text"] = (prev["text"] + "\n\n" + head + text).strip()
            prev["images"] += imgs
            prev["links"] += links
            prev["folded"].append(title or "(chapter opening)")
            continue

        # A chapter opening has nothing above it to fold into, so it waits and
        # goes on the front of the first real section instead.
        if short and not chunks:
            pending = (text, imgs, links)
            continue

        chunks.append({
            "id": f"{slug(chapter)}/{slug(title)}" if title else slug(chapter),
            "chapter": chapter,
            "section": title,
            "breadcrumb": " > ".join([chapter] + trail),
            "anchor": slug(title) if title else slug(chapter),
            "source": source,
            "document": md_name,
            "text": text,
            "images": imgs,
            "links": links,
            "folded": [],
        })

        if pending is not None:
            c, (ptext, pimgs, plinks) = chunks[-1], pending
            c["text"] = (ptext + "\n\n" + c["text"]).strip()
            c["images"] = pimgs + c["images"]
            c["links"] = plinks + c["links"]
            c["folded"].append("(chapter opening)")
            pending = None

    # A chapter that is nothing but a short opening still has to survive.
    if pending is not None and not chunks:
        text, imgs, links = pending
        chunks.append({
            "id": slug(chapter), "chapter": chapter, "section": None,
            "breadcrumb": chapter, "anchor": slug(chapter), "source": source,
            "document": md_name, "text": text, "images": imgs, "links": links,
            "folded": [],
        })

    for c in chunks:
        c["words"] = words(c["text"])
    return [c for c in chunks if c["text"]]


def main():
    quiet = "--quiet" in sys.argv
    out_dir = DEFAULT_OUT
    if "--out" in sys.argv:
        out_dir = sys.argv[sys.argv.index("--out") + 1]
    md_dir = os.path.join(out_dir, "markdown")

    base = os.getenv("BME_FILE_BASE", "")
    fingerprint = os.getenv("BME_FINGERPRINT", "unknown")
    edition = os.getenv("BME_EDITION", "unknown")
    if not base and not quiet:
        print("  knowledge: BME_FILE_BASE unset -- image and file links stay relative")

    os.makedirs(md_dir, exist_ok=True)
    for stale in glob.glob(os.path.join(md_dir, "*.md")):
        os.remove(stale)  # a renamed chapter must not leave its old copy behind

    # Pass one: source -> markdown on disk.
    written = []
    for path in sorted(glob.glob(os.path.join(CHAPTERS, "*.md"))):
        chapter, md = convert(path, base, edition, fingerprint)
        if chapter is None:
            print(f"  !! {os.path.basename(path)} has no chapter title -- skipped")
            continue
        name = os.path.basename(path)
        with open(os.path.join(md_dir, name), "w", encoding="utf-8") as fh:
            fh.write(md)
        written.append(name)

    # Pass two: markdown on disk -> chunks.
    chunks = []
    for name in written:
        text = open(os.path.join(md_dir, name), encoding="utf-8").read()
        chunks += chunk(text, name)

    with open(os.path.join(out_dir, "chunks.jsonl"), "w", encoding="utf-8") as fh:
        for c in chunks:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    manifest = {
        "edition": edition,
        "fingerprint": fingerprint,
        "file_base": base,
        "documents": len(written),
        "chunks": len(chunks),
        "images": sum(len(c["images"]) for c in chunks),
        "links": sum(len(c["links"]) for c in chunks),
        "words": sum(c["words"] for c in chunks),
        "min_words": MIN_WORDS,
        "generated_by": "book/tools/knowledge.py",
    }
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    if not quiet:
        longest = max(chunks, key=lambda c: c["words"])
        print(f"  {len(written)} documents -> {len(chunks)} chunks, "
              f"{manifest['words']} words")
        print(f"  {manifest['images']} images, {manifest['links']} links")
        print(f"  longest chunk {longest['words']} words: {longest['breadcrumb']}")
        # A chunk carrying a table or a screenshot is not a fragment even when
        # its prose is short -- the table *is* the content.
        thin = [c for c in chunks if c["words"] < MIN_WORDS and not c["images"]
                and not any(l.startswith("|") for l in c["text"].split("\n"))]
        for c in thin[:5]:
            print(f"  thin: {c['words']:3d} words  {c['breadcrumb']}")


if __name__ == "__main__":
    main()
