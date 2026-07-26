# BmE materials — open items

Everything still outstanding, in one place. Grouped by **what you need in hand**, because most of
these are cheap once you're in the right place and impossible when you're not.

Every chapter of the book has been through a full review. What is left here is what could not be
settled at a desk: checks that need the robot, a Mac, a Chromebook or a camera, and decisions that
are the project's to make rather than a reviewer's. If you are picking this up cold, read this file
and then `git log`; between them they carry the reasoning that the finished text deliberately leaves
out.

Sources folded in: the materials review, the recovered Notion comment threads, the original
`Admin/To do` backlog, and items thrown up by the migration.

*Last updated: 2026-07-25*

Audited against the source on 25–26 July 2026 rather than trusted, first section 4 and then every
other section for work that only looked like it needed hardware. Five entries in section 4 had already
been closed by earlier commits and were still listed as open; those now say so.

Everything that could be settled at a desk has been, and each entry records what was done and what it
turned up. Closed this way: all of section 4 except the items below, plus **5.2** (it was a badge, now
blurred), **5.3**'s licence gap, **6.2** (eight installer screenshots), and the Kinesis half of
**4.6**. One entry in 1.8 was retired as already dealt with — no Google Drive mirrors remain in the
book, the programs are mirrored locally.

**What is genuinely left, and why:**

| | Needs |
|---|---|
| 1.1–1.7, most of 1.8, 1.9, 1.10 | the robot |
| 2.1 | a Mac |
| 3.1 | a Chromebook |
| 5.1 | a camera |
| 4.1, 4.2's Q2, 4.3's "section B", the rest of 4.6, 4.8's backlog, 5.3's redraw choice, 6.1, 6.3 | a decision that is yours |

Two 1.8 items were attempted and could not be settled from the material at hand — the port 1/2 pin
labels and which motor connector is backmost. What was ruled out is written into those entries so the
next person does not repeat the attempt.

---

## 1. Needs a robot

The first item is the big one. Do it before revising any prose, because it may delete a whole
section.

### 1.1 ★ Can you now switch between Live and Upload mode without resetting the firmware?
Your own note said: *"It seems you might now be able to switch back and forth between modi. Check
this."*

If that's true, the firmware-reset procedure is **obsolete** — and with it a good part of the
*Getting started* chapter, plus the caveats scattered through Color Vision. This is the single
highest-leverage check on the list.

- [ ] Reset still required
- [ ] No longer required → rewrite *Getting started* §Resetting the firmware, and remove the
      Color Vision warnings that depend on it

### 1.2 Does the firmware reset work over the Bluetooth dongle, or only USB?
Your note: *"Double check whether the new Bluetooth dongle also allows using Upload mode."*
The chapter currently says **use the USB cable** — the conservative choice. If the dongle works,
relax that sentence.

- [ ] Dongle works   - [ ] USB required

### 1.3 Does "Update Firmware" offer a choice of Factory vs Online firmware?
Makeblock distinguishes the two; Live mode needs **Online**. You confirmed Online is correct — the
open question is whether mBlock ever asks. If it does and a teacher picks Factory, Live mode still
fails and it looks like the reset didn't work.

- [ ] No choice offered   - [ ] Choice offered → say which to pick

### 1.4 What is the connect control called? — largely answered
The screenshots settle most of this, and the chapter now matches them:

| Context | Control | Then |
|---|---|---|
| Browser, direct connection | `Bluetooth` / `Serial` buttons | choose `Serial`; Chrome asks which port |
| Browser, via mLink | a single `Connect` button | |
| Installed mBlock | `Connect` | a dialog with `USB` / `Bluetooth` / `2.4G` tabs; choose `USB` |

- [ ] Confirm this is still what v5.6.0 shows — the screenshots are from v5.4.3.

### 1.5 Which dongle-pairing sequence is right?
- [ ] **A** — switch off other robots → insert dongle → press its Bluetooth symbol
- [ ] **B** — robot **off** → insert dongle → press and *hold* until rapid flash → robot on
- [ ] Both work

