#!/usr/bin/env python3
"""
List revision notes left in the chapter source.

Notes are HTML comments, which pandoc drops from the PDF, so they cannot reach a
reader:

    <!-- D: this contradicts the paragraph above -->
    <!-- D: reshoot this photo once the dongle arrives -->

Usage:
    python3 tools/notes.py            # list every outstanding note
    python3 tools/notes.py --count    # just the number (used by build.sh)
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(HERE, "content", "chapters")

# <!-- D: ... -->  or  <!-- TODO: ... -->  (case-insensitive, may span lines)
NOTE = re.compile(r"<!--\s*(D|TODO|NOTE|FIXME|Q)\s*:\s*(.*?)-->",
                  re.S | re.I)


def collect():
    found = []
    for path in sorted(glob.glob(os.path.join(CHAPTERS, "*.md"))):
        text = open(path, encoding="utf-8").read()
        for m in NOTE.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            body = " ".join(m.group(2).split())
            # the nearest heading above, so the note has context
            heads = re.findall(r"^(#{1,6})\s+(.*)$",
                               text[:m.start()], re.M)
            where = heads[-1][1].strip() if heads else ""
            found.append((os.path.basename(path), line, m.group(1).upper(),
                          body, where))
    return found


def main():
    notes = collect()
    if "--count" in sys.argv:
        print(len(notes))
        return
    if not notes:
        print("No outstanding notes.")
        return
    current = None
    for fname, line, kind, body, where in notes:
        if fname != current:
            print(f"\n{fname}")
            current = fname
        print(f"  {line:>5}  [{kind}] {body}")
        if where:
            print(f"         under: {where}")
    print(f"\n{len(notes)} outstanding note(s)")


if __name__ == "__main__":
    main()
