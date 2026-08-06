# BmE materials — open items

Everything still outstanding, in one place. Grouped by **what you need in hand**, because most of
these are cheap once you're in the right place and impossible when you're not.

Every chapter of the book has been through a full review, and everything that could be settled at a
desk has been. The 6 August 2026 test session settled almost everything that needed a robot; its
notes are in `TestAugust06.md` and its evidence in `documentation_resources/`. What is listed below
is what that session did not reach: a Mac, a Chromebook, two sensor readings nobody looked at, three
menus nobody opened, and the editorial calls that are the project's to make rather than a reviewer's.
The photography is done — every photograph of the kit in the book is now our own.

Items are deleted when they close, and the numbering was reset on 2026-08-06 after the August tests
closed most of the list, so numbers here do not match numbers in older commit messages. `git log`
says what happened to each.

*Last updated: 2026-08-06*

---

## 1. Needs mBlock, but not a robot

Half an hour with mBlock open and the mBot added to the `Devices` panel, which does not require the
robot to be plugged in.

### 1.1 Three dropdowns the *Block reference* describes but does not enumerate
Everything else in that chapter was confirmed against mBlock; these three were not, so the chapter
says "the chosen side" and "the dropdown selects which" rather than listing the options. Open each
one and the chapter can be made complete.

- [ ] `stop [all ▾]` (Control)
- [ ] `line follower sensor ... detects [leftside ▾] being [black ▾]` (Sensing)
- [ ] `IR remote [A ▾] pressed?` (Sensing)

---

## 2. Needs a robot

### 2.1 Does the onboard light sensor really return 0–1000?
The challenge threshold of 500 depends on it, and the *Block reference* states the range as "roughly
0–1000" on the strength of documentation rather than measurement.

- [ ] Read it in a bright room and under a covering hand, and note both ends

### 2.2 A sonar photograph in which the `T` and `R` can be read
The letters are on the board — that much is settled — but the photograph now in *Sonar*
(`sonar-sensor-photo.jpg`) is too dark around the transducers for them to be made out, and the caption
therefore has to assert what the picture cannot show.

- [ ] Reshoot with more light on that part of the board. **In hand as of 6 August 2026.**

---

## 3. Needs a Mac

### 3.1 The Mac instructions have never been tested
Recovered from a 2023 comment thread: *"These instructions were collated based on the makeblock
website and apple help website. They have not been tested."* Two further comments doubt whether the
mLink window appears on Mac at all, and one is still unresolved.

This carries into the *Installing mBlock* chapter, whose Mac section descends from that material. It
is now the **only platform where we have no evidence the instructions work** — Windows and Linux were
both walked end to end in August 2026.

- [ ] Apple Silicon build installs and runs
- [ ] Installer blocked by Gatekeeper? does right-click → Open work?
- [ ] App blocked on first launch? does Control-click → Open work?
- [ ] Does mLink show a "running" window on Mac, as on Windows?
- [ ] Does the dongle connect from a Mac?

Worth knowing before you start: on Windows the mBlock installer no longer installs the serial driver
and mLink's installer still does. If the same is true on Mac, a Mac with only mBlock installed may
not see the robot at all, and the fix is to install mLink for its driver.

---

## 4. Needs a Chromebook

### 4.1 Is the Chromebook route still alive, and does it need mLink?
Two questions that are really one. The old page used "Add to Chrome" → **"Add App"** — the deprecated
Chrome *App* flow — and Makeblock now lists the Chrome version as merged into the web version. If
that path is dead, Chromebook schools have no working route unless direct connection covers them, as
it does on Windows and Linux. The download page still lists a Chromebook build of mLink, so Makeblock
evidently thinks it is needed.

The chapter describes the install vaguely enough to be true either way, but it needs replacing with
what actually happens.

- [ ] Walk the current path and record the steps
- [ ] Is direct connection available in the Chromebook's Chrome? If so, the Chromebook section
      shrinks to a sentence and the mLink material can go

---

## 5. Needs only your judgement

These need no hardware. They're the editorial calls I deliberately did not make for you.

### 5.1 Read the PDF
Chapter ordering is **my guess, not your judgement**. In particular: I put *Introduction to
Programming* and *Programming the robot* before the three sensor lessons, and *Educational
standards* as a reference chapter at the back rather than distributed per lesson.

- [ ] Also in scope: in *Sound Localization* the assessment sits **before** the activities that
      generate the data it asks about, roughly 150 lines earlier. The cross-references carry page
      numbers so it works on paper, but you may prefer to move the assessment after the activities.

### 5.2 Sound Localization — the Q2 answer doesn't match the question
Question 2 asks whether ear *placement angle* affects localisation. The answer supplied instead
discusses **left/right microphone sensitivity mismatch** — a different question, already covered in
the phonotaxis section.

- [ ] Write the answer that addresses placement angle. This needs your data on what ear angle
      actually does, which is why it is here rather than done.

