# Teacher-support bot — design notes

Notes for the next big step: a chatbot that supports teachers **teaching from these materials**. It is
modelled on the agent used in the related summer program (`bme_agent`, a separate repository), but
simpler, and it shares nothing with it — that program runs on different hardware (mBot Ranger, where
this book is the mBot/mCore) and serves students rather than teachers.

Nothing here is built yet. This file exists so the reasoning is not lost between sessions.

*Written 2026-07-26, against fingerprint `6b1113d`. The counts below were measured at that commit and
will drift as chapters are edited; re-measure before relying on them.*

---

## Decisions taken

### Build it in this repository

Considered against a separate repository, and this repository wins for one reason that outweighs the
rest: **the bot is a view of the book, not a product beside it.** It has no knowledge that does not
originate here and no reason to exist apart from these materials. When something in a chapter turns
out to be wrong, the chapter and the bot's knowledge should be fixed in one commit and released under
one tag. Split across repositories, that becomes a bump commit and a window during which the bot
contradicts the PDF a teacher is holding — which is the worst failure this thing has.

The usual arguments for splitting — independent release cadence, separate teams, separate access
control — all presuppose an organisational separation that does not exist here.

### But the bot reads a built artifact, never `content/` directly

This is the rule to hold onto, and it is about *when* rather than *where*. Chapters get edited in
progress; a teacher-facing bot must serve the **edition that was published**, not whatever is in the
working tree. Co-location does not force live reading, so both properties are available.

It also happens to be necessary for a second reason: chapters are written for print, and carry
constructs that are meaningless or harmful in a chat window. See the conversion spec below.

### `build.sh` regenerates the knowledge

The right place, because `build.sh` already holds the two things the conversion needs: `BME_FILE_BASE`
for resolving relative links to absolute URLs, and the git-derived fingerprint, so a knowledge set can
always be traced to the edition it came from.

### The bot shows images

Decided. There are 160 of them, and for the commonest kind of question a teacher asks mid-lesson —
"which button do I click?" — the mBlock screenshot *is* most of the answer. So chunks carry the
resolved image URL alongside the caption text rather than dropping the path.

---

## Proposed layout

```
book/                        unchanged
book/tools/knowledge.py      chapters -> knowledge set; run by build.sh
bot/
├── knowledge/               generated. Do not hand-edit.
├── overlay/                 hand-written: misconceptions, teacher-asks-X-say-Y
└── app/                     the bot itself
```

The converter belongs in `book/tools/` beside `strip-notes.lua` and `abs-links.lua`, because it has to
track chapter structure and will break when chapter structure changes. The overlay belongs with the
bot, because it is not derived from the book.

**Facts flow from the book; the pedagogy overlay lives with the bot; the seam is a version number.**

---

## Conversion spec: what has to happen to the chapter files

Ordered by how much it matters. Counts measured across the 14 chapters.

### 1. Keep captions as text; drop the image *markup*, keep the resolved URL

The single most important item, and the easy thing to get wrong. The 160 image captions carry **3,411
words, 11% of all prose in the book**, and since the captioning work finished they are load-bearing
instruction rather than decoration:

> "The block that switches the sensor's white fill LEDs off. Note that the port dropdown reads
> `port1`; set it to the port the color sensor is actually plugged into…"

Stripping `![...](...)` lines throws away an eighth of the knowledge, including much of the
watch-out-for-this content. Emit the caption as a sentence, and — since the bot shows images — keep
the resolved URL attached to the chunk.

### 2. Resolve links rather than stripping them

39 `files/` links and 100 external links. `abs-links.lua` already rewrites the first group to absolute
URLs using `BME_FILE_BASE`; reuse that logic so the bot can answer with the handout itself rather than
merely mentioning that one exists. A bot that produces *Rules for Kinesis* on request is considerably
more useful than one that says the file is somewhere in the repository.

### 3. Flatten internal cross-references to their link text

63 of them. For print, `xref.lua` expands these to "(Figure 9.23, on page 131)", which is noise in a
chat window. The link *text*, however, is actionable — keep the phrase, discard the anchor:

> "See Getting started with the robot for USB connection instructions."

### 4. Preserve tables verbatim

