#!/usr/bin/env bash
# Render content/ -> render/. Never writes to content/.
#
# The version is derived from git, so there is nothing to remember to bump:
#   * human-facing edition date = date of the last commit
#   * technical fingerprint     = nearest tag (if any) + short commit hash
#   * "-dirty" is appended when the working tree has uncommitted changes, so a
#     local build can never be mistaken for a released one.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p render

if git rev-parse --git-dir >/dev/null 2>&1; then
  FINGERPRINT=$(git describe --tags --always --dirty 2>/dev/null || echo uncommitted)
  ISO=$(git log -1 --format=%cs 2>/dev/null || date +%F)
else
  FINGERPRINT=no-git; ISO=$(date +%F)
fi
EDITION=$(date -d "$ISO" +"%-d %B %Y" 2>/dev/null || echo "$ISO")
echo "edition: $EDITION   fingerprint: $FINGERPRINT"

# running footer, generated so the version is baked into every page
cat > render/_version.tex <<TEX
\\usepackage{fancyhdr}
\\pagestyle{fancy}
\\fancyhf{}
\\renewcommand{\\headrulewidth}{0pt}
\\newcommand{\\bmefoot}{\\footnotesize\\textcolor{gray}{BmE teacher materials \\textperiodcentered\\ $EDITION \\textperiodcentered\\ $FINGERPRINT}}
\\fancyfoot[L]{\\bmefoot}
\\fancyfoot[R]{\\footnotesize\\thepage}
\\fancypagestyle{plain}{\\fancyhf{}\\fancyfoot[L]{\\bmefoot}\\fancyfoot[R]{\\footnotesize\\thepage}}
TEX

mapfile -t CH < <(ls content/chapters/*.md | sort)
ARGS=(
  metadata.yaml "${CH[@]}"
  --from=markdown+pipe_tables+tex_math_dollars+implicit_figures
  --toc --toc-depth=2 --number-sections
  --resource-path=content:content/images
  --metadata "date=Edition of $EDITION"
  --metadata "subtitle=Teacher materials · $FINGERPRINT"
  --metadata "subject=BmE teacher materials, edition of $EDITION ($FINGERPRINT)"
  --metadata "keywords=Biology Meets Engineering; mBot; mBlock; NGSS; ISTE; $FINGERPRINT"
)

echo "--- PDF ---"
pandoc "${ARGS[@]}" --pdf-engine=xelatex \
  --include-in-header=render/_version.tex \
  -o render/BmE-teacher-materials.pdf
echo "--- HTML (single self-contained file) ---"
pandoc "${ARGS[@]}" --standalone --embed-resources --mathml \
  -o render/BmE-teacher-materials.html
rm -f render/_version.tex
ls -lh render/ | awk 'NR>1{print "  "$9"  "$5}'
