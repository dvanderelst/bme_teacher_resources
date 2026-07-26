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
- [ ] Colour sensor genuinely requires **port 2** (or is that just convention?)
- [ ] Onboard light sensor really returns **0–1000** (the challenge threshold of 500 depends on it)
- [ ] Sound-sensor sensitivity dial: is "both to the same halfway position" still right, and does it
      interact with the `left_scale` calibration students derive later?
- [ ] Pin labels beside **ports 1 and 2** — one appears to include `A5`. If so, "sound sensors must
      go in ports 3 or 4" is slightly too strict. (Ports 3 and 4 carry `A0`–`A3`; that much is
      confirmed from your board photo.)
- [ ] Which motor connector is physically **backmost** — M1 or M2? Your board photo shows M2 left of
      M1, but "backmost" depends on chassis orientation. Would make the wrong-direction
      troubleshooting much faster to follow.
- [ ] Do the 2024 Google Drive program mirrors still match the current `planet.mblock.cc` versions?
      The mirrors date from Sept–Dec 2024.
- [ ] **Screenshot drift.** Every mBlock screenshot in the document dates from 2024; the current PC
      release is v5.6.0 (April 2025). Spot-check the Devices panel, the `+` extension button and the
      Connect dialog. This matters more in a PDF than it did on a website — a teacher who printed it
      in September has a wrong picture all year.
- [ ] The mBlock `File` menu wording. The chapter had it both ways — "Save to **your** computer" and
      "Save to **my** computer". I standardised on "my computer", matching "Open from my computer",
      but one of the two spellings was wrong and it is worth reading the menu once.
- [ ] Screenshot versions: the installed-mBlock screenshot shows **v5.4.3** in its title bar, and the
      current release is v5.6.0. Part of the screenshot drift already noted below.
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

### 4.2 Sound Localization — the assessment answers don't match the questions
Question 2 asks whether ear *placement angle* affects localisation. The answer supplied instead
discusses **left/right microphone sensitivity mismatch** — a different question, already covered in
the phonotaxis section. And Q1's answer cites "the graph" and "the previous graph", which are not in
that part of the chapter.

### 4.3 Kinesis and Taxis — a cluster of problems
Your own backlog already says *"Revise Kinesis/Taxis lesson plan"*. Specifically:

- Assessment Q2 refers to *"the protocol in section B"* — there is no section B
- Q1 asks about *"these four mechanisms"*, never enumerated as four
- The introduction promises **three** activities; the chapter delivers **two**
- The definitions callout defines kinesis by *tumble frequency* — that's klinokinesis — and then the
  activity correctly introduces orthokinesis. The two are conflated.

### 4.4 Color Vision — "three steps" that are two
*"we will proceed in three steps"* — steps 2 and 3 restate the same thing, and the actual Step 2
heading is "Interpreting the data".

### 4.5 Sound Localization — "Sound localization cues" is still just a link
A 2024 comment said *"Expand this with theory"* and was marked resolved, but the section is a bare
bookmark with no prose. The assessment questions depend on this theory.

### 4.6 The materials database is unmaintained for two lessons
| Lesson | Items |
|---|---|
| Sonar | 16 |
| Color Vision | 12 |
| Sound Localization | 11 |
| Programming the robot | 7 |
| **Intro Programming** | **1** |
| **Taxis/Kinesis** | **1** |

Your backlog has *"Add Taxis/Kinesis Materials"*, *"Add model magic to materials"* and *"Create
material list to make external pinnae"*. The Kinesis chapter's table currently lists one item
(Spinners) though the lesson also needs printed grids, the rules handouts and paper. Fixing the
source CSV or the chapter directly both work — the chapter is now the source of truth.

### 4.7 61 images still have no caption
Your note asked whether the empty `![]()` was a markdown fault. It isn't — those images simply never
had a caption in Notion, or had junk like `Screenshot 2024-10-28.png` that I stripped during the
migration. You spotted the visible symptom yourself: an uncaptioned image is not a figure, so it gets
neither centring nor a number, and nothing in the text can refer to it.

Started at 111. Done: *Introduction to the robot*, *Getting started*, *Programming the robot* and
*Color Vision*. Remaining, worst first:

| Chapter | Uncaptioned |
|---|---|
| Sound Localization | 30 |
| Sonar | 26 |
| Kinesis and Taxis | 5 |

Sonar and Sound Localization are the two chapters still to review, so they will come out in the wash.
Kinesis and Taxis you are overhauling anyway.

### 4.9 Three handouts are linked by raw filename
Now that handout links actually work, the link text matters. `output.mp4` is dealt with — it now
reads "Video: the robot following the path (.mp4)", and the file is renamed to match. Three left, all
in chapters still to review:

| Link text | Chapter |
|---|---|
| `pip_exported.mp3` | Sound Localization |
| `burst_short.wav` | Sound Localization |
| `Echolocation_in_Insectivores_and_Rodents.pdf` | Sonar |

### 4.8 Loose ends in the prose
- [ ] *Sonar cane*: "The student guide for this part can be found **here**" — "here" is not a link
- [ ] *Programming the robot*: only the first of four challenges is numbered, though the intro
      promises "four challenges"
- [ ] *Programming the robot*: escaped-backtick leak — `` \`difference is\> 0\` `` renders broken
- [ ] *Sound Localization*: literal tab characters in the essential questions, rendering as odd gaps
- [ ] *Programming the robot*: your backlog says *"Create programs under 'Programming the robot'"* —
      it is the only lesson with no `.mblock` programs
- [ ] Backlog: *"Create Master slide deck"*, *"Use the slides below to illustrate the working
      principle of sonar"*, *"Update robot color vision activity?"*

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

### 5.2 One image to glance at
In the pinnae photo (`testing-artificial-pinnae-e2beccd3.jpg`) the seated student has a small
light-coloured rectangle at their hip. Could be a phone, a sheet of paper, or a name badge. If it's
a badge, spot-blur it. Faces are already masked throughout — that part is done.

### 5.3 The mCore board diagram is Makeblock's, not ours
`introduction-to-the-robot-51abd850.png` — the labelled main-board diagram — is a Makeblock
illustration, so it belongs with the web-sourced images above rather than with your own photographs.
It now carries "Diagram by Makeblock." in its caption, which is the honest minimum. Reshooting is not
really an option here (it's a line drawing, not a photo), so the choices are to keep it with the
credit, or redraw it. The licence carve-out in *About these materials* covers "photographs of
Makeblock hardware" — if this diagram stays, widen that wording to cover diagrams too.

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

### 6.2 Screenshots for *Installing mBlock*
The new chapter is text-and-links only. Worth bringing across the installer screenshots from the
retired platform pages (they're still in `bme-notion-export/`): the mBlock installer, `Finish`,
"installed", the mLink installer, the `Driver Install Failure` dialog, the firewall prompt.

### 6.3 A Live/Upload screenshot to delete — gated on 1.1
*Getting started* line 189 still carries an image captioned *"Use the slider to switch the software
to `Live` mode"*, which contradicts the text now saying no mode toggle is needed. Delete once 1.1
and 1.3 are settled. One line of markdown now, rather than a Notion UI job.

## Done

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
