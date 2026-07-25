#!/usr/bin/env python3
"""
Check the links in the chapter source.

Four classes of defect have actually happened in this book, and each is silent:

  * an anchor that points at no heading -- pandoc emits a dangling reference
  * an anchor that resolves but names a different section than its link text,
    which reads fine on screen and sends a reader to the wrong page in print
  * a files/ link with no file behind it
  * an mBlock program linked on planet.mblock.cc with no local mirror, so a
    school that blocks the Makeblock site has no route to it

The second one is a heuristic and will have false positives -- link text like
"here" can point anywhere -- so it is reported separately as a warning.

    python3 tools/check-links.py          # report
    python3 tools/check-links.py --quiet  # only complain, for use in build.sh
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(HERE, "content", "chapters")
CONTENT = os.path.join(HERE, "content")

LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$", re.M)
PLANET = re.compile(r"https://planet\.mblock\.cc/project/\d+")


def slug(text):
    t = re.sub(r"\{.*?\}", "", text).strip().lower()
    t = re.sub(r"[*`_]", "", t)
    t = re.sub(r"[^\w\s-]", "", t)
    return re.sub(r"\s+", "-", t).strip("-")


def main():
    quiet = "--quiet" in sys.argv
    files = sorted(glob.glob(os.path.join(CHAPTERS, "*.md")))
    texts = {f: open(f, encoding="utf-8").read() for f in files}

    anchors = set()
    for t in texts.values():
        for m in HEADING.finditer(t):
            anchors.add(slug(m.group(2)))

    broken, missing, mismatched = [], [], []
    planet_links, mirrors = 0, 0

    for f, t in texts.items():
        name = os.path.basename(f)
        for m in LINK.finditer(t):
            text, target = m.group(1), m.group(2)
            line = t.count("\n", 0, m.start()) + 1
            if target.startswith("#"):
                a = target[1:]
                if a not in anchors:
                    broken.append((name, line, text, a))
                else:
                    want = slug(text)
                    # only flag when the text plainly names a section
                    if len(want) > 12 and want != a and want not in a and a not in want:
                        mismatched.append((name, line, text, a))
            elif target.startswith("files/"):
                if not os.path.exists(os.path.join(CONTENT, target)):
                    missing.append((name, line, target))
                if target.endswith(".mblock"):
                    mirrors += 1
        planet_links += len(PLANET.findall(t))

    bad = len(broken) + len(missing)
    if not quiet:
        print(f"  {len(anchors)} headings")
        print(f"  {planet_links} mBlock programs linked, {mirrors} local mirrors")
    if planet_links != mirrors:
        print(f"  !! {planet_links} planet.mblock.cc links but {mirrors} mirrors")
        bad += 1
    for n, l, txt, a in broken:
        print(f"  !! {n}:{l} broken anchor #{a}  [{txt}]")
    for n, l, tgt in missing:
        print(f"  !! {n}:{l} no such file {tgt}")
    if mismatched and not quiet:
        print(f"\n  {len(mismatched)} link(s) whose text may not match their target:")
        for n, l, txt, a in mismatched:
            print(f"     {n}:{l} [{txt}] -> #{a}")
    if not bad and not quiet:
        print("  no broken links")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
