#!/usr/bin/env python3
"""
ONE-TIME migration: Notion export  ->  book/content/

Run this once. After that, `content/` is the source of truth: edit the markdown
there by hand and use build.sh to render. This script refuses to overwrite an
existing content/chapters unless you pass --force, precisely so a stray run
cannot destroy hand edits.

    python3 convert.py            # first run
    python3 convert.py --force    # deliberately re-migrate, discarding edits
"""
import os, re, csv, sys, shutil, urllib.parse, unicodedata, hashlib, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXPORT = os.path.join(ROOT, "bme-notion-export")
SRC = os.path.join(EXPORT, "Home Page", "My Websites", "BmE Lesson Plans")
MATERIALS_CSV = os.path.join(EXPORT, "Untitled f2d6-60d0_all.csv")

CONTENT = os.path.join(HERE, "content")
CHAPTERS = os.path.join(CONTENT, "chapters")
IMAGES = os.path.join(CONTENT, "images")
FILES = os.path.join(CONTENT, "files")

# ------------------------------------------------------------------------ spec
# Each entry becomes one continuous chapter. `children` are inlined as sections
# in the order given, so a lesson and its activities read as one piece.
SPEC = [
    # --- part 1: getting started -------------------------------------------
    dict(slug="10-robot", title="Introduction to the robot",
         parent="Introduction to the robot 3dd1a687a70d4daa81054c28398ca77d.md",
         children=[], materials=None),
    dict(slug="20-installing-mblock", title="Installing mBlock",
         parent="Quick Start Guide/Installing mBlock 3a781ad79c6d81d4bfc0f2eb2c90dd76.md",
         children=[], materials=None),
    dict(slug="30-getting-started", title="Getting started with the robot",
         parent="Getting started with the robot 3a781ad79c6d81008691e118106562e5.md",
         children=[], materials=None),
    dict(slug="40-first-program", title="Running your first program",
         parent="Running your first program 2c704b6aec32473893890de0c46b8788.md",
         children=[], materials=None),
    # --- part 2: lessons ----------------------------------------------------
    dict(slug="50-intro-programming", title="Introduction to Programming",
         parent="Introduction to Programming 7bfff9e8c8ea4abebff70cf5c4df328c.md",
         children=[], materials="Intro Programming"),
    dict(slug="55-programming-the-robot", title="Programming the robot",
         parent="Programming the robot b338c690e1aa4d9b8adfa46fbf6112db.md",
         children=[], materials="Programming the robot"),
    dict(slug="60-kinesis-taxis", title="Kinesis and Taxis",
         parent="Kinesis and Taxis Lesson Plan 55ab6e320a9f4dfd9a63b8e6add10d44.md",
         children=[], materials="Taxis/Kinesis"),
    dict(slug="65-color-vision", title="Color Vision",
         parent="Color Vision Lesson Plan db4af9d2856c4944a3d87324f4e087af.md",
         children=["Color Vision Lesson Plan/Adding color sensor extension 12881ad79c6d80ac9699f8d00edb2d8d.md"],
         materials="Color Vision"),
    dict(slug="70-sound-localization", title="Sound Localization",
         parent="Sound Localization Lesson Plan ff8eee556e26443598b9f83a171c69c3.md",
         children=[
             "Sound Localization Lesson Plan/Testing artificial pinnae e59cc7d0d78c4f67bf858ffd3011c084.md",
             "Sound Localization Lesson Plan/Robot phonotaxis e0d32cddd8b7417db54ffe2cc3828983.md",
             "Sound Localization Lesson Plan/Robot phonotaxis/Adding the sound sensor extension 12881ad79c6d801c95e9da3bcda6e8b7.md",
         ], materials="Sound Localization"),
    dict(slug="75-sonar", title="Sonar",
         parent="Sonar Lesson Plan 852e95eca80846f085c069032492b4b5.md",
         children=[
             "Sonar Lesson Plan/Activity 1 Measuring the sonar’s directivity 3dd67bd81a6f4e7187b447709cce689a.md",
             "Sonar Lesson Plan/Activity 2 Acoustic mirrors f685e7673d1a40eca0864c461eae2f28.md",
             "Sonar Lesson Plan/Robot obstacle avoidance 3c7b659c1cc147fdbe327ad2f203c6d8.md",
             "Sonar Lesson Plan/Sonar cane f7a3788b39a343ec93050ac213c9836b.md",
         ], materials="Sonar"),
    # --- part 3: reference --------------------------------------------------
    dict(slug="90-standards", title="Educational standards",
         parent="Educational Standards ba857051c04244cdacc5868038818b38.md",
         children=[
             "Educational Standards/Educational standards Kinesis Taxis 00ebdeba4a0e421ea6eeabe9d769f165.md",
             "Educational Standards/Educational standards Color Vision 533c06b852774edfa7f937ac32401b2e.md",
             "Educational Standards/Educational standards Sound Localization ba7b681a26c04287884a09101e415644.md",
             "Educational Standards/Educational standards Sonar 259b9ef1ec754bae8f28026306e50588.md",
         ], materials=None),
    dict(slug="93-materials", title="Required materials",
         parent="Required materials bc0d295c4b7045cd83c53e13ddfbd256.md",
         children=[], materials=None),          # None -> the full table
    dict(slug="96-battery-pack", title="Optional: using the battery pack",
         parent="Optional Using the battery pack b11dc296a7a54746874ef1fc3be818e9.md",
         children=[], materials=None),
    dict(slug="99-contact", title="Feedback, contact and support",
         parent="Feedback, Contact, and Support 240452ce29114936aa9398ce5877a441.md",
         children=[], materials=None),
]

