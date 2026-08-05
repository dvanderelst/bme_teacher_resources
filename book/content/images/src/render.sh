#!/usr/bin/env bash
# Render the drawn figures: src/*.svg -> ../<name>.png at print resolution.
#
# The book's other images are photographs and screenshots, which arrive as
# raster and stay that way. These are diagrams we drew, so the SVG is the
# source and the PNG is output -- edit the SVG, run this, commit both. The PNG
# is committed rather than built by build.sh because inkscape is a heavy
# dependency to require of anyone who only wants to rebuild the book, and these
# change about once a year.
#
# 300 dpi at the drawing's own size, which is what the brand guidelines ask for
# in print and comfortably more than the page needs.
set -euo pipefail
cd "$(dirname "$0")"

for svg in *.svg; do
  [ -e "$svg" ] || continue
  png="../${svg%.svg}.png"
  inkscape --export-type=png --export-dpi=300 --export-filename="$png" "$svg" >/dev/null 2>&1
  printf '  %-44s %s\n' "$svg" "$(du -h "$png" | cut -f1)"
done