### 1.6 Does the mBot need re-adding to mBlock for every new program?
Open one of the supplied `.mblock` files in a fresh session — is the mBot already under Devices?
The old pages contradicted each other.

- [ ] Already present   - [ ] Must re-add every time

### 1.7 Is the sonar under-reporting still there?
The question has changed shape. You checked years ago, across several distances, that the error is
proportional rather than a fixed offset — which is what makes a single multiplier the right fix, and
it is now what the chapter says instead of "an internet search indicated". So the model is settled.

What is not settled is whether the bug is still there. mBlock has been updated many times since, and
if Makeblock has corrected it, our x 1.25 becomes an error of the same size in the opposite
direction: the robot would believe obstacles are 25% further away than they are, and would leave
every turn and every beep too late. A teacher would see a robot that clips things it should have
avoided, with no obvious reason.

Measure at two or three distances — say 50 cm, 1 m and 2 m — against a flat wall, and divide true by
reported each time:

| True | Reported | Ratio |
|---|---|---|
| 50 cm | | |
| 100 cm | | |
| 200 cm | | |

- [ ] Ratio still about **1.25** — nothing to do
- [ ] Ratio now about **1.0** — the bug is fixed; remove the multiplier from both programs and rewrite
      the section, which then becomes a short historical note rather than an instruction
- [ ] Something else — put that number in the programs instead

Where it lives, confirmed by reading the .mblock files rather than the screenshots: four occurrences
in `sonar_obstacle_avoidance`, two in `sonar_cane`, and none in `sonar_directionality`, which is
correct — that program only reports whether an echo came back, and students measure the real distance
on the floor.

While measuring, note the ratio at 50 cm particularly. The programs turn at 30 cm and beep from about
120 cm, but the only calibration point we have ever published is at 184 cm, so the correction has
never been checked over the range where it is actually used.

### 1.8 Smaller confirmations
- [ ] Colour sensor genuinely requires **port 2** (or is that just convention?) — note that the
      `set fill light LED to off` screenshot in *Color Vision* §Taking it further shows the block set
      to **`port1`**, which is at least suggestive. See 4.7.
- [ ] Onboard light sensor really returns **0–1000** (the challenge threshold of 500 depends on it)
- [ ] Sound-sensor sensitivity dial: is "both to the same halfway position" still right, and does it
      interact with the `left_scale` calibration students derive later?
- [ ] Pin labels beside **ports 1 and 2** — one appears to include `A5`. If so, "sound sensors must
      go in ports 3 or 4" is slightly too strict. **Tried and failed to settle this at a desk:** the
      only board photograph available is an 855 px Makeblock product shot, and while ports 3 and 4
      legibly read `SCL SDA GND 5V A0 A1` and `SCL SDA GND 5V A2 A3` — confirming that half — the
      port 1 and 2 strips are printed at half the size and upside down, and `A5` cannot be told from
      `L1` at that resolution. Makeblock's *Beginner's Guide* has no pinout table either. Needs the
      board in your hand and good light.
- [ ] Which motor connector is physically **backmost** — M1 or M2? The product shot confirms M2 sits
      left of M1 with the power switch above them, but no photograph in the repository shows the
      board mounted in the chassis, so "backmost" still cannot be resolved from what we have.
- [ ] **Screenshot drift.** Every mBlock screenshot in the document dates from 2024; the current PC
      release is v5.6.0 (April 2025). Spot-check the Devices panel, the `+` extension button and the
      Connect dialog. This matters more in a PDF than it did on a website — a teacher who printed it
      in September has a wrong picture all year.
- [ ] The mBlock `File` menu wording. The chapter had it both ways — "Save to **your** computer" and
      "Save to **my** computer". I standardised on "my computer", matching "Open from my computer",
      but one of the two spellings was wrong and it is worth reading the menu once.
- [ ] Screenshot versions: the installed-mBlock screenshot shows **v5.4.3** in its title bar, and the
      current release is v5.6.0. Part of the screenshot drift already noted below. The eight installer
      screenshots added for 6.2 are the same vintage — two of them print a version in the window
      chrome, **mBlock 5.4.3** and **mLink2 2.1.1**. Installer dialogs change far less often than the
      editor, so these should age better than the IDE screenshots, but they are on the drift list now
      rather than discovered later.
