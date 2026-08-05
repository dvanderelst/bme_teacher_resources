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
# Full explanation of the sequence and why it is in this order:
# BUILDING_AND_RELEASING.md in the repository root.
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
  # Put the knowledge set back. The build stamped it with a tag that does not
  # exist, and leaving it dirty would make the real run refuse on its own
  # clean-tree guard -- a dry run that breaks the release it is rehearsing for.
  # Safe to do bluntly: the tree was verified clean above, so this restores it
  # exactly, and everything under bot/knowledge/ is generated in the first place.
  (cd "$ROOT" && git checkout -q -- bot/knowledge && git clean -qfd bot/knowledge)
  echo "==> dry run: nothing committed, tagged, pushed or published"
  echo "    bot/knowledge/ restored; render/ still holds the two files above"
  echo "    open them and check the footer reads '$TAG' before doing this for real"
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
PAGES_URL="https://${REPO%%/*}.github.io/${REPO#*/}/"
NOTES=$(cat <<NOTES
Edition $TAG · $EDITION

**[Read it in your browser]($PAGES_URL)** · **[Download the PDF](https://github.com/$REPO/releases/latest/download/BmE-teacher-materials.pdf)**

Or [download the web version](https://github.com/$REPO/releases/latest/download/BmE-teacher-materials.html)
to keep: one file with the images inside it, which works with no network once
saved, and reflows on a phone or tablet in a way the PDF cannot.

All three links always point at the newest edition, so they can be shared once
and left alone. The version is printed in the footer of every PDF page.
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

# --- the readable-in-a-browser copy -----------------------------------------
# Release assets are always sent as downloads: GitHub stamps every one of them
# content-disposition: attachment, deliberately, so nobody can host arbitrary
# HTML and JavaScript on github.com. No file name or content type gets around
# it. So the HTML in the release is a file a teacher saves and opens, and this
# is the copy they can simply read: GitHub Pages serves the same document at a
# fixed address, which is also what a website would point an iframe at.
#
# Built with plumbing rather than a checkout, because switching branches in a
# Dropbox folder invites the sync client to fight the working tree. Nothing
# here touches it: the file is hashed straight into the object database and a
# parentless commit is pushed over whatever gh-pages held.
#
# Parentless is the point. The branch keeps no history, so each release makes
# the previous 20 MB copy unreachable rather than stacking another one up on
# top of it, and the repository does not grow by an edition every time.
echo "==> publishing the readable copy to GitHub Pages"
HTML_BLOB=$(git hash-object -w "$HTML")
EMPTY_BLOB=$(git hash-object -w -t blob /dev/null)
# .nojekyll stops Pages running the document through Jekyll, which would try to
# interpret parts of it as a template and mangle them.
TREE=$(printf '100644 blob %s\tindex.html\n100644 blob %s\t.nojekyll\n' \
  "$HTML_BLOB" "$EMPTY_BLOB" | git mktree)
PAGES_COMMIT=$(git commit-tree "$TREE" -m "Edition $TAG")

if git push --quiet --force origin "$PAGES_COMMIT:refs/heads/gh-pages"; then
  # Turning Pages on is a one-off; 409 means it already is, which is fine.
  gh api -X POST "repos/$REPO/pages" \
    -f "source[branch]=gh-pages" -f "source[path]=/" >/dev/null 2>&1 || true
  echo "    pushed; Pages takes a minute or two to rebuild"
else
  echo "    !! the Pages push failed. The release itself is published and fine;"
  echo "       only the read-in-a-browser copy is still on the previous edition."
fi

cat <<DONE

==> published, and the documents are done. One step left, and it is not
    automatic: the bot is still answering from the previous edition.

      python bot/scripts/configure_agent.py

    That pushes the knowledge set this release just committed to Mistral.
    It is deliberately separate -- it needs an API key, it talks to a live
    service, and it is the one step here that changes what teachers are
    told rather than what they can download.

==> the permanent links, unchanged from here on:

  read in a browser  $PAGES_URL
  download the PDF   https://github.com/$REPO/releases/latest/download/BmE-teacher-materials.pdf
  download the HTML  https://github.com/$REPO/releases/latest/download/BmE-teacher-materials.html
DONE
