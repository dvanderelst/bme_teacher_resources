# BmE materials — open items

Everything still outstanding, in one place. Grouped by **what you need in hand**, because most of
these are cheap once you're in the right place and impossible when you're not.

Every chapter of the book has been through a full review, and everything that could be settled at a
desk has been. What is left is what could not: checks that need the robot, a Mac, a Chromebook or a
camera, and decisions that are the project's to make rather than a reviewer's. If you are picking this
up cold, read this file and then `git log`; between them they carry the reasoning that the finished
text deliberately leaves out.

Closed items are deleted rather than struck through, so gaps in the numbering (4.4, 4.5, 4.7, 4.9,
5.2, 6.2) are items that are done. `git log` says what happened to each.

*Last updated: 2026-07-26*

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
- [ ] Colour sensor genuinely requires **port 2** (or is that just convention?) The `set fill light
      LED to off` screenshot in *Color Vision* §Taking it further shows the block set to **`port1`**,
      which is at least suggestive. If port 1 works, several sentences in that chapter change.
- [ ] Onboard light sensor really returns **0–1000** (the challenge threshold of 500 depends on it)
- [ ] Sound-sensor sensitivity dial: is "both to the same halfway position" still right, and does it
      interact with the `left_scale` calibration students derive later?
- [ ] Pin labels beside **ports 1 and 2** — one appears to include `A5`. If so, "sound sensors must
      go in ports 3 or 4" is slightly too strict. Ports 3 and 4 carry `A0`–`A3`, confirmed by reading
      the board photograph. Ports 1 and 2 cannot be read from it — their labels are half the size,
      upside down, and `A5` is indistinguishable from `L1` at 855 px. Makeblock's *Beginner's Guide*
      has no pinout table either, so this needs the board in your hand.
- [ ] Which motor connector is physically **backmost** — M1 or M2? The board photograph shows M2 left
      of M1 with the power switch above them, but no photograph we have shows the board mounted in the
      chassis, which is what "backmost" depends on. Would make the wrong-direction troubleshooting
      much faster to follow.
- [ ] **Screenshot drift.** Every mBlock screenshot in the document dates from 2024; the current PC
      release is v5.6.0 (April 2025). Three of them print a version on screen: the installed-mBlock
      screenshot shows **v5.4.3**, and two of the installer screenshots show **mBlock 5.4.3** and
      **mLink2 2.1.1**. Spot-check the Devices panel, the `+` extension button and the Connect dialog.
      Installer dialogs should age better than the editor. This matters more in a PDF than it did on a
      website — a teacher who printed it in September has a wrong picture all year.
- [ ] The mBlock `File` menu wording. The chapter had it both ways — "Save to **your** computer" and
      "Save to **my** computer". I standardised on "my computer", matching "Open from my computer",
      but one of the two spellings was wrong and it is worth reading the menu once.
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

- [ ] Also in scope: in *Sound Localization* the assessment sits **before** the activities that
      generate the data it asks about, roughly 150 lines earlier. The cross-references carry page
      numbers so it works on paper, but you may prefer to move the assessment after the activities.

### 4.2 Sound Localization — the Q2 answer doesn't match the question
Question 2 asks whether ear *placement angle* affects localisation. The answer supplied instead
discusses **left/right microphone sensitivity mismatch** — a different question, already covered in
the phonotaxis section.

- [ ] Write the answer that addresses placement angle. This needs your data on what ear angle
      actually does, which is why it is here rather than done.

### 4.3 Kinesis and Taxis — Assessment Q2 cites a section that does not exist
- [ ] Q2 refers to *"the protocol in section B"*. There is no section B and never was: both handouts
      are organised as "Condition 1 / 2 / 3", with no lettered sections anywhere. Q2 asks whether the
      protocol describes klinokinesis or klinotaxis, and the only protocol where that is a real
      question is Taxis Condition 1 — but that handout is *titled* "Condition 1. Klinotaxis", so
      simply repointing the question hands students the answer. That makes it a pedagogical choice
      rather than a reference repair: either rename the handout condition, or reword the question to
      describe the protocol instead of citing it.

### 4.6 The materials database is still thin for one lesson
| Lesson | Items |
|---|---|
| Sonar | 16 |
| Color Vision | 12 |
| Sound Localization | 11 |
| Programming the robot | 7 |
| Taxis/Kinesis | 5 |
| **Intro Programming** | **1** |

