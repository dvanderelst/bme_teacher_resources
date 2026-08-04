#!/usr/bin/env bash
# Publish an edition: build the PDF and HTML, tag them, attach them to a GitHub
# release. Teachers are given one permanent link, which GitHub redirects to the
# newest release:
#
#   https://github.com/dvanderelst/bme_teacher_resources/releases/latest/download/BmE-teacher-materials.pdf
#
# That redirect is keyed on the *file name*, so the two artifacts must keep the
# names build.sh gives them. Rename them and every link already handed out dies.
#
#   ./release.sh v1.0             build, check, then ask before publishing
#   ./release.sh v1.0 --dry-run   build and check only; touches nothing remote
#   ./release.sh v1.0 --yes       no confirmation prompt
#
# Full explanation of the sequence and why it is in this order: RELEASING.md
set -euo pipefail
cd "$(dirname "$0")"
ROOT=$(git rev-parse --show-toplevel)

REPO="dvanderelst/bme_teacher_resources"
BRANCH="main"
PDF="render/BmE-teacher-materials.pdf"
HTML="render/BmE-teacher-materials.html"

TAG=""; DRY=0; ASSUME_YES=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY=1 ;;
    --yes|-y)  ASSUME_YES=1 ;;
    -*)        echo "unknown option: $arg" >&2; exit 2 ;;
    *)         TAG="$arg" ;;
  esac
done

die() { echo "release: $*" >&2; exit 1; }

[ -n "$TAG" ] || die "give the version to release, e.g. ./release.sh v1.0"
[[ "$TAG" =~ ^v[0-9]+(\.[0-9]+)*$ ]] || die "tag should look like v1.0 or v1.2.3, got '$TAG'"

# --- refuse to build a release out of anything ambiguous ---------------------
# Every one of these has been a way to ship the wrong bytes under a version
# number that says otherwise, which is the one failure a teacher cannot see.
[ "$(git rev-parse --abbrev-ref HEAD)" = "$BRANCH" ] \
  || die "releases are cut from $BRANCH; you are on $(git rev-parse --abbrev-ref HEAD)"

[ -z "$(git status --porcelain)" ] \
  || die "working tree has uncommitted changes -- commit or stash them first"

git rev-parse -q --verify "refs/tags/$TAG" >/dev/null \
  && die "tag $TAG already exists locally; pick the next version"

git fetch --quiet origin "$BRANCH" --tags
git ls-remote --exit-code --tags origin "refs/tags/$TAG" >/dev/null 2>&1 \
  && die "tag $TAG already exists on origin; pick the next version"

[ "$(git rev-parse HEAD)" = "$(git rev-parse "origin/$BRANCH")" ] \
  || die "$BRANCH and origin/$BRANCH have diverged -- pull or push before releasing"

# --- build ------------------------------------------------------------------
# The tag does not exist yet, so build.sh cannot derive it. Hand it over, along
# with a file base pinned to the tag rather than to main, so the handout links
# inside this PDF keep resolving to the content this PDF was built from.
echo "==> building $TAG"
BME_FINGERPRINT="$TAG" \
BME_FILE_BASE="https://github.com/$REPO/raw/$TAG/book/content/" \
  ./build.sh

[ -s "$PDF" ]  || die "$PDF was not produced"
[ -s "$HTML" ] || die "$HTML was not produced"

# build.sh regenerates the bot's knowledge set, stamped with the same
# fingerprint, so a rebuild always leaves the tree dirty under bot/knowledge/.
# That is expected and gets committed below. Anything *else* changing means the
# build wrote somewhere it should not have, and the release stops.
UNEXPECTED=$(cd "$ROOT" && git status --porcelain | grep -vE '^.. bot/knowledge/' || true)
[ -z "$UNEXPECTED" ] || die "the build changed files outside bot/knowledge/:
$UNEXPECTED"

printf '%s\n' "==> built" "  $(du -h "$PDF"  | cut -f1)  $PDF" "  $(du -h "$HTML" | cut -f1)  $HTML"

if [ "$DRY" -eq 1 ]; then
  echo "==> dry run: nothing committed, tagged, pushed or published"
  echo "    the two files above are the ones a release would carry; open them"
  echo "    and check the footer reads '$TAG' before doing this for real"
  exit 0
fi

# --- confirm ----------------------------------------------------------------
if [ "$ASSUME_YES" -eq 0 ]; then
  cat <<CONFIRM

About to publish, which is public and awkward to walk back:
  commit  the regenerated bot/knowledge/ as "Release $TAG"
  tag     $TAG
  push    $BRANCH and the tag to origin
  release $TAG on GitHub, carrying the PDF and the HTML

CONFIRM
  read -r -p "go ahead? [y/N] " reply
  [[ "$reply" =~ ^[Yy]$ ]] || die "stopped; nothing was published"
fi

# --- commit, tag, push ------------------------------------------------------
# The knowledge set is committed before tagging so the tag covers the bot's
# copy of the edition too: PDF, HTML and bot all answer for the same $TAG.
if [ -n "$(cd "$ROOT" && git status --porcelain)" ]; then
  (cd "$ROOT" && git add bot/knowledge && git commit -qm "Release $TAG")
  echo "==> committed regenerated knowledge set"
fi

git tag -a "$TAG" -m "Edition $TAG"
git push --quiet origin "$BRANCH"
git push --quiet origin "$TAG"
echo "==> pushed $BRANCH and $TAG"

# --- publish ----------------------------------------------------------------
EDITION=$(git log -1 --format=%cs)
NOTES=$(cat <<NOTES
Edition $TAG · $EDITION

**[Download the PDF](https://github.com/$REPO/releases/latest/download/BmE-teacher-materials.pdf)**
· **[web version](https://github.com/$REPO/releases/latest/download/BmE-teacher-materials.html)**
(one file, images included, opens in a browser without a network connection)

Both links always point at the newest edition, so they can be shared once and
left alone. The version is printed in the footer of every PDF page.
NOTES
)

if ! command -v gh >/dev/null 2>&1; then
  cat <<MANUAL

==> the GitHub CLI (gh) is not installed, so the release itself is not created.
    Either install it -- sudo apt install gh && gh auth login -- and run

      gh release create $TAG $PDF $HTML --title "Edition $TAG"

    or do it by hand at https://github.com/$REPO/releases/new
      tag:   $TAG   (already pushed; pick it from the list)
      files: drag $ROOT/book/$PDF
             and  $ROOT/book/$HTML
MANUAL
  exit 0
fi

gh release create "$TAG" "$PDF" "$HTML" \
  --repo "$REPO" --title "Edition $TAG" --notes "$NOTES"

cat <<DONE

==> published. The permanent links, unchanged from here on:

  https://github.com/$REPO/releases/latest/download/BmE-teacher-materials.pdf
  https://github.com/$REPO/releases/latest/download/BmE-teacher-materials.html
DONE
