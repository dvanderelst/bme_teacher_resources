# BmE teacher resources

Teacher-facing materials for **Biology Meets Engineering**, a transdisciplinary STEM program
run by the University of Cincinnati (Colleges of Arts and Sciences and of Engineering, and the
School of Education), supported by NSF ITEST grants DRL 1759150 and 2342578.

The materials pair animal sensory biology with robotics: students investigate how animals detect
and localize stimuli, then build and program mBot robots that do something comparable.

## Looking for the materials themselves?

This repository holds the **source** of the teaching materials and the **teacher-support bot** 
that answers questions about them. The finished document is
[**biologymeetsengineering.org**](https://www.biologymeetsengineering.org), or download it directly:

- [**PDF**](https://github.com/dvanderelst/bme_teacher_resources/releases/latest/download/BmE-teacher-materials.pdf)
  — to read or print
- [**Web version**](https://github.com/dvanderelst/bme_teacher_resources/releases/latest/download/BmE-teacher-materials.html)
  — one file, images included, opens in a browser and works offline

Both links always serve the newest edition, so they are safe to bookmark or pass on.

You do not need any of the rest of this if you just want to teach from it.

| Chapter | |
| :-- | :-- |
| Introduction to the robot | the mBot, its ports, the battery pack, which sensor goes where |
| Installing mBlock | Windows, Mac, Linux, Chromebook |
| Getting started with the robot | pairing, connecting, Live vs Upload mode, firmware |
| Running your first program | |
| Introduction to Programming | the cheese-sandwich-factory game |
| Programming the robot | mBlock basics and four challenges |
| Kinesis and Taxis | orientation mechanisms, simulated with paper grids |
| Color Vision | cone cells, color discrimination, a color-following robot |
| Sound Localization | binaural cues, artificial pinnae, robot phonotaxis |
| Sonar | echolocation, sensor directivity, obstacle avoidance, a sonar cane |
| Educational standards | NGSS and ISTE alignment per lesson |
| Required materials | what to buy, per lesson |

Plus an unnumbered colophon carrying the licence, the version, and who to write to.

## State of the work

**Every chapter has been reviewed.** What is still open is listed in [TODO.md](TODO.md), grouped by
what you need in hand to settle it — the robot, a Mac, a Chromebook, a camera, or a decision that is
the project's to make. That file and `git log` between them carry the reasoning behind the current
state; the finished text deliberately does not.

The next planned step is a chatbot to support teachers working through these materials, built from
this content so that it cannot drift out of step with it. Nothing is built yet;
[BOT-PLAN.md](BOT-PLAN.md) holds the design and the decisions taken so far.

## Layout

```
book/
├── content/          <-- THE SOURCE. Edit these files.
│   ├── chapters/     13 markdown chapters
│   ├── images/       figures
│   └── files/        handouts, media, primers, and the .mblock programs
├── metadata.yaml     title, print layout, fonts
├── preamble.tex      LaTeX for the PDF only
├── build.sh          renders content/ -> render/
├── release.sh        builds, tags and publishes an edition
├── RELEASING.md      how that works and what to do when it goes wrong
├── convert.py        one-time Notion migration. Already run. Do not re-run.
└── tools/            filters and checks used by the build

bot/
├── app/              the teacher-support chatbot
├── overlay/          hand-written pedagogy notes and misconceptions
└── knowledge/        generated knowledge base (do not hand-edit)
```

`book/render/` is deliberately not committed. It is a build artifact, and a 14 MB PDF that changes
completely on every rebuild would bloat history fast. It is distributed as a release asset instead,
which lives outside git history — see [Releasing](#releasing).

## Building

Needs `pandoc`, `xelatex` and ImageMagick.

```sh
cd book && ./build.sh
```

Produces `render/BmE-teacher-materials.pdf` and a single self-contained
`render/BmE-teacher-materials.html` (images embedded, works offline). The edition date and version
fingerprint are derived from git, so there is nothing to remember to bump; tag a commit and the
fingerprint becomes the tag rather than a bare hash.

## Releasing

```sh
cd book
./release.sh v1.0 --dry-run   # build and check; publishes nothing
./release.sh v1.0             # the real thing
```

This builds both documents, stamps them with the tag, commits the regenerated bot knowledge set so
the bot answers for the same edition, tags, pushes, and attaches the two files to a GitHub release.
The two download links at the top of this file then serve the new edition automatically — they point
at `releases/latest/`, so nothing has to be re-sent to anyone.

[**RELEASING.md**](book/RELEASING.md) explains the sequence, why it is in that order, and what to do
when a release goes wrong.

## Editing

`book/content/` is the source of truth. Edit the markdown directly and rebuild.

Each prose paragraph is one long line, so that editing a sentence does not leave the rest of the
paragraph ragged and diffs are per paragraph. `tools/unwrap.py` restores that if it drifts; it
leaves alone anything where a line ending carries meaning.

Leave revision notes to yourself as HTML comments, which pandoc drops from the PDF and a filter
strips from the HTML, so they cannot reach a reader:

```markdown
<!-- D: this contradicts the paragraph above -->
<!-- TODO: reshoot this photo once the dongle arrives -->
```

`python3 tools/notes.py` lists every outstanding note with its file, line and the heading it sits
under. `build.sh` reports the count after each build and warns loudly if one ever leaks into the
output.

`convert.py` was the one-time migration from Notion and refuses to run again unless forced —
re-running would discard hand edits. The original Notion pages are a **frozen archive**: they are
no longer maintained and should not be edited.

## Links, files and checks

Handouts, media and the mBlock programs live in `book/content/files/` and are linked relatively from
the source. `tools/abs-links.lua` rewrites those to full URLs into this repository when building, so
they still resolve from a downloaded PDF or a saved HTML file. The base URL is set in `build.sh` and
points at `main`, so a working build tracks the latest content; `release.sh` repoints it at the tag,
so a published edition's links stay frozen to the content it was built from.

Every mBlock program is linked twice: to `planet.mblock.cc`, and to our own copy in
`content/files/programs/`, because some school networks block the Makeblock site.

`python3 tools/check-links.py` checks that internal anchors resolve, that every `files/` link has a
file behind it, and that every `planet.mblock.cc` link has a local mirror. It also warns when a
link's text names a different section than the one it points at — a defect that reads fine on screen
and sends a printed reader to the wrong page. `build.sh` runs it.

`tools/xref.lua` appends a page reference to every internal link in the PDF, so cross-references
work on paper. It is not applied to the HTML, where the link is live. Give a figure an id —
`![caption](x.png){#fig:audiogram}` — and a link to it also picks up the figure number, which LaTeX
counts, so numbering cannot drift as the book is edited.

`./tools/check-overfull.sh` reports text that runs into the margin. LaTeX knows when a line does not
fit but pandoc discards the log, so this rebuilds through a kept log and lists what is left. It
should report zero; anything it does report is usually something TeX cannot break, such as a file
name or a standards code.

Two smaller pieces: `tools/strip-notes.lua` keeps revision notes out of the HTML, since pandoc only
drops them from LaTeX, and `tools/read-comments.py` pulls annotations out of a marked-up PDF and
reports which chapter and line each one lands on, which is how the review was run.

## Branding

`book/content/branding/` holds the programme logo, which goes above the title in both outputs, and
the robot bug, which sits in the running footer of the PDF. Both are the RGB versions, following the
2021 brand guidelines: RGB for screen, CMYK for print at 300 dpi or better. At the sizes used the RGB
files still resolve well past 300 dpi, and the document is read on screen far more than it is
printed.

The logo is a trademark and is **not** covered by the licence below. If you adapt these materials,
remove it.

## Licence

Teaching materials: **CC BY-NC 4.0** — share and adapt for non-commercial
purposes with attribution. Build scripts: **MIT**.

Third-party material (mBlock screenshots, Makeblock product photographs and diagrams, the
reproduced primers in `content/files/`, and everything linked externally) is
**not** covered by that grant and remains with its owners. See [LICENSE](LICENSE).