# Notion databases whose rows are sub-pages that must be inlined where the
# database appears. Keyed by a fragment of the exported CSV filename.
INLINE_DBS = {
    "Mounting instructions": [
        "Sonar Lesson Plan/Sonar cane/Mounting instructions/Step 1 90e184bee34c4847ab49f5eb056a9e0c.md",
        "Sonar Lesson Plan/Sonar cane/Mounting instructions/Step 2 d5df7fd1b1a94f2d8a7346d740db00d5.md",
        "Sonar Lesson Plan/Sonar cane/Mounting instructions/Step 3 589de7dea9994a38aeba4ff3ad75e407.md",
        "Sonar Lesson Plan/Sonar cane/Mounting instructions/Step 4 4a59e1c64e114acca197d6005855350b.md",
        "Sonar Lesson Plan/Sonar cane/Mounting instructions/End result ad881c1bf9a94607893286d088f4eceb.md",
    ],
}

CALLOUT_LABEL = {
    "💡": "Tip", "⚠️": "Note", "ℹ️": "Note", "❗": "Important",
    "☝🏽": "Note", "❓": "Why?", "⚪": "Note", "✅": "Note",
}

stats = {k: 0 for k in ("images", "callouts", "links_internal", "links_dropped",
                        "materials_tables", "db_junk", "captions_deduped",
                        "captions_dropped", "inlined_db_pages", "meta_stripped",
                        "attachments")}
warnings = []


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s.-]", "", s).strip().lower()
    return re.sub(r"[-\s]+", "-", s)


def strip_notion_id(name):
    name = re.sub(r"\.md$", "", name)
    return re.sub(r"\s+[0-9a-f]{32}$", "", name).strip()


def _match_delim(text, start, open_c, close_c):
    depth = 0
    for i in range(start, len(text)):
        if text[i] == open_c:
            depth += 1
        elif text[i] == close_c:
            depth -= 1
            if depth == 0:
                return i
    return -1


def replace_images(text, fn):
    """Handles nested [] in alt text, which a plain regex cannot."""
    out, i = [], 0
    while True:
        j = text.find("![", i)
        if j < 0:
            out.append(text[i:])
            return "".join(out)
        out.append(text[i:j])
        ca = _match_delim(text, j + 1, "[", "]")
        if ca < 0 or ca + 1 >= len(text) or text[ca + 1] != "(":
            out.append("![")
            i = j + 2
            continue
        ct = _match_delim(text, ca + 1, "(", ")")
        if ct < 0:
            out.append("![")
            i = j + 2
            continue
        out.append(fn(text[j + 2:ca], text[ca + 2:ct]))
        i = ct + 1


# ------------------------------------------------------------------- materials
def load_materials():
    with open(MATERIALS_CSV, encoding="utf-8-sig") as fh:
        return [{(k or "").strip(): (v or "").strip() for k, v in r.items()}
                for r in csv.DictReader(fh)]


def materials_table(rows, lesson):
    sel = [r for r in rows
           if not lesson or lesson.lower() in r.get("Lesson Plans", "").lower()]
    if not sel:
        warnings.append(f"no materials matched {lesson!r}")
        return ""
    stats["materials_tables"] += 1
    out = ["", "| Item | Description |", "| :--- | :--- |"]
    for r in sel:
        d = r.get("Description", "").replace("|", "/").replace("\n", " ")
        out.append(f"| {r.get('Item','').replace('|','/')} | {d} |")
    return "\n".join(out + [""])


# ---------------------------------------------------------------------- images
MAX_WIDTH = 1400
PHOTO_COLOUR_THRESHOLD = 30000