- [ ] **"Panda window."** Several chapters call the variable-values panel the "panda window". Confirm
      that is still what it looks like and a name teachers recognise, or replace it with a neutral
      description.

### 1.9 Is mLink needed at all in the browser? — mostly answered
Your note asked what the minimum software is for the browser route. The screenshots answer most of
it: the dialog in *Connecting to the robot* is Chrome's own "ide.mblock.cc wants to connect to a
serial port" prompt, which is the browser's Web Serial support talking to the dongle directly. mLink
is not involved. Both chapters now say so, and *Installing mBlock* no longer presents mLink as
mandatory — which matters, because it means a locked-down school computer needs **nothing installed**
to run the browser route in Chrome.

Two gaps left, both needing a robot:

- [ ] Does **firmware update / reset** work over the direct connection, or does that step still need
      mLink or the installed mBlock? This is the one operation that reaches deepest into the board.
- [ ] On a **Chromebook**, is the direct connection available, or is mLink still required there?
      Ties in with 3.1.

If the direct connection covers everything, the mLink material can shrink to a footnote.

### 1.10 Confirm the pairing test
I wrote up the test you described — break the pair from either end and see whether the other partner
starts blinking — as *Checking whether a dongle and a robot are paired*. Worth running once as
written to confirm the timings, particularly the "five to ten seconds" before the dongle reacts.

- [ ] Robot blinks a few seconds after the dongle is unplugged
- [ ] Dongle blinks five to ten seconds after the robot is switched off

---

## 2. Needs a Mac

### 2.1 The Mac instructions have never been tested
Recovered from a 2023 comment thread: *"These instructions were collated based on the makeblock
website and apple help website. They have not been tested."* Two further comments doubt whether the
mLink window appears on Mac at all, and one is still unresolved.

This carries into the new *Installing mBlock* chapter, whose Mac section descends from that
material. It is the **only platform where we have no evidence the instructions work**.

- [ ] Apple Silicon build installs and runs
- [ ] Installer blocked by Gatekeeper? does right-click → Open work?
- [ ] App blocked on first launch? does Control-click → Open work?
- [ ] Does mLink show a "running" window on Mac, as on Windows?
- [ ] Does the dongle connect from a Mac?

---

## 3. Needs a Chromebook

### 3.1 Is the Chromebook install path still alive?
The old page used "Add to Chrome" → **"Add App"** — the deprecated Chrome *App* flow — and Makeblock
now lists the Chrome version as merged into the web version. If this path is dead, Chromebook
schools have **no working route at all**.

The new chapter describes it vaguely enough to be true either way, but it needs replacing with what
actually happens.

- [ ] Walk the current path and record the steps

---

## 4. Needs only your judgement

These need no hardware. They're the editorial calls I deliberately did not make for you.

### 4.1 Read the PDF
Chapter ordering is **my guess, not your judgement**. In particular: I put *Introduction to
Programming* and *Programming the robot* before the three sensor lessons, and *Educational
standards* as a reference chapter at the back rather than distributed per lesson.

### 4.2 Sound Localization — the assessment answer to Q2 doesn't match the question
Question 2 asks whether ear *placement angle* affects localisation. The answer supplied instead
discusses **left/right microphone sensitivity mismatch** — a different question, already covered in
the phonotaxis section. Writing the right answer needs your data on what ear angle actually does, so
it is left for you.

Q1 is dealt with: it cited "the graph" with no graph nearby, and now points at the two directionality
measurements by figure number (the without-ears and with-ears plots, which gained ids for the
purpose). Both resolve in the PDF.

While in there: the **assessment sits before the activities that generate its data** — Assessment
Questions is §Assessment Questions, and the graphs it now cites are ~150 lines later under *Robot
phonotaxis*. The cross-references carry page numbers so it works on paper, but you may prefer to move
the assessment after the activities. That is an ordering call, so it belongs with 4.1.

