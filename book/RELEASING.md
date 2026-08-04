# Releasing an edition

How the finished PDF and HTML get to teachers, why it works the way it does, and what to do when
it goes wrong. Written to be read cold, months later.

## The idea in one paragraph

Teachers get **one link that never changes**. GitHub keeps a permanent redirect from
`releases/latest/download/<filename>` to whatever the newest release holds, so publishing a new
edition silently updates every link already handed out — nothing to re-send, no `guide_v3_final.pdf`
circulating alongside `guide_v4.pdf`. The redirect is keyed on the **file name**, which is the one
thing in this system that must never change:

```
https://github.com/dvanderelst/bme_teacher_resources/releases/latest/download/BmE-teacher-materials.pdf
https://github.com/dvanderelst/bme_teacher_resources/releases/latest/download/BmE-teacher-materials.html
```

The repository is public, so neither link asks for a GitHub account or a login. Both are downloads:
the HTML lands in the teacher's Downloads folder and opens from there. It is a single self-contained
file — images and all — so it works with no network afterwards. If you ever want *view in browser*
rather than *download*, that stays a job for biologymeetsengineering.org; a release cannot do it.

## Cutting a release

```sh
cd book
./release.sh v1.0 --dry-run   # build and check everything, publish nothing
./release.sh v1.0             # the real thing; asks before anything goes public
```

Do the dry run first. It runs every check, produces exactly the files a real release would carry and
leaves them in `render/`, but commits, tags, pushes and publishes nothing. Open the PDF and confirm
the footer reads `v1.0` and that there is no red *do not distribute* box on the cover.

Building regenerates `bot/knowledge/` as a side effect (see step 3 below), stamped with a tag that
does not exist yet, so a dry run restores it before exiting. Otherwise it would leave the tree dirty
and the real run would refuse on its own clean-tree guard — a rehearsal that breaks the performance.

Versions are `v1.0`, `v1.1`, `v2.0` — the script rejects anything else, so the tag names stay
sortable and predictable. There is no rule about what earns a minor versus a major bump; use your
judgement, and remember the number is mostly there so a teacher on the phone can tell you which
edition they are holding.

## What happens, in order, and why that order

The sequence is not arbitrary. Each step exists because the obvious ordering produces a document
that lies about itself.

**1. Refuse to build anything ambiguous.** On `main`, clean working tree, in sync with `origin`, tag
not already taken. Every one of these is a way to ship bytes that do not match the version number
printed on them — the single failure a teacher cannot see and cannot report usefully.

**2. Build with the tag passed in.** `build.sh` normally derives the version from
`git describe --tags`, but at this point the tag does not exist yet: it is created in step 4, on a
commit that does not exist yet either. So `release.sh` passes `BME_FINGERPRINT=v1.0` and `build.sh`
uses it instead of asking git.

This is the one place where the tail wags the dog, so it is guarded: the override is applied *after*
`build.sh` has tested the working tree for uncommitted changes. Renaming a build cannot silence the
"do not distribute" cover. If the tree is dirty you get the warning regardless of what you called
the version — and `release.sh` refuses to run on a dirty tree anyway, so you should never see it.

Handout links are also pinned in this step. Day to day, `BME_FILE_BASE` points at `main`, so the
`.docx` and `.mblock` links in a build track the latest content. For a release that is wrong: `main`
moves on, and a PDF handed out last spring would quietly start serving next spring's handouts.
`release.sh` overrides the base to `raw/v1.0/…`, freezing the links to the content that edition was
built from. Old editions stay internally consistent forever.

**3. Commit the regenerated knowledge set.** `build.sh` also rewrites `bot/knowledge/`, which *is*
tracked, so every build leaves the tree dirty. That is expected and it gets committed as
`Release v1.0`. The point is that the bot answers from the same edition as the PDF: three artifacts,
one version number. `release.sh` checks that `bot/knowledge/` is the *only* thing the build touched
and stops if anything else changed.

**4. Tag, push, publish.** The tag lands on the knowledge commit, so it covers the bot's copy of the
edition too. Then `main` and the tag are pushed, and the release is created with both files
attached. The tag must be pushed before the release exists, and both must exist before the pinned
`raw/v1.0/…` links inside the PDF resolve — which is why publishing is last.

## Where the version numbers on the page come from

Two different things, both printed in the PDF footer and on the title page:

- **Edition** — a human-facing date, taken from the date of the last commit. Nothing to bump.
- **Fingerprint** — `v1.0` on a release; on a local build, the nearest tag plus a short commit hash,
  with `-stale` appended when the tree has uncommitted changes.

So any file anyone sends you can be traced back to a commit, and a development build can never be
mistaken for a released one.

## When something goes wrong

**"tag v1.0 already exists".** Tags are cheap but releases are public; do not reuse one. Move to
`v1.1`. If the tag was genuinely a mistake and nothing was published from it,
`git tag -d v1.0 && git push origin :refs/tags/v1.0` removes it.

**"working tree has uncommitted changes".** Deliberate. Commit or stash. A release built from
uncommitted work cannot be reproduced from the tag, which defeats the point of tagging it.

**"main and origin/main have diverged".** Pull or push first. Otherwise the tag points at a commit
nobody else can see.

**The GitHub CLI is not installed.** `release.sh` does everything except the final publish, then
prints the two ways to finish: install it (`sudo apt install gh && gh auth login`) and run the one
command it gives you, or drag the two files onto
<https://github.com/dvanderelst/bme_teacher_resources/releases/new> and pick the already-pushed tag
from the list. For a handful of editions a year the web UI is genuinely fine.

**A bad release is already published.** Do not delete it and re-upload under the same tag — the
`latest` link would break for as long as no release exists, and anyone who downloaded in between has
a file whose version number now means something else. Fix the content and release `v1.1`. The old
release stays up as a historical record, which is the honest outcome.

**A release must actually come down** (wrong licence, a photograph you cannot distribute). Delete
the release on GitHub; `latest` immediately falls back to the previous one, so the link keeps
working rather than 404-ing. Then release a corrected version.

## The website

The cleanest arrangement is for biologymeetsengineering.org to link the two `latest/download` URLs
rather than host its own copies. Then cutting a release is the entire publishing step, and the site
cannot fall a version behind the repository. If the site does host copies instead, uploading them
becomes a step you have to remember, and this document cannot help you remember it.

## Why the build is not automated

A GitHub Actions workflow could build on every `v*` tag in a pandoc/TeX container, and eventually
that may be worth it. It is not done yet because the PDF depends on a specific xelatex, a specific
TeX package set and the DejaVu fonts; reproducing that in a container is a day's work, and the
output shifts under you if you get it slightly wrong. For a document released a few times a year and
built on a machine that already renders it correctly, the local script is the better trade. Revisit
if releases start being cut by more than one person.

## Files involved

```
book/release.sh      the whole procedure, with the guards described above
book/build.sh        does the rendering; honours BME_FINGERPRINT and BME_FILE_BASE
book/render/         the two artifacts. Not committed -- deliberately, see README
bot/knowledge/       regenerated by the build and committed as part of the release
```
