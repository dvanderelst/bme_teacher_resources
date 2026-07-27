#!/usr/bin/env python3
"""
Turn the chapter source into the knowledge set the teacher-support bot reads.

The bot must answer from the edition that was *published*, not from whatever is
in the working tree, so this runs from build.sh alongside the PDF and the HTML
and stamps its output with the same git fingerprint. Three artifacts, one
version number: that is the whole point of generating rather than hand-writing.

Chapters are written for print and carry constructs that are meaningless or
harmful in a chat window, so the conversion is not a copy:

  * Image captions survive as prose. They are 11% of the book and, since the
    captioning work finished, they are instruction rather than decoration --
    "note that the port dropdown reads port1" is the answer to a real question.
    The resolved image URL rides along, because the bot shows images and for
    "which button do I click?" the screenshot is most of the answer.
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


def take_images(text, base):
    """Replace image markup with its caption and collect the resolved URLs.

    The caption becomes a sentence of its own rather than being dropped or left
    as markup, because it frequently carries the instruction the surrounding
    prose only gestures at.
    """
    found = []

    def swap(m):
        caption, target = m.group(1).strip(), m.group(2).strip()
        found.append({"url": resolve(target, base), "caption": caption})
        return caption

    return IMAGE.sub(swap, text), found


def take_links(text, base):
    """Flatten internal references, absolutise bundled files, keep the rest."""
    found = []

    def swap(m):
        label, target = m.group(1), m.group(2).strip()
        if not target or target.startswith("#"):
            return label  # a cross-reference; the phrase is the useful part
        url = resolve(target, base)
        found.append({"text": label, "url": url})
        return f"{label} ({url})" if url.startswith("http") else label

    return LINK.sub(swap, text), found


def take_callouts(lines):
    """Label `> **Note**` blockquotes and unwrap them.

    A blockquote in a chat window reads as a quotation from somewhere else,
    which is exactly wrong: these are the book speaking in its own voice about
    something that will bite you.
    """
    out, kinds, i = [], [], 0
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
        kind = None
        if block and CALLOUT_KIND.match(block[0].strip()):
            kind = CALLOUT_KIND.match(block[0].strip()).group(1).capitalize()
            block.pop(0)
            while block and not block[0].strip():
                block.pop(0)
        body = "\n".join(block).strip()
        if not body:
            continue
        kinds.append(kind or "Aside")
        out.append(f"**{kind or 'Aside'}:** {body}" if kind else f"**Aside:** {body}")
    return out, kinds


def words(text):
    """Prose length. Table rows are lookup data, not prose, and counting them
    would keep a two-line section alive purely because it holds a wide table."""
    prose = [l for l in text.split("\n") if not l.strip().startswith("|")]
    return len(" ".join(prose).split())


def sections(path, base):
    """Split one chapter into (level, title, body, images, links, callouts)."""
    raw = COMMENT.sub("", open(path, encoding="utf-8").read())
    lines = raw.split("\n")

    chapter, out, cur = None, [], None
    for line in lines:
        m = HEADING.match(line)
        if m:
            level, title = len(m.group(1)), ATTR.sub("", m.group(2)).strip()
            if level == 1 and chapter is None:
                chapter = title
                cur = {"level": 1, "title": None, "body": []}
                out.append(cur)
                continue
            cur = {"level": level, "title": title, "body": []}
            out.append(cur)
            continue
        if cur is not None:
            cur["body"].append(line)

    for s in out:
        body, kinds = take_callouts(s["body"])
        text = "\n".join(body)
        text, imgs = take_images(text, base)
        text, links = take_links(text, base)
        s["text"] = re.sub(r"\n{3,}", "\n\n", text).strip()
        s["images"], s["links"], s["callouts"] = imgs, links, kinds
    return chapter, out


def fold(chapter, secs, source):
    """Emit chunks, folding anything too short into its parent.

    Breadcrumbs are not optional. The prose says "the robot", "the sensor",
    "the dial" constantly with the referent sitting in the heading, so a chunk
    retrieved without its heading path is often ambiguous about which sensor it
    is even discussing.
    """
    chunks, stack, pending = [], [], None
    for s in secs:
        title, level = s["title"], s["level"]
        if title is None:
            trail = []
        else:
            stack = stack[: max(0, level - 2)]
            stack.append(title)
            trail = list(stack)

        body = s["text"]
        short = words(body) < MIN_WORDS

        # Fold upward: a heading with almost nothing under it is a signpost for
        # the section that follows, and belongs with it rather than alone.
        if short and chunks:
            prev = chunks[-1]
            head = f"### {title}\n\n" if title else ""
            prev["text"] = (prev["text"] + "\n\n" + head + body).strip()
            prev["images"] += s["images"]
            prev["links"] += s["links"]
            prev["callouts"] += s["callouts"]
            prev["folded"].append(title or "(chapter opening)")
            continue

        # A chapter opening has nothing above it to fold into, so it waits and
        # goes on the front of the first real section instead.
        if short and not chunks:
            pending = s
            continue

        chunks.append({
            "id": f"{slug(chapter)}/{slug(title)}" if title else slug(chapter),
            "chapter": chapter,
            "section": title,
            "breadcrumb": " > ".join([chapter] + trail),
            "anchor": slug(title) if title else slug(chapter),
            "source": source,
            "text": body,
            "images": list(s["images"]),
            "links": list(s["links"]),
            "callouts": list(s["callouts"]),
            "folded": [],
        })

        if pending is not None:
            c = chunks[-1]
            c["text"] = (pending["text"] + "\n\n" + c["text"]).strip()
            c["images"] = pending["images"] + c["images"]
            c["links"] = pending["links"] + c["links"]
            c["callouts"] = pending["callouts"] + c["callouts"]
            c["folded"].append("(chapter opening)")
            pending = None

    # A chapter that is nothing but a short opening still has to survive.
    if pending is not None and not chunks:
        chunks.append({
            "id": slug(chapter), "chapter": chapter, "section": None,
            "breadcrumb": chapter, "anchor": slug(chapter), "source": source,
            "text": pending["text"], "images": pending["images"],
            "links": pending["links"], "callouts": pending["callouts"],
            "folded": [],
        })

    for c in chunks:
        c["words"] = words(c["text"])
    return [c for c in chunks if c["text"] or c["images"]]


def main():
    quiet = "--quiet" in sys.argv
    out_dir = DEFAULT_OUT
    if "--out" in sys.argv:
        out_dir = sys.argv[sys.argv.index("--out") + 1]

    base = os.getenv("BME_FILE_BASE", "")
    fingerprint = os.getenv("BME_FINGERPRINT", "unknown")
    edition = os.getenv("BME_EDITION", "unknown")
    if not base and not quiet:
        print("  knowledge: BME_FILE_BASE unset -- image and file links stay relative")

    chunks = []
    files = sorted(glob.glob(os.path.join(CHAPTERS, "*.md")))
    for path in files:
        chapter, secs = sections(path, base)
        if chapter is None:
            print(f"  !! {os.path.basename(path)} has no chapter title -- skipped")
            continue
        chunks += fold(chapter, secs, os.path.basename(path))

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "chunks.jsonl"), "w", encoding="utf-8") as fh:
        for c in chunks:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    manifest = {
        "edition": edition,
        "fingerprint": fingerprint,
        "file_base": base,
        "chapters": len(files),
        "chunks": len(chunks),
        "images": sum(len(c["images"]) for c in chunks),
        "links": sum(len(c["links"]) for c in chunks),
        "callouts": sum(len(c["callouts"]) for c in chunks),
        "words": sum(c["words"] for c in chunks),
        "min_words": MIN_WORDS,
        "generated_by": "book/tools/knowledge.py",
    }
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    if not quiet:
        longest = max(chunks, key=lambda c: c["words"])
        print(f"  {len(chunks)} chunks from {len(files)} chapters, "
              f"{manifest['words']} words")
        print(f"  {manifest['images']} images, {manifest['links']} links, "
              f"{manifest['callouts']} callouts")
        print(f"  longest chunk {longest['words']} words: {longest['breadcrumb']}")
        # A chunk carrying a table or a screenshot is not a fragment even when
        # its prose is short -- the table *is* the content.
        thin = [c for c in chunks if c["words"] < MIN_WORDS and not c["images"]
                and not any(l.startswith("|") for l in c["text"].split("\n"))]
        if thin:
            print(f"  {len(thin)} chunk(s) still under {MIN_WORDS} words:")
            for c in thin[:5]:
                print(f"     {c['words']:3d}  {c['breadcrumb']}")


if __name__ == "__main__":
    main()