def _optimise(src_abs, dst_noext):
    try:
        colours = int(subprocess.run(["identify", "-format", "%k", src_abs],
                                     capture_output=True, text=True,
                                     check=True).stdout.strip() or 0)
    except Exception:
        colours = 0
    is_photo = colours > PHOTO_COLOUR_THRESHOLD
    dst = dst_noext + (".jpg" if is_photo else ".png")
    cmd = ["convert", src_abs, "-auto-orient",
           "-resize", f"{MAX_WIDTH}x{MAX_WIDTH}>", "-strip"]
    cmd += ["-quality", "85"] if is_photo else \
           ["-define", "png:compression-level=9"]
    try:
        subprocess.run(cmd + [dst], check=True, capture_output=True)
    except Exception:
        warnings.append(f"optimise failed: {os.path.basename(src_abs)}")
        dst = dst_noext + os.path.splitext(src_abs)[1].lower()
        shutil.copy2(src_abs, dst)
    return os.path.basename(dst)


def copy_image(src_abs):
    if not os.path.exists(src_abs):
        warnings.append(f"missing image: {src_abs}")
        return None
    base = slugify(strip_notion_id(os.path.basename(os.path.dirname(src_abs)))) or "img"
    stem = f"{base}-{hashlib.md5(src_abs.encode()).hexdigest()[:8]}"
    hit = [f for f in os.listdir(IMAGES) if f.startswith(stem + ".")]
    name = hit[0] if hit else _optimise(src_abs, os.path.join(IMAGES, stem))
    stats["images"] += 1
    return f"images/{name}"


ATTACH_EXT = {".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls", ".pdf",
              ".wav", ".mp3", ".mp4", ".mov", ".mblock", ".zip", ".ods"}


def copy_attachment(src_abs):
    """Handouts, sounds, programs. Kept as real files so the links work."""
    if not os.path.exists(src_abs):
        warnings.append(f"missing attachment: {src_abs}")
        return None
    name = os.path.basename(src_abs)
    dst = os.path.join(FILES, name)
    if os.path.exists(dst) and not os.path.samefile(src_abs, dst):
        stem, ext = os.path.splitext(name)
        name = f"{stem}-{hashlib.md5(src_abs.encode()).hexdigest()[:6]}{ext}"
        dst = os.path.join(FILES, name)
    if not os.path.exists(dst):
        shutil.copy2(src_abs, dst)
    stats["attachments"] += 1
    return f"files/{name}"


