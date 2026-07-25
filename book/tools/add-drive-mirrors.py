#!/usr/bin/env python3
"""
One-off (idempotent) edit of content/chapters: after every link to a program on
planet.mblock.cc, add a direct Google Drive mirror.

Why: some schools block the Makeblock site. The old Notion page "All mBot
programs" carried a single link to a Drive *folder* as a fallback; that page is
not part of the book, so instead each program now names its own mirror.

Safe to re-run: lines that already carry a Drive link are skipped.

    python3 tools/add-drive-mirrors.py [--dry-run]
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS = os.path.join(HERE, "content", "chapters")

# planet.mblock.cc project id -> (program name, Google Drive file id)
# Pairing taken from the Notion bookmark titles; Drive ids read from the shared
# folder 1Y4nvCqRsjATdGCejyM5iZIFyEw06Hzfa (all files are "anyone: commenter").
MIRRORS = {
    "3934903": ("MyFirstProgram",                    "1XCEIlMv4KOro7h_ZQQajJ_j_5QhLtC34"),
    "3916152": ("sonar_directionality",              "1ycsKwRZEAqmBKjQ5AxTq4WWw4T5JBfVx"),
    "3916162": ("sonar_obstacle_avoidance",          "1-NNPwR_EeliOnSDDOA87IJ-XHtJDunZ1"),
    "3916250": ("sonar_cane",                        "1nENLgknP-9-Gud3_HAl-3C0QFPo1bq6T"),
    "3941521": ("sound_localization_directionality", "1hKiYFX9wSxCGxuLkfC3UYyaonUeW_tbo"),
    "3941523": ("sound_localization_approach",       "1-cUC4kOW5Fy2Qy7libpa73puB28lPIS_"),
    "3954097": ("color_vision_communication",        "1HsO5T4I7fSO7VC-iYbI_eH1SbMnlvQkI"),
    "3954308": ("color_vision_motion",               "1kIi6T0hHREPmvZpEvC-I0OGfBcrrUTfW"),
}

DRIVE = "https://drive.google.com/file/d/{}/view?usp=sharing"
LINK_RE = re.compile(
    r"\[([^\]]*)\]\((https://planet\.mblock\.cc/project/(\d+))\)")

dry = "--dry-run" in sys.argv
changed = skipped = unknown = 0

for path in sorted(glob.glob(os.path.join(CHAPTERS, "*.md"))):
    text = open(path, encoding="utf-8").read()
    out, last = [], 0
    for m in LINK_RE.finditer(text):
        label, url, pid = m.group(1), m.group(2), m.group(3)
        # already mirrored? look at the rest of this line
        eol = text.find("\n", m.end())
        tail = text[m.end():eol if eol > 0 else len(text)]
        if "drive.google.com" in tail:
            skipped += 1
            continue
        if pid not in MIRRORS:
            unknown += 1
            print(f"  ! no mirror known for project {pid} in {os.path.basename(path)}")
            continue
        name, fid = MIRRORS[pid]
        # tidy the Notion bookmark title, keep any hand-written label
        new_label = name if label.endswith("- mBlock Community") or not label.strip() else label
        repl = (f"[{new_label}]({url}) — or "
                f"[download `{name}.mblock` directly]({DRIVE.format(fid)}) "
                f"if your school blocks the Makeblock site.")
        out.append(text[last:m.start()])
        out.append(repl)
        last = m.end()
        changed += 1
    if out:
        out.append(text[last:])
        new = "".join(out)
        if not dry:
            open(path, "w", encoding="utf-8").write(new)
        print(f"  {'would update' if dry else 'updated'} {os.path.basename(path)}")

print(f"\n{changed} mirrored, {skipped} already had one, {unknown} unknown")