### 4.3 Kinesis and Taxis — one problem left of the four
Your own backlog already says *"Revise Kinesis/Taxis lesson plan"*. Three of the four are fixed;
the remaining one is genuinely yours.

**Still open:**

- [ ] Assessment Q2 refers to *"the protocol in section B"* — **there is no section B, and never
      was.** I extracted both handouts: `Rules for Kinesis.docx` and `Rules for Taxis.docx` are
      organised as "Condition 1 / 2 / 3", with no lettered sections anywhere. Q2 asks whether the
      protocol describes klinokinesis or klinotaxis, and the only protocol where that is a real
      question is Taxis Condition 1 — but that handout is *titled* "Condition 1. Klinotaxis", so
      simply repointing the question hands students the answer. That makes it a pedagogical choice,
      not a reference repair: either rename the handout condition, or reword the question to describe
      the protocol rather than cite it.

**Fixed:**

- Q1's *"these four mechanisms"* — the four are unambiguous once you read the handouts (kinesis
  without sensors, orthokinesis, klinotaxis, tropotaxis: six conditions, four mechanisms). Both the
  chapter introduction and Q1 itself now name them.
- The introduction promised **three** activities and **three** hypotheses; the chapter delivers **two
  activities of three conditions each**, and four hypotheses (one, plus A/B/C). The introduction now
  describes what is actually there, and names the mechanism each condition demonstrates.
- The definitions callout conflated klinokinesis and orthokinesis. It now gives both halves of the
  definition their names and says which one the activities use. (It also had a grammar slip —
  "depending on" for "depends on" — and an inverted "but" where "and" was meant.)

### 4.4 Color Vision — "three steps" — fixed
There really are three steps; the paragraph introducing them described the second and third as the
same thing. It now matches the three headings that follow it (Inspecting the sensor values,
Interpreting the data, Programming the robot).

