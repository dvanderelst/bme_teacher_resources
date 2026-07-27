#!/usr/bin/env python3
"""
Turn the chapter source into the knowledge set the teacher-support bot reads.

The bot must answer from the edition that was *published*, not from whatever is
in the working tree, so this runs from build.sh alongside the PDF and the HTML
and stamps its output with the same git fingerprint. Three artifacts, one
version number: that is the whole point of generating rather than hand-writing.

    content/chapters/*.md  ->  bot/knowledge/*.md

One document per chapter, and no chunking. Retrieval is somebody else's job: a
hosted library parses and chunks what it is given, and passing it pre-cut pieces
would only have it cut them again on boundaries of its own. The same documents
serve a full-context bot, which is a live option here -- the whole book is about
60,000 tokens.

What cannot be delegated is the conversion, because none of it is inferable from
the files. Nothing tells an ingestion pipeline that image captions are
load-bearing instruction rather than decoration, or that a relative files/ path
resolves against a raw GitHub URL. Chapters are written for print and carry
constructs that are meaningless or harmful in a chat window:

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
  * Headings are left exactly where they are. They are the breadcrumb -- the
    prose says "the robot", "the sensor", "the dial" constantly with the
    referent sitting in the heading -- and a chunker we do not control can only
    see them if they are in the text.
  * Revision notes, pandoc attributes and LaTeX machinery are dropped.

Chapter *numbers* are deliberately absent. Pandoc computes them from
--number-sections, so they shift whenever a chapter is reordered; the titles are
stable and are what a teacher would say out loud.

    python3 tools/knowledge.py            # write ../bot/knowledge (no frontmatter)
    python3 tools/knowledge.py --quiet    # for use in build.sh
    python3 tools/knowledge.py --out DIR
"""
import os, re, sys, json, glob

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(HERE, "content", "chapters")
DEFAULT_OUT = os.path.join(os.path.dirname(HERE), "bot", "knowledge")

COMMENT = re.compile(r"<!--.*?-->", re.S)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
ATTR = re.compile(r"\s*\{[^}]*\}\s*$")
# One level of nesting on the left, because captions contain links.
IMAGE = re.compile(r"!\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)]*)\)(?:\{[^}]*\})?")
LINK = re.compile(r"(?<!!)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)]*)\)")
CALLOUT_KIND = re.compile(r"^\*\*(Note|Tip|Warning|Caution)\*\*\s*$", re.I)

# How a figure is written, and how it is read back for the integrity check
# below. The two must stay in step, so they are defined together. Leading
# whitespace is allowed on the way back in: six figures sit inside numbered-list
# items and are indented to match.
FIGURE_OUT = "Figure: {caption} ([image]({url}))"
FIGURE_IN = re.compile(r"^[ \t]*Figure: (.*?) \(\[image\]\((\S+)\)\)\s*$", re.M)


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
    return chapter, body + "\n"


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

    os.makedirs(out_dir, exist_ok=True)
    for stale in glob.glob(os.path.join(out_dir, "*.md")):
        os.remove(stale)  # a renamed chapter must not leave its old copy behind

    written, words, figures, links, expected = [], 0, 0, 0, 0
    for path in sorted(glob.glob(os.path.join(CHAPTERS, "*.md"))):
        chapter, md = convert(path, base, edition, fingerprint)
        if chapter is None:
            print(f"  !! {os.path.basename(path)} has no chapter title -- skipped")
            continue
        name = os.path.basename(path)
        with open(os.path.join(out_dir, name), "w", encoding="utf-8") as fh:
            fh.write(md)
        written.append(name)

        # Integrity check. Every image in the source must come back out as a
        # figure line the agreed shape can read; a caption that quietly fails to
        # round-trip is invisible otherwise, and has happened.
        src_images = len(IMAGE.findall(open(path, encoding="utf-8").read()))
        out_figures = len(FIGURE_IN.findall(md))
        if src_images != out_figures:
            print(f"  !! {name}: {src_images} images in, {out_figures} figures out")
        expected += src_images
        figures += out_figures
        links += sum(1 for a, _ in LINK.findall(md) if a != "image")
        words += len(" ".join(l for l in md.split("\n")
                              if not l.strip().startswith("|")).split())

    manifest = {
        "edition": edition,
        "fingerprint": fingerprint,
        "file_base": base,
        "documents": len(written),
        "words": words,
        "figures": figures,
        "links": links,
        "generated_by": "book/tools/knowledge.py",
        "note": "One document per chapter. Chunking is left to whatever ingests these.",
    }
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    if not quiet:
        print(f"  {len(written)} documents, {words} words, "
              f"{figures}/{expected} figures, {links} links")


if __name__ == "__main__":
    main()
