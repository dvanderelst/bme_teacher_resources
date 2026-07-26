#!/usr/bin/env bash
# Report text that runs into the margin.
#
# LaTeX knows when a line does not fit and says so, but pandoc throws the log
# away, so these went unnoticed until someone read the PDF and spotted one. This
# rebuilds through a kept log and lists what it complains about, worst first.
#
# An overfull box is usually something TeX cannot break: a file name, a block
# name, a standards code, a word with a slash in it. Small ones are absorbed by
# \emergencystretch in preamble.tex; anything still listed here needs the text
# changed.
#
#     ./tools/check-overfull.sh
set -euo pipefail
cd "$(dirname "$0")/.."

WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT

export BME_FILE_BASE="https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/"
mapfile -t CH < <(ls content/chapters/*.md | sort)

pandoc metadata.yaml "${CH[@]}" \
  --from=markdown+pipe_tables+tex_math_dollars+implicit_figures \
  --toc --toc-depth=2 --number-sections \
  --resource-path=content:content/images \
  --lua-filter=tools/strip-notes.lua \
  --lua-filter=tools/abs-links.lua \
  --lua-filter=tools/xref.lua \
  --include-in-header=preamble.tex \
  --standalone -o "$WORK/book.tex" 2>/dev/null

cp -r content/images "$WORK/" 2>/dev/null || true
( cd "$WORK" && xelatex -interaction=nonstopmode book.tex >/dev/null 2>&1 || true
                xelatex -interaction=nonstopmode book.tex >/dev/null 2>&1 || true )

N=$(grep -c 'Overfull \\hbox' "$WORK/book.log" || true)
echo "  $N overfull box(es)"
[ "$N" = "0" ] && exit 0

# each report is followed by the offending text, and a [page] marker later
grep -A3 'Overfull \\hbox' "$WORK/book.log" \
  | grep -E 'Overfull \\hbox|TU/DejaVu' \
  | sed -E 's/Overfull \\hbox \(([0-9.]+)pt too wide\).*/\n  == \1pt too wide/; s/\\TU\/[A-Za-z()0-9\/]+ //g; s/^/    /' \
  | head -60