### 4.5 Sound Localization — "Sound localization cues" — already done
This entry was stale. The section now names all three cues (interaural time difference, interaural
level difference, and the outer ear's spectral colouring) before linking the *Physics Today* survey,
and the Motivation exercise below it turns the horizontal/vertical distinction into a demonstration.
Nothing to do.

### 4.6 The materials database — Kinesis done, two items left
| Lesson | Items |
|---|---|
| Sonar | 16 |
| Color Vision | 12 |
| Sound Localization | 11 |
| Programming the robot | 7 |
| **Taxis/Kinesis** | **5** (was 1) |
| **Intro Programming** | **1** |

*"Add Taxis/Kinesis Materials"* is done, in the chapter rather than the CSV, since the chapter is the
source of truth now. The table was derivable without asking you: I extracted both rules handouts and
the grids file, so the list is what the activities actually consume rather than a guess — spinners,
the four printed grids (Grid 4 carries the narrow and wide markings the tropotaxis conditions need),
the two rules handouts, a large and a wide arrow cut-out, and the data sheets.

**Still open, because these need you:**

- [ ] *"Add model magic to materials"* — which lesson, and how much per group?
- [ ] *"Create material list to make external pinnae"* — Sound Localization says "cardboard paper,
      pipe cleaners, tape, etc." in prose. Turning "etc." into a table is a purchasing decision.
- [ ] **Intro Programming still lists one item.** The cheese-sandwich game needs the two Avery label
      sheets that are already linked from the chapter, and presumably actual materials to build a
      sandwich from. Not obvious from the source what you hand out.

**One naming conflict found while doing this, which is a decision rather than a defect:**

- [ ] The chapter calls the manipulative the **Blue Arrow** and measures in *arrow lengths*; both
      rules handouts call the same object the **Blue Bug** and measure in *bug-lengths*. The figure
      shows an arrow, so neither name is wrong about the artwork, but a group holding the handout and
      a teacher reading the chapter are using two words for one thing. The materials table now
      mentions both so nobody is stuck, which is a bridge rather than a fix. Standardising means
      either editing the chapter or regenerating the two `.docx` handouts, and only you know whether
      those handouts are already printed and in a cupboard.

### 4.7 Image captions — done
Started at 111, and this entry still said 61. The real figure is now **zero**: every image in every
chapter carries a caption. Sonar and Sound Localization did come out in the wash of their reviews, as
predicted.

The last one was the `set fill light LED to off` block in *Color Vision* §Taking it further. Writing
its caption turned up something worth keeping: **the block in that screenshot reads `port1`**, while
the chapter tells teachers throughout to use **port 2**. The caption now says so explicitly and tells
the reader to set the dropdown to whichever port the sensor is on, so nobody copies the screenshot
blindly — but it is also a data point for **1.8**, where "does the colour sensor genuinely require
port 2, or is that just convention?" is still open. If port 1 works, that screenshot is evidence, and
the answer changes several sentences in the chapter.

### 4.9 Link text — done, and it was bigger than three
Every link in the book now has descriptive text. The house convention is `Description (.ext)`, set by
"Video: the robot following the path (.mp4)".

`pip_exported.mp3` was already fixed. `Echolocation_in_Insectivores_and_Rodents.pdf` is now
"Echolocation in insectivores and rodents (.pdf)". Checking properly turned up **six more of the same
defect** in Kinesis and Taxis, which the original count missed because those filenames contain spaces
— `Rules for Kinesis.docx`, `Kinesis-Taxis grids.pptx` and the rest. All seven now follow the
convention.

Separately, **14 links had a bare URL as their link text** — unreadable in print, where the reader
cannot click. Those are now titled, using the actual titles fetched from each target rather than
invented ones: three sonar clips (BBC Earth sperm whales, a bat taking moths, a Toyota parking
sensor), four kinesis/taxis teaching videos, the PhET colour-vision simulation, and the six
student-data clips.

Two things fell out of that:

- The six student-data clips are named `kinesis1-3` and `taxis1-3` at the source but were **listed
  taxis-first**, the reverse of the activity order in the chapter. They are now a labelled list in
  kinesis-then-taxis order. If those six do correspond to the three *conditions* of each activity,
  the labels could say so — I did not assume it.
- Sonar's introduction promised **four** short video clips and listed **three**; the sentence then
  goes on to describe exactly three (whales, bats, parking sensor). Corrected to three.

- [ ] `files/burst_short.wav` is **tracked but linked from nowhere** — a 0.5 second mono 44.1 kHz
      burst, presumably meant as a stimulus alongside `pip_exported.mp3`. Either it lost its
      reference somewhere in the migration, or it was superseded by the .mp3. Your call: link it
      where it belongs, or delete it. I left it alone rather than guess.

### 4.8 Loose ends in the prose

**Still open — these need you, not a desk:**

- [ ] *Programming the robot*: your backlog says *"Create programs under 'Programming the robot'"* —
      it is the only lesson with no `.mblock` programs
- [ ] Backlog: *"Create Master slide deck"*, *"Use the slides below to illustrate the working
      principle of sonar"*, *"Update robot color vision activity?"*
- [ ] Minor, and only if it bothers you: *Introduction to Programming* uses "Challenge 1" and
      "Challenge 2" for the two conceptual halves of programming (working out the algorithm, then
      expressing it), while *Programming the robot* now uses "Challenge 1–4" for the four exercises.
      Self-consistent within each chapter, but the same word carries two meanings across a page turn.

**Fixed:**

- *Programming the robot*: challenges 2, 3 and 4 were unnumbered headings while the intro promised
  four. All four now numbered, and their headings brought to consistent sentence case. Nothing linked
  to the old anchors, so no cross-references broke.
- *Sound Localization*: four literal tab characters — three in the essential questions, one in
  learning objective 4 — replaced with spaces. No chapter contains a tab any more.
- *Color Vision*: a caption was repeated verbatim as body text directly beneath its own image, so the
  same sentence appeared twice in a row. The duplicate is gone.

Two entries here were already stale and are struck: the *Sonar cane* "here is not a link" sentence no
longer exists in the chapter, and the escaped-backtick leak is gone — that passage now reads
`abs(difference) > 2` cleanly.

---

## 5. Needs a camera

### 5.1 Replace the web-sourced product photographs
Three, not the five I listed before. I have now looked at all of them instead of guessing from
captions, and two of my earlier candidates are plainly your own photographs — the desk, the robot
labelled `vanderdt04`, the hand-drawn red arrows. Sorry for the noise.

The three that are studio product shots on pure white backgrounds, and are not yours:

| File | Shows | Chapter |
|---|---|---|
| `getting-started-draft-6fb3632a.png` | the Bluetooth dongle | Getting started |
| `getting-started-draft-dd60485a.png` | the USB cable | Getting started |
| `introduction-to-the-robot-676c1e4d.png` | the RJ25 sensor cable | Introduction to the robot |

Worth reshooting regardless of the licensing question: your own photos would show the **actual kit
teachers receive**, with the coloured port stickers the text keeps referring to.

On git history: these were already served publicly from the Notion site, so pushing does not expose
them for the first time — it makes them permanent. While you are the only person with a clone,
rewriting history to drop them is easy. It stops being easy once anyone else clones the repo.

### 5.2 The rectangle at the student's hip — it was a badge, and it is blurred
Enlarged ten times, it is unmistakably an **ID badge in a plastic holder on a lanyard clip**: white
card, a pink header band, three lines of printed text, clipped to the waistband. Not a phone and not a
sheet of paper.

Blurred as you instructed, by pixelating a 24 × 48 px region past any possibility of recovery rather
than softening it, so nothing can be reconstructed from the file. At page scale it reads as a small
soft patch, consistent with the black face masks already used throughout. The original is one
`git revert` away if you dislike it.

### 5.3 The mCore board diagram is Makeblock's — carve-out widened
`introduction-to-the-robot-51abd850.png` — the labelled main-board diagram — is a Makeblock
illustration, so it belongs with the web-sourced images above rather than with your own photographs.
It carries "Diagram by Makeblock." in its caption, which is the honest minimum.

The licence carve-out said "Photographs of Makeblock hardware not taken by the project", which as
written did not reach a line drawing at all — a diagram is not a photograph, so the one item most
needing the carve-out fell outside it. It now reads "Photographs **and diagrams** of Makeblock
hardware not **made** by the project" and names the board drawing explicitly.

- [ ] That closes the licensing gap but not the underlying choice: keep the diagram with its credit,
      or redraw it so the book owns the artwork outright. Reshooting is not an option, it being a line
      drawing rather than a photo.

---

## 6. Mechanical

### 6.1 Getting a new edition onto the website
Not a GitHub job — you've ruled that out, and rightly: teachers didn't use Notion and won't use
GitHub either. So the only route to a teacher is biologymeetsengineering.org, which makes uploading
the build the step that actually publishes anything. Worth being deliberate about it:

```sh
cd book && ./build.sh          # render/BmE-teacher-materials.pdf + .html
```

- [ ] Upload both files to the website
- [ ] Use a URL that stays the same between editions, so the link in the colophon and any link a
      teacher has bookmarked keeps working
- [ ] Tag the commit you built from (`git tag 2026-07 && git push --tags`). The footer fingerprint
      is `git describe --tags`, so tagging turns a bare hash into something you can ask a teacher to
      read back to you over email

The last one is worth the ten seconds. When someone reports a problem, the first question is which
version they have, and it is printed at the foot of every page.

### 6.2 Screenshots for *Installing mBlock* — done, eight of them
The chapter was text-and-links only; it now illustrates every step that has a dialog. All eight came
from `bme-notion-export/` and every one was opened and checked before it was captioned, which turned
up four things worth recording:

- **Two of them existed in both exports at different versions.** The retired `Admin` page had mBlock
  **5.4.0**; the newer `Quick Start Guide` page had **5.4.3**, which matches the rest of the book.
  Used the 5.4.3 pair.
- **There is no `Driver Install Failure` screenshot**, contrary to what this entry used to claim. That
  failure appears in the same `DriverSetup` window as the success case, and that window does carry the
  `UNINSTALL` button the step-4 advice tells teachers to press, so the caption points at it there.
- **The driver confirmation really does say "The drive is successfully Pre-installed in advance!"** —
  Makeblock's own wording, "drive" and all. Captioned verbatim, and flagged as the message you want,
  because it reads like an error when it is not.
- **The mLink window is a launcher, not a status box.** It has cards and a `Create now` button that
  opens the same editor as Step 3. The chapter described it as "a small window confirming it is
  running"; that is now corrected, and the caption notes the shortcut.

Their vintage is on the drift list in 1.8 rather than left to be discovered later.

### 6.3 A Live/Upload screenshot to delete — gated on 1.1
*Getting started* line 189 still carries an image captioned *"Use the slider to switch the software
to `Live` mode"*, which contradicts the text now saying no mode toggle is needed. Delete once 1.1
and 1.3 are settled. One line of markdown now, rather than a Notion UI job.

## Done

- **Sections 5 and 6 swept too, and one 1.8 entry retired.** *Installing mBlock* gained the eight
  installer screenshots it was missing (6.2), the badge on the student's hip turned out to be a badge
  and is blurred (5.2), the licence carve-out was widened to cover diagrams and not just photographs,
  which is what the mCore drawing needed (5.3), and the Kinesis materials table went from one item to
  five, derived from the rules handouts and the grids file rather than guessed (4.6). The Google Drive
  mirror check in 1.8 was retired: no Google Drive links remain anywhere in the book.
- **Section 4 swept for everything a desk can settle.** Nine defect classes fixed across five
  chapters: literal tabs, unnumbered challenges, seven file links off the naming convention, 14 bare
  URLs as link text, the Color Vision "three steps" paragraph, a caption duplicated as body text, the
  last uncaptioned image, the Kinesis activity and hypothesis counts, and the klinokinesis /
  orthokinesis conflation. Q1 of the Sound Localization assessment now cites its graphs by figure
  number instead of saying "the graph". Verified by rebuilding: no broken links, no unresolved
  references, zero overfull boxes, and no revision notes leaked.
- **The open-items list is in the repository.** It was excluded at first on the grounds that it held
  frank criticism and private notes. Re-reading it before publishing, it holds neither — it is a
  project to-do list, which is a normal and useful thing for a public repository to carry, and it is
  the closest thing this project has to a handoff document.
- **Directivity claim settled.** Each ear is most sensitive towards its own side, so straight ahead
  is necessarily below that maximum — the passage was right and my doubt was not. Rewritten so the
  claim rests on that fact rather than on reading it off a cut-away sphere, which is the part that
  genuinely was hard to see.
- **Blinking-LED solution corrected.** `shows color ... for N secs` holds the program while it runs,
  so the old solution ran one second red and three seconds dark against a challenge asking for one
  and one. New two-block version, and the blocking behaviour is now stated where the LED and motor
  blocks are introduced, since the same distinction drives the advice about slower robots.
- **mBlock interface screenshot replaced** with one taken after the mBot was added. The previous one
  was the fresh-start state, which is why it showed Codey's block categories.
- **Pushed, and the file links work.** All 20 handout, media and program links resolve from the
  built PDF, along with the repository pointer in the colophon. That closes 6.1 and 6.6.

- ~40 typo and factual fixes applied in Notion before migrating (`m/ms`→`cm/ms`, `2000 kHz`→`2000 Hz`,
  the PI email, the method-4 cross-reference, Hypothesis C wording, and the rest)
- The dead firmware page: five inbound links found and repointed
- Terminology standardised on **mBot / mBlock / Makeblock / phonotaxis** — 31 instances, including
  the two image captions that were unreachable in Notion
- Port table added to *Introduction to the robot*, with the analog-pin reason
- Sonar range corrected to Makeblock's real 3–400 cm
- Deep link to Makeblock's assembly instructions instead of duplicating them
- 2.4 GHz and direct-Bluetooth connection methods retired
- Migration to markdown: 14 chapters, 172-page PDF, self-contained HTML
- All ten mBlock program links paired with Google Drive mirrors
- Comment threads recovered before they were lost to the export
- Repo initialised, licensed CC BY-NC 4.0 + MIT, committed locally