# ----------------------------------------------------------------- page -> md
def convert_page(path, shift, page_index, mat_rows, mat_filter, depth=0):
    text = open(path, encoding="utf-8", errors="replace").read()
    base_dir = os.path.dirname(path)
    lines = text.split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].startswith("# "):
        lines.pop(0)
    text = "\n".join(lines)

    # Notion database-row metadata ("Created: May 20, 2024 12:27 PM", "Status: ...")
    def drop_meta(m):
        stats["meta_stripped"] += 1
        return ""
    text = re.sub(r"^(Created|Status|Tags|Owner|Lesson Plans?|Count|Type|Link):.*$\n?",
                  drop_meta, text, flags=re.M)

    # callouts
    def fix_aside(m):
        body = m.group(1).strip()
        label = "Note"
        for emoji, lab in CALLOUT_LABEL.items():
            if body.startswith(emoji):
                label, body = lab, body[len(emoji):].strip()
                break
        else:
            body = re.sub(r"^[^\w*\[]+", "", body).strip()
        stats["callouts"] += 1
        quoted = "\n".join("> " + l if l.strip() else ">" for l in body.split("\n"))
        return f"\n> **{label}**\n>\n{quoted}\n"
    text = re.sub(r"<aside>(.*?)</aside>", fix_aside, text, flags=re.S)

    # databases: either inline their sub-pages, or render the materials table
    def fix_db(label, target):
        name = urllib.parse.unquote(os.path.basename(target))
        for key, pages in INLINE_DBS.items():
            if key.lower() in name.lower():
                parts = []
                for p in pages:
                    ttl = strip_notion_id(os.path.basename(p))
                    parts.append(f"## {ttl}\n")
                    parts.append(convert_page(os.path.join(SRC, p), 0,
                                              page_index, mat_rows, mat_filter,
                                              depth + 1))
                    stats["inlined_db_pages"] += 1
                return "\n\n" + "\n\n".join(parts) + "\n"
        return materials_table(mat_rows, mat_filter)

    def db_sub(m):
        stats["db_junk"] += 1
        return fix_db(m.group(1), m.group(2))
    text = re.sub(r"\[([^\]]*)\]\(([^)]*\.csv)\)\s*\n+filters:[^\n]*\n[^\n]*\n",
                  db_sub, text)
    text = re.sub(r"\[([^\]]*)\]\(([^)]*\.csv)\)", db_sub, text)

    # images
    def fix_img(alt, target):
        # inlined sub-pages have already been converted; don't reprocess them
        if target.startswith("images/"):
            return f"![{alt}]({target})"
        alt = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", alt).strip().replace("|", "/")
        # Notion uses the filename as alt text when an image has no caption:
        # "Untitled", "image.png", "3.png", "2026-06-03_19-47.png". A real
        # caption is never a single token ending in an image extension.
        if (not alt
                or re.fullmatch(r"(untitled|image|screenshot)[\s\d_.-]*"
                                r"(png|jpe?g|gif|bmp|svg)?", alt, re.I)
                or re.fullmatch(r"\S+\.(png|jpe?g|gif|bmp|svg)", alt, re.I)):
            stats["captions_dropped"] += 1
            alt = ""
        if target.startswith("http"):
            return f"![{alt}]({target})"
        new = copy_image(os.path.normpath(
            os.path.join(base_dir, urllib.parse.unquote(target))))
        return f"![{alt}]({new})" if new else ""
    text = replace_images(text, fix_img)

    # Notion repeats an image's caption as the next paragraph; drop the copy
    kept, prev = [], None
    for ln in text.split("\n"):
        m = re.match(r"!\[([^\]]*)\]\(", ln)
        if m:
            prev = m.group(1).strip()
            kept.append(ln)
            continue
        if prev and ln.strip() == prev and ln.strip():
            stats["captions_deduped"] += 1
            prev = None
            continue
        if ln.strip():
            prev = None
        kept.append(ln)
    text = "\n".join(kept)

    # links to other exported pages
    def fix_link(m):
        label, target = m.group(1), m.group(2)
        if target.startswith(("http", "mailto", "#")):
            return m.group(0)
        name = strip_notion_id(os.path.basename(urllib.parse.unquote(target)))
        if name in page_index:
            stats["links_internal"] += 1
            return f"[{label}](#{page_index[name]})"
        stats["links_dropped"] += 1
        return label
    text = re.sub(r"\[([^\]]*)\]\(([^)]+\.md[^)]*)\)", fix_link, text)

    def fix_attach(m):
        label, target = m.group(1), m.group(2)
        if target.startswith(("http", "mailto", "#", "files/", "images/")):
            return m.group(0)
        ext = os.path.splitext(urllib.parse.unquote(target))[1].lower()
        if ext not in ATTACH_EXT:
            return m.group(0)
        new = copy_attachment(os.path.normpath(
            os.path.join(base_dir, urllib.parse.unquote(target))))
        return f"[{label}]({new})" if new else label
    text = re.sub(r"\[([^\]]*)\]\(([^)]+)\)", fix_attach, text)

    # headings
    def fix_head(m):
        body = re.sub(r"^\*\*(.*)\*\*$", r"\1", m.group(2).strip()).strip()
        return "#" * min(6, len(m.group(1)) + shift) + " " + body
    text = re.sub(r"^(#{1,6})\s+(.*)$", fix_head, text, flags=re.M)

    text = text.replace(r"\begin{align}", r"\begin{aligned}") \
               .replace(r"\end{align}", r"\end{aligned}")
    text = text.replace("\xa0", " ")
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def main():
    force = "--force" in sys.argv
    if os.path.isdir(CHAPTERS) and os.listdir(CHAPTERS) and not force:
        sys.exit("content/chapters already exists.\n"
                 "This is a one-time migration and content/ is now the source of\n"
                 "truth -- re-running would discard hand edits. Use --force only\n"
                 "if you really mean to re-migrate from Notion.")
    for d in (CONTENT, CHAPTERS, IMAGES, FILES):
        os.makedirs(d, exist_ok=True)
    if force:
        for d in (CHAPTERS, IMAGES, FILES):
            for f in os.listdir(d):
                os.remove(os.path.join(d, f))

    mat = load_materials()
    page_index = {}
    for ch in SPEC:
        page_index[strip_notion_id(os.path.basename(ch["parent"]))] = slugify(ch["title"])
        for c in ch["children"]:
            n = strip_notion_id(os.path.basename(c))
            page_index[n] = slugify(n)

    for ch in SPEC:
        parts = [f"# {ch['title']}\n"]
        parts.append(convert_page(os.path.join(SRC, ch["parent"]), 1,
                                  page_index, mat, ch["materials"]))
        for c in ch["children"]:
            parts.append(f"\n## {strip_notion_id(os.path.basename(c))}\n")
            parts.append(convert_page(os.path.join(SRC, c), 2,
                                      page_index, mat, ch["materials"]))
        body = "\n\n".join(p for p in parts if p.strip()) + "\n"
        open(os.path.join(CHAPTERS, ch["slug"] + ".md"), "w",
             encoding="utf-8").write(body)
        print(f"  {ch['slug']+'.md':32s} {len(body.split()):>6,} words")

    print("\nstats:")
    for k, v in stats.items():
        print(f"  {k:20s} {v}")
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w in dict.fromkeys(warnings):
            print("  -", w)


if __name__ == "__main__":
    main()
