# BmE teacher resources

Teacher-facing materials for **Biology Meets Engineering**, a transdisciplinary STEM programme
run by the University of Cincinnati (Colleges of Arts and Sciences and of Engineering, and the
School of Education), supported by NSF ITEST grants DRL 1759150 and 2342578.

The materials pair animal sensory biology with robotics: students investigate how animals detect
and localise stimuli, then build and program mBot robots that do something comparable.

## What this repository is

A single document containing everything a teacher needs, published as **a PDF to download** and
**a web version to browse**. It replaces a Notion site that teachers found awkward to use.

| Chapter | |
| :-- | :-- |
| Introduction to the robot | the mBot, its ports, and which sensor goes where |
| Installing mBlock | Windows, Mac, Linux, Chromebook |
| Getting started with the robot | pairing, connecting, Live vs Upload mode, firmware |
| Running your first program | |
| Introduction to Programming | the cheese-sandwich-factory game |
| Programming the robot | mBlock basics and four challenges |
| Kinesis and Taxis | orientation mechanisms, simulated with paper grids |
| Color Vision | cone cells, colour discrimination, a colour-following robot |
| Sound Localization | binaural cues, artificial pinnae, robot phonotaxis |
| Sonar | echolocation, sensor directivity, obstacle avoidance, a sonar cane |
| Educational standards | NGSS and ISTE alignment per lesson |
| Required materials | what to buy, per lesson |
| Optional: using the battery pack | |
| Feedback, contact and support | |

## Layout

```
book/
├── content/          <-- THE SOURCE. Edit these files.
│   ├── chapters/     14 markdown chapters
│   ├── images/       figures
│   └── files/        handouts (.docx, .pptx, .xlsx), sounds, primers
├── metadata.yaml     title, print layout, fonts
├── build.sh          renders content/ -> render/
├── convert.py        one-time Notion migration. Already run. Do not re-run.
└── tools/            small one-off maintenance scripts
```

## Building

Needs `pandoc`, `xelatex` and ImageMagick.

```sh
cd book && ./build.sh
```

Produces `render/BmE-teacher-materials.pdf` and a single self-contained
`render/BmE-teacher-materials.html` (images embedded, works offline).

## Editing

`book/content/` is the source of truth. Edit the markdown directly and rebuild.

`convert.py` was the one-time migration from Notion and refuses to run again unless forced —
re-running would discard hand edits. The original Notion pages are a **frozen archive**: they are
no longer maintained and should not be edited.

## Notes on links

Every mBlock program is linked twice: to `planet.mblock.cc`, and to a Google Drive mirror of the
same `.mblock` file, because some school networks block the Makeblock site.
`tools/add-drive-mirrors.py` records the pairing and is safe to re-run.

## Licence

Teaching materials: **CC BY-NC 4.0** — share and adapt for non-commercial
purposes with attribution. Build scripts: **MIT**.

Third-party material (mBlock screenshots, Makeblock product photographs, the
reproduced primers in `content/files/`, and everything linked externally) is
**not** covered by that grant and remains with its owners. See [LICENSE](LICENSE).
