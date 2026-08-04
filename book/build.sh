#!/usr/bin/env bash
# Render content/ -> render/. Never writes to content/.
#
# The version is derived from git, so there is nothing to remember to bump:
#   * human-facing edition date = date of the last commit
#   * technical fingerprint     = nearest tag (if any) + short commit hash
#   * "-stale" is appended when the working tree has uncommitted changes, so a
#     local build can never be mistaken for a released one.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p render

# Handouts, media and mBlock programs travel with the repository, and are linked
# from the source relatively. tools/abs-links.lua rewrites those to full URLs, so
# they still resolve from a downloaded PDF or a saved HTML file.
#
# A day-to-day build points at main, which is what you want while editing: the
# links track the latest content. A *release* must not, because main moves on
# and a PDF handed out last spring would quietly start serving next spring's
# handouts. release.sh overrides this to point at the tag, freezing the links to
# the edition that carries them.
export BME_FILE_BASE="${BME_FILE_BASE:-https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/}"

if git rev-parse --git-dir >/dev/null 2>&1; then
  FINGERPRINT=$(git describe --tags --always --dirty 2>/dev/null || echo uncommitted)
  # Replace "dirty" with "stale" for clarity
  FINGERPRINT=${FINGERPRINT/-dirty/-stale}
  ISO=$(git log -1 --format=%cs 2>/dev/null || date +%F)
else
  FINGERPRINT=no-git; ISO=$(date +%F)
fi
EDITION=$(date -d "$ISO" +"%-d %B %Y" 2>/dev/null || echo "$ISO")

# Check if this is a stale build (uncommitted changes)
STALE=0
if [[ "$FINGERPRINT" == *-stale* ]]; then
  STALE=1
fi

# release.sh builds the documents *before* the tag exists, so it passes the tag
# it is about to create. Deliberately applied after the staleness test above: an
# override renames the build, it cannot silence the "do not distribute" cover.
FINGERPRINT="${BME_FINGERPRINT:-$FINGERPRINT}"
echo "edition: $EDITION   fingerprint: $FINGERPRINT"

# running footer, generated so the version is baked into every page
cat > render/_version.tex <<TEX
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\newcommand{\bmefoot}{\bmebug\hspace{0.45em}\footnotesize\textcolor{gray}{biologymeetsengineering.org · $EDITION · $FINGERPRINT}}
\fancyfoot[L]{\bmefoot}
\fancyfoot[R]{\footnotesize\thepage}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[L]{\bmefoot}\fancyfoot[R]{\footnotesize\thepage}}
TEX

mapfile -t CH < <(ls content/chapters/*.md | sort)
ARGS=(
  metadata.yaml "${CH[@]}"
  --from=markdown+pipe_tables+tex_math_dollars+implicit_figures
  --toc --toc-depth=2 --number-sections
  --resource-path=content:content/images:content/branding
  --lua-filter=tools/strip-notes.lua
  --lua-filter=tools/abs-links.lua
  --lua-filter=tools/xref.lua
  --metadata "subtitle=Teacher materials"
  --metadata "date=Edition of $EDITION · $FINGERPRINT"
  --metadata "subject=BmE teacher materials, edition of $EDITION ($FINGERPRINT)"
  --metadata "keywords=Biology Meets Engineering; mBot; mBlock; NGSS; ISTE; $FINGERPRINT"
)

# Add stale warning to cover if needed
if [ "$STALE" -eq 1 ]; then
  # Create a warning box for the title page
  cat > render/_stale_warning.tex <<'TEX'
\AtBeginDocument{
  \thispagestyle{empty}
  \vspace*{-2cm}
  \begin{center}
    \colorbox{red!10}{\parbox{0.9\linewidth}{
      \centering\large\bfseries
      WARNING: This is a development version with uncommitted changes.\\
      Do not distribute. Build from a clean repository for release.
    }}
    \vspace{1cm}
  \end{center}
}
TEX
  ARGS+=("--include-in-header=render/_stale_warning.tex")
fi

echo "--- PDF ---"
pandoc "${ARGS[@]}" --pdf-engine=xelatex \
  --include-in-header=preamble.tex \
  --include-in-header=render/_version.tex \
  -o render/BmE-teacher-materials.pdf
echo "--- HTML (single self-contained file) ---"
pandoc "${ARGS[@]}" --standalone --embed-resources --mathml \
  --include-before-body=content/branding/logo.html \
  -o render/BmE-teacher-materials.html
rm -f render/_version.tex
rm -f render/_stale_warning.tex 2>/dev/null || true
ls -lh render/ | awk 'NR>1{print "  "$9"  "$5}'

# --- knowledge set for the teacher-support bot -------------------------------
# Regenerated here rather than on demand, because a bot that answers from the
# working tree contradicts the PDF a teacher is holding. Same source, same
# BME_FILE_BASE, same fingerprint as the two documents above.
echo "--- knowledge (bot) ---"
BME_FINGERPRINT="$FINGERPRINT" BME_EDITION="$EDITION" python3 tools/knowledge.py

# safety net: a revision note must never reach a reader
if pdftotext render/BmE-teacher-materials.pdf - 2>/dev/null | grep -q -- '<!--'; then
  echo "  !! a revision note leaked into the PDF -- check the chapters"
fi
if grep -q -- '<!--' render/BmE-teacher-materials.html; then
  echo "  !! a revision note leaked into the HTML source"
fi
python3 tools/check-links.py --quiet || true
N=$(python3 tools/notes.py --count)
# An `if` rather than `[ ... ] && echo`: as the last line of the script, the
# test's own exit status becomes the script's, so a clean build with no
# outstanding notes would report failure. Nothing noticed while this was only
# ever run by hand, but release.sh runs under set -e and stops on it.
if [ "$N" != "0" ]; then
  echo "  $N outstanding revision note(s) -- python3 tools/notes.py"
fi