- [ ] *"Add model magic to materials"* — which lesson, and how much per group?
- [ ] *"Create material list to make external pinnae"* — Sound Localization says "cardboard paper,
      pipe cleaners, tape, etc." in prose. Turning "etc." into a table is a purchasing decision.
- [ ] **Intro Programming still lists one item.** The cheese-sandwich game needs the two Avery label
      sheets already linked from the chapter, and presumably materials to build a sandwich from. Not
      obvious from the source what you hand out.
- [ ] The chapter calls the manipulative the **Blue Arrow** and measures in *arrow lengths*; both
      rules handouts call the same object the **Blue Bug** and measure in *bug-lengths*. The figure
      shows an arrow, so neither name is wrong about the artwork, but a group holding the handout and
      a teacher reading the chapter are using two words for one thing. The materials table mentions
      both, which is a bridge rather than a fix. Standardising means editing the chapter or
      regenerating the two `.docx` handouts, and only you know whether those are already printed.

### 4.8 Loose ends in the prose
- [ ] *Programming the robot*: your backlog says *"Create programs under 'Programming the robot'"* —
      it is the only lesson with no `.mblock` programs
- [ ] Backlog: *"Create Master slide deck"*, *"Use the slides below to illustrate the working
      principle of sonar"*, *"Update robot color vision activity?"*
- [ ] `files/burst_short.wav` is tracked but linked from nowhere — a 0.5 second mono 44.1 kHz burst,
      presumably meant as a stimulus alongside `pip_exported.mp3`. Either it lost its reference in the
      migration or it was superseded by the .mp3. Link it where it belongs, or delete it.
- [ ] Minor, and only if it bothers you: *Introduction to Programming* uses "Challenge 1" and
      "Challenge 2" for the two conceptual halves of programming (working out the algorithm, then
      expressing it), while *Programming the robot* uses "Challenge 1–4" for the four exercises.
      Self-consistent within each chapter, but the same word carries two meanings across a page turn.

---

## 5. Needs a camera

### 5.1 Replace the web-sourced product photographs
Three, not the five I listed before. I have now looked at all of them instead of guessing from
captions, and two of my earlier candidates are plainly your own photographs — the desk, the robot
labelled `vanderdt04`, the hand-drawn red arrows.

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

### 5.3 The mCore board diagram is Makeblock's, not ours
`introduction-to-the-robot-51abd850.png` — the labelled main-board diagram — is a Makeblock
illustration. It carries "Diagram by Makeblock." in its caption, and the licence carve-out now covers
diagrams as well as photographs, so the licensing is straight.

- [ ] The underlying choice is still open: keep the diagram with its credit, or redraw it so the book
      owns the artwork outright. Reshooting is not an option, it being a line drawing rather than a
      photo.

---

## 6. Mechanical

### 6.1 Getting a new edition onto the website
Not a GitHub job — you've ruled that out, and rightly: teachers didn't use Notion and won't use
GitHub either. So the only route to a teacher is biologymeetsengineering.org, which makes uploading
the build the step that actually publishes anything. Worth being deliberate about it, and note the
order — the fingerprint is baked in at build time, so tagging after building stamps the bare hash:

```sh
git tag -a 2026-07 -m "Edition of July 2026"   # 1. tag first
cd book && ./build.sh                          # 2. footer picks the tag up
                                               # 3. upload render/*.pdf and *.html
git push origin main && git push origin 2026-07
```

- [ ] Upload both files to the website
- [ ] Use a URL that stays the same between editions, so the link in the colophon and any link a
      teacher has bookmarked keeps working
- [ ] Tag the commit you built from. The footer fingerprint is `git describe --tags --always`, so
      tagging turns a bare hash into something you can ask a teacher to read back to you over email

The last one is worth the ten seconds. When someone reports a problem, the first question is which
version they have, and it is printed at the foot of every page.

### 6.3 A Live/Upload screenshot to delete — gated on 1.1
*Getting started* line 189 still carries an image captioned *"Use the slider to switch the software
to `Live` mode"*, which contradicts the text now saying no mode toggle is needed. Delete once 1.1
and 1.3 are settled. One line of markdown.
