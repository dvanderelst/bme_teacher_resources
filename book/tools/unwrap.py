#!/usr/bin/env python3
"""
Rewrite the chapters so each prose paragraph is a single line.

The chapters arrived with inconsistent wrapping: paragraphs from Notion are one
long line, paragraphs written by hand were wrapped at about 95 columns. Editing a
sentence in a wrapped paragraph leaves the rest ragged, which makes revision
fiddly. One line per paragraph, with soft wrap in the editor, avoids that and
gives paragraph-level diffs.

Deliberately conservative. It leaves alone anything where a line ending carries
meaning:

  * fenced code blocks and $$ math blocks, verbatim
  * headings, table rows, horizontal rules, HTML comments
  * block images, which become figures only when alone in a paragraph
  * list items, including indented continuation lines
  * markdown hard breaks -- a line ending in two spaces or a backslash

Blockquotes (our callouts) are unwrapped within each of their paragraphs, keeping
the "> " prefix.

    python3 tools/unwrap.py --check   # report what would change
    python3 tools/unwrap.py           # rewrite in place
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(HERE, "content", "chapters")

HEADING = re.compile(r"^#{1,6}\s")
TABLE = re.compile(r"^\s*\|")
IMAGE = re.compile(r"^\s*!\[")
COMMENT = re.compile(r"^\s*<!--")
RULE = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")
LIST = re.compile(r"^\s*([-*+]|\d+[.)])\s")
INDENTED = re.compile(r"^\s{2,}\S")
HARDBREAK = re.compile(r"(\s{2,}|\\)$")
FENCE = re.compile(r"^\s*(```|~~~)")
MATH = re.compile(r"^\s*\$\$\s*$")


def unwrap(text):
    lines = text.split("\n")
    out, buf = [], []
    in_code = in_math = False

    def flush():
        if buf:
            lead = re.match(r"\s*", buf[0]).group(0)
            out.append(lead + " ".join(s.strip() for s in buf))
            buf.clear()

    for raw in lines:
        line = raw.rstrip("\n")

        if FENCE.match(line):
            flush(); out.append(line); in_code = not in_code; continue
        if in_code:
            out.append(line); continue
        if MATH.match(line):
            flush(); out.append(line); in_math = not in_math; continue
        if in_math:
            out.append(line); continue

        if not line.strip():
            flush(); out.append(""); continue

        # blockquote: unwrap inside it, keep the marker
        if line.lstrip().startswith(">"):
            body = re.sub(r"^\s*>\s?", "", line)
            if not body.strip():                      # blank line inside quote
                flush(); out.append(">"); continue
            if (HEADING.match(body) or TABLE.match(body) or IMAGE.match(body)
                    or LIST.match(body) or HARDBREAK.search(line)):
                flush(); out.append(line); continue
            buf.append("> " + body if not buf else body)
            continue
        if buf and buf[0].startswith(">"):
            flush()                                   # quote ended

        if (HEADING.match(line) or TABLE.match(line) or IMAGE.match(line)
                or COMMENT.match(line) or RULE.match(line)):
            flush(); out.append(line); continue

        if LIST.match(line):
            flush(); out.append(line); continue

        # An indented line is either a list-item continuation or indented code.
        # Joining it would dedent it and pull it out of its list, so leave it be.
        if INDENTED.match(line):
            flush(); out.append(line); continue

        if HARDBREAK.search(line):                    # break is meaningful
            flush(); out.append(line); continue

        buf.append(line)

    flush()
    # collapse runs of blank lines, keep a single trailing newline
    res = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return res.rstrip("\n") + "\n"


def main():
    check = "--check" in sys.argv
    total_before = total_after = changed = 0
    for path in sorted(glob.glob(os.path.join(CHAPTERS, "*.md"))):
        src = open(path, encoding="utf-8").read()
        dst = unwrap(src)
        nb = len([l for l in src.split("\n") if l.strip()])
        na = len([l for l in dst.split("\n") if l.strip()])
        total_before += nb; total_after += na
        if src != dst:
            changed += 1
            print(f"  {os.path.basename(path):30s} {nb:4d} -> {na:4d} non-blank lines")
            if not check:
                open(path, "w", encoding="utf-8").write(dst)
    verb = "would change" if check else "changed"
    print(f"\n{verb} {changed} file(s); {total_before} -> {total_after} non-blank lines")


if __name__ == "__main__":
    main()
