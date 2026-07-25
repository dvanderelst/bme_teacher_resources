#!/usr/bin/env python3
"""
Read review comments out of an annotated PDF and locate each one in the markdown
source, so a comment made on page 94 can be acted on in the right chapter.

    ../.venv/bin/python tools/read-comments.py ../review/BmE-review.pdf

For each annotation it reports:
    * the page
    * the text you highlighted (if any)
    * your comment
    * the chapter file and line number where that text lives

Highlighting the text you are commenting on is what makes the last part work.
A bare sticky note gives only a page and a position, which I can still read but
cannot pin to an exact sentence.
"""
import sys, os, re, glob, unicodedata

try:
    import fitz
except ImportError:
    sys.exit("PyMuPDF missing. Run:  ../.venv/bin/python tools/read-comments.py ...")

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(HERE, "content", "chapters")

# annotation types worth reporting, mapped to a readable label
KINDS = {
    8:  "highlight", 9: "underline", 10: "squiggly", 11: "strikeout",
    0:  "sticky note", 1: "link", 2: "free text", 4: "square",
    12: "stamp", 13: "caret", 14: "ink", 15: "popup", 16: "file attachment",
}


def norm(s):
    """Normalise for matching: PDF text carries LaTeX hyphenation, ligatures and
    smart punctuation that the markdown source does not."""
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("­", "")                 # soft hyphen
    s = re.sub(r"-\s*\n\s*", "", s)             # hyphenated line break
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def load_sources():
    out = []
    for p in sorted(glob.glob(os.path.join(CHAPTERS, "*.md"))):
        lines = open(p, encoding="utf-8").read().split("\n")
        out.append((os.path.basename(p), lines,
                    [norm(l) for l in lines]))
    return out


def locate(quote, sources):
    """Find `quote` in the markdown. Tries the whole thing, then a distinctive
    fragment, since a highlight often spans a line break in the PDF."""
    q = norm(quote)
    if len(q) < 12:
        return []
    hits = []
    for name, lines, nlines in sources:
        for i, nl in enumerate(nlines):
            if q in nl:
                hits.append((name, i + 1, lines[i]))
    if hits:
        return hits
    # fall back to the longest run of words that does match
    words = q.split()
    for span in range(len(words), 3, -1):
        frag = " ".join(words[:span])
        for name, lines, nlines in sources:
            for i, nl in enumerate(nlines):
                if frag in nl:
                    hits.append((name, i + 1, lines[i]))
        if hits:
            return hits
    return []


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pdf = sys.argv[1]
    doc = fitz.open(pdf)
    sources = load_sources()

    total = 0
    for pno in range(doc.page_count):
        page = doc[pno]
        for a in page.annots() or []:
            kind = KINDS.get(a.type[0], a.type[1])
            comment = (a.info.get("content") or "").strip()
            quote = ""
            try:
                if a.type[0] in (8, 9, 10, 11):        # text-markup annots
                    quote = page.get_textbox(a.rect).strip()
            except Exception:
                pass
            if not comment and not quote:
                continue
            total += 1
            print(f"\n[{total}] page {pno + 1} — {kind}")
            if quote:
                flat = re.sub(r"\s+", " ", quote)
                print(f"     text : {flat[:300]}")
            if comment:
                print(f"     note : {comment}")
            for name, ln, src in locate(quote or comment, sources)[:3]:
                print(f"     -> {name}:{ln}")
                print(f"        {src.strip()[:160]}")
            if quote and not locate(quote, sources):
                print("     -> (could not locate in source; will need a manual look)")

    print(f"\n{total} comment(s) in {os.path.basename(pdf)}"
          f" across {doc.page_count} pages")
    if not total:
        print("No annotations found. Highlights with attached notes work best.")


if __name__ == "__main__":
    main()