### 5.3 Kinesis and Taxis — Assessment Q2 cites a section that does not exist
- [ ] Q2 refers to *"the protocol in section B"*. There is no section B and never was: both handouts
      are organised as "Condition 1 / 2 / 3", with no lettered sections anywhere. Q2 asks whether the
      protocol describes klinokinesis or klinotaxis, and the only protocol where that is a real
      question is Taxis Condition 1 — but that handout is *titled* "Condition 1. Klinotaxis", so
      simply repointing the question hands students the answer. That makes it a pedagogical choice
      rather than a reference repair: either rename the handout condition, or reword the question to
      describe the protocol instead of citing it.

### 5.4 The materials database is still thin for one lesson
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
- [ ] **The Required materials chapter has no quantities**, despite its opening sentence promising
      "the quantity required per student (or group of students)". Some entries say how many inside
      their description; most do not. Either add a column or drop the promise.
- [ ] **One line on that table cannot be ordered at all** — the whisker sensors are ours and are not
      sold. A teacher reading a purchasing list finds that out at the bottom. Worth a sentence at the
      top of the chapter saying so.
- [ ] The chapter calls the manipulative the **Blue Arrow** and measures in *arrow lengths*; both
      rules handouts call the same object the **Blue Bug** and measure in *bug-lengths*. The figure
      shows an arrow, so neither name is wrong about the artwork, but a group holding the handout and
      a teacher reading the chapter are using two words for one thing. The materials table mentions
      both, which is a bridge rather than a fix. Standardising means editing the chapter or
      regenerating the two `.docx` handouts, and only you know whether those are already printed.

### 5.5 Loose ends in the prose
- [ ] *Programming the robot*: your backlog says *"Create programs under 'Programming the robot'"* —
      it is the only lesson with no `.mblock` programs
- [ ] Backlog: *"Create Master slide deck"*, *"Use the slides below to illustrate the working
      principle of sonar"*, *"Update robot color vision activity?"*
- [ ] `files/burst_short.wav` is tracked but linked from nowhere — a 0.5 second mono 44.1 kHz burst,
      presumably meant as a stimulus alongside `pip_exported.mp3`. Either it lost its reference in the
      migration or it was superseded by the .mp3. Link it where it belongs, or delete it.
- [ ] The *Touch and Whiskers* standards section is still a placeholder. It needs the same four blocks
      as the other lessons, written by somebody who knows the standards rather than somebody
      pattern-matching from the other four.
- [ ] Minor, and only if it bothers you: *Introduction to Programming* uses "Challenge 1" and
      "Challenge 2" for the two conceptual halves of programming (working out the algorithm, then
      expressing it), while *Programming the robot* uses "Challenge 1–4" for the four exercises.
      Self-consistent within each chapter, but the same word carries two meanings across a page turn.

### 5.6 The bat-and-dolphin directionality figure in *Sonar*
`sonar-lesson-plan-c01f834f.png` — the two beam patterns seen from above — is from Madsen, P. T. &
Surlykke, A. (2013), *Functional Convergence in Bat and Toothed Whale Biosonars*, Physiology 28,
276–283, and is credited in its caption. It is the last figure in the book taken from someone else's
work that we have neither redrawn nor confirmed the licence of. Crossref records **no licence** for
that article, so it is presumably subscription material rather than open access: citing it is not the
same as being allowed to reproduce it.

- [ ] Check the licence properly — the APS permissions page, or write and ask
- [ ] If it is not reusable, redraw it from the published data the way the Maxbotix beam pattern and
      the microphone response were redrawn, or replace it with a measurement of our own robot, which
      would be better still: the students measure exactly this in Activity 1

### 5.7 Whether to rewrite git history for the replaced product photographs
The Makeblock studio shots — the dongle, the USB cable, the RJ25 cable, the default-configuration
robot — and the Makeblock board diagram are gone from the working tree but remain in the history,
where they were already public from the Notion site. While you are the only person with a clone,
dropping them from history is easy. It stops being easy once anyone else clones the repo.

- [ ] Decide, and if the answer is yes, do it before the repository is shared

The `board.svg` that the new board figure was exported from is 36 MB and lives in
`documentation_resources`, which is not tracked. Worth keeping wherever you keep the originals: the
figure cannot be relabelled without it.

---

## 6. Mechanical

### 6.1 Getting a new edition onto the website
Not a GitHub job — you've ruled that out, and rightly: teachers didn't use Notion and won't use
GitHub either. So the only route to a teacher is biologymeetsengineering.org, which makes uploading
the build the step that actually publishes anything. Worth being deliberate about it, and note the
order — the fingerprint is baked in at build time, so tagging after building stamps the bare hash:

```sh
git tag -a 2026-08 -m "Edition of August 2026"   # 1. tag first
cd book && ./build.sh                            # 2. footer picks the tag up
                                                 # 3. upload render/*.pdf and *.html
git push origin main && git push origin 2026-08
```

- [ ] Upload both files to the website
- [ ] Use a URL that stays the same between editions, so the link in the colophon and any link a
      teacher has bookmarked keeps working
- [ ] Tag the commit you built from. The footer fingerprint is `git describe --tags --always`, so
      tagging turns a bare hash into something you can ask a teacher to read back to you over email

The last one is worth the ten seconds. When someone reports a problem, the first question is which
version they have, and it is printed at the foot of every page.