112 pipe-table rows. The port table, the per-lesson materials lists and the NGSS/ISTE alignment are
lookup data; prose-flattening destroys them. Markdown tables retrieve perfectly well — leave them.

### 5. Label the callouts explicitly

39 `> **Note**` / `> **Tip**` blocks. Per word these are the highest-value content in the book, being
the accumulated gotchas — the dongle button undoing a pairing, the colour sensor only working in
Upload mode. Mark them so a chunker cannot split one mid-block, and so retrieval can weight them.

### 6. Strip the pandoc and LaTeX machinery

`{.unnumbered}` (6), `{#fig:...}` (9), and `<!-- ... -->` revision notes. Mechanical.

Also **do not carry chapter numbers.** Pandoc computes them from `--number-sections`, so they shift
whenever a chapter is reordered — and reordering is still an open question (TODO 4.1). Carry chapter
*titles*.

There is no maths to handle: zero `$...$` spans in the book.

---

## Chunking

The structure is unusually cooperative. 215 sections, and the **longest is 719 words**, so nothing
needs splitting — chunk at H2/H3 and the top end takes care of itself.

The bottom end is the problem: **64 of 215 sections are under 40 words**, and one
(*Using mBlock in the browser*) contains nothing but an image. These must merge upward into their
parent or they become useless fragments.

Not optional: every chunk needs a **breadcrumb** — chapter title, then section path. The prose says
"the robot", "the sensor", "the dial" constantly, with the referent sitting in the heading. A chunk
retrieved without its heading is frequently ambiguous about which sensor it is even discussing.

---

## Chores this repository will need

Small, but each is deliberate, because this repository is curated to be a clean public artifact.

- [ ] **`.gitignore` is a whitelist** (`/*`, then re-admit). A new top-level `bot/` is invisible until
      `!/bot/` is added. That is the design working as intended, not an obstacle.
- [ ] **`LICENSE`** splits CC BY-NC 4.0 for the materials and MIT for "build scripts". Bot code
      belongs in the MIT half, but the wording needs to say *code* rather than *build scripts*.
- [ ] **`README`** says the repository holds the source of the document. That framing needs widening,
      or a reader arriving for a typo fix will be surprised by an application.
- [ ] **Decide where teacher conversation logs go — before writing code.** Not in this repository: it
      is public, and the whole point of the whitelist gitignore is that nothing lands here unnoticed.
      Retrofitting this is painful.

---

## Open questions

- [ ] Is the generated `bot/knowledge/` committed, or produced at deploy time? Committing it makes the
      bot's knowledge reviewable in diffs, which is worth a great deal when the bot starts saying
      something wrong. It also doubles the repository's prose in every clone.
- [ ] What does the bot do about the **teacher-facing vs student-facing** line? These materials are
      written for teachers and contain assessment answers. If a student ever reaches the bot, it
      should not hand over the answer key.
- [ ] How does the overlay reference the book? If a misconception note points at a section title and
      the title changes, that link breaks silently. Worth a check in `knowledge.py`, in the same
      spirit as `check-links.py`.

---

## One consequence worth stating plainly

A bot will repeat whatever the chapters say, confidently, to a teacher in the middle of a lesson. That
raises the stakes on the open hardware checks in [TODO.md](TODO.md), and on **1.7** in particular. The
x 1.25 sonar multiplier is currently a sentence in a PDF that a reader might skim past. Once a bot
exists it becomes the direct answer to "why is my robot hitting the wall?", delivered with confidence
and no hedging.

Settle section 1 of TODO.md before the bot goes in front of anyone.

**Observed, once the agent was actually running.** It does not only repeat what the chapters say
— it invents what they leave out, in exactly the places they trail off. Asked why the sound sensor
needs ports 3 or 4, it explained that ports 1 and 2 "are digital and cannot read the analog signal".
No chapter says that; chapter 1 stops at "the only ports with analog inputs" and never characterises
the others. See TODO 1.8, which the answer lands squarely on.

This is the worse half of the problem, because a wrong sentence can be reviewed and a silence
cannot. Grep will not find the gaps, and reading for them means noticing an absence. The practical
consequence is that the open hardware checks are not merely a correctness backlog: every one of
them is a hole the bot will fill on its own, and the filling will sound as confident as the rest.
