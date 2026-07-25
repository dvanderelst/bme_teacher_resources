#!/usr/bin/env bash
# Render content/ -> render/. Never writes to content/.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p render
CH=$(ls content/chapters/*.md | sort)
COMMON="--from=markdown+pipe_tables+tex_math_dollars+implicit_figures
        --toc --toc-depth=2 --number-sections --resource-path=content:content/images"
echo "--- PDF ---"
pandoc metadata.yaml $CH $COMMON --pdf-engine=xelatex \
  -o render/BmE-teacher-materials.pdf
echo "--- HTML (single self-contained file) ---"
pandoc metadata.yaml $CH $COMMON --standalone --embed-resources --mathml \
  -o render/BmE-teacher-materials.html
ls -lh render/ | awk 'NR>1{print "  "$9"  "$5}'
