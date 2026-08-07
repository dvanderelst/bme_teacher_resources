# Style Guide for Biology Meets Engineering Teacher Manual

*Version 1.3 | Last updated: 2026-08-06*

This style guide establishes writing conventions for the Biology Meets Engineering teacher manual. It ensures consistency, clarity, and professionalism across all chapters.

---

## Table of Contents

1. [General Principles](#general-principles)
2. [Voice and Tone](#voice-and-tone)
3. [Grammar and Mechanics](#grammar-and-mechanics)
4. [Formatting](#formatting)
5. [Terminology](#terminology)
6. [Facts, Numbers, and Sources](#facts-numbers-and-sources)
7. [Punctuation](#punctuation)
8. [Common Patterns](#common-patterns)
9. [What to Avoid](#what-to-avoid)

---

## General Principles

### Write for teachers
- Assume the reader is a busy educator who needs clear, practical, actionable information
- Respect their time: be concise but complete
- Anticipate questions and address them proactively

### Prioritize clarity over elegance
- Clear > Clever
- Simple > Complex
- Direct > Circuitous

### Be consistent
- When in doubt, match the style of surrounding text
- Use this guide as the authoritative reference

---

## Voice and Tone

### Use active voice
- **Do:** "Connect the dongle to the computer"
- **Don't:** "The dongle should be connected to the computer"
- **Do:** "The program calculates the difference"
- **Don't:** "The difference is calculated by the program"

### "We" is us, "you" is the reader

The two are not interchangeable, and swapping one for the other changes who is
doing the work.

- **"We"** means the project: the people who wrote the materials, chose the robot, and taught the
  lessons. Use it for our recommendations, decisions, and experience.
  - **Do:** "We recommend pairing each dongle to a specific robot"
  - **Do:** "Our example programs load the extension automatically"
  - **Do:** "In our tests, Vivaldi failed to connect"
- **"You"** means the teacher reading the manual. Use it for anything they do, decide, or need to
  know.
  - **Do:** "The rest of this chapter covers the parts you need to know"
  - **Do:** "If you start from scratch, you must add the extension yourself"
  - **Do:** "Use the power switch as your landmark"
- **Don't** write "we" for a reader action. "If we prefer not to replace batteries" and "even if we
  forget the rule" describe the teacher, not us, and read as though the authors are standing at
  their elbow.
- **Don't** retreat into the impersonal to dodge the choice: "Each dongle must be paired" hides who
  is responsible.

### Maintain a professional but approachable tone
- Friendly and helpful, like a knowledgeable colleague
- Avoid sounding patronizing or overly casual
- Use complete sentences; avoid fragments in formal sections

---

## Grammar and Mechanics

### Sentence Structure
- **Aim for 15–25 words**, and vary the length for rhythm.
- **A long sentence is not automatically a fault.** The test is whether it carries one idea. Some of
  the best explanations in these chapters run past 40 words because the thought does not divide, and
  chopping them into fragments to satisfy a word count makes them harder to read, not easier.
- **Do** break a sentence that has changed subject halfway through, or that needs re-reading.

### Break up complex ideas
- One idea per sentence when possible
- Use bullet points or numbered lists for multi-part concepts
- Use parallel structure in lists

### Contractions
- **The chapters use none**, and read the better for it: the register is a knowledgeable colleague
  writing carefully, not chatting. Keep it that way — "do not", "cannot", "it is".
- This is a change from v1.0, which recommended contractions. The manual never followed that advice,
  so the guide now follows the manual.

### Possessives
- Use apostrophe-s for **possessive singular**: `Gaffer's tape`, `robot's sensors`
- For **plural possessives** ending in s, use apostrophe only: `students' materials`, `sensors' readings`
- **Do:** "The robot's sensors are calibrated"
- **Don't:** "The robots' sensors are calibrated" (unless referring to multiple robots)

---

## Formatting

### Headings
- Use **sentence case** for all headings (only first word and proper nouns capitalized)
- **Do:** `## Pairing the Bluetooth dongle and the robot`
- **Don't:** `## Pairing The Bluetooth Dongle And The Robot`
- End headings with **no punctuation** (no periods, colons, or question marks)
- **Exception:** Headings that are actual questions should end with a question mark

### Lists

#### Bullet Lists (-)
- Use for **non-sequential** items
- Use **consistent punctuation**: either all fragments (no punctuation) or all complete sentences (with periods)
- Capitalize the first word of each item
- **Preferred:** Fragments without ending punctuation for simple items
- **Example:**
  ```markdown
  - Left motor to `M1`
  - Right motor to `M2`
  - Reconnect power and turn on the robot
  ```

#### Numbered Lists (1. 2. 3.)
- Use for **sequential steps** or ordered items
- Each item should be a complete instruction or step
- End each item with appropriate punctuation (usually a period)
- **Example:**
  ```markdown
  1. Switch all robots off.
  2. Plug the dongle into a computer.
  3. Press the Bluetooth symbol on the dongle.
  ```

### Tables
- **Item column:** Use sentence case (only first word and proper nouns capitalized)
  - **Do:** `mBot robot`, `PVC pipe`, `3D-printed brackets`
  - **Don't:** `mBot Robot`, `PVC Pipe`
- **Description column:** Capitalize the first word of each cell
- End cells with appropriate punctuation:
  - Complete sentences: end with period
  - Fragments: no punctuation
- Align columns consistently (use markdown table syntax)
- **Example:**
  ```markdown
  | Your computers | Recommended option |
  | --- | --- |
  | Windows | Either. Installing is slightly more reliable. |
  | Mac | Either. Take care to select the correct version. |
  ```

### Bold and Italics
- **Bold:** Use for **key terms on first mention** and for **emphasis** — the one thing in a
  paragraph a hurried reader must not miss. Do not bold every component name; a page of bold is a
  page with no emphasis in it.
- **UI elements and button names take backticks, not bold.** The chapters already do this almost
  without exception: `` `Connect` ``, `` `Upload Code` ``, `` `Setting` ``, `` `Live` `` mode. Bold
  is for our voice; backticks are for words the software puts on the screen.
- *Italics:* Use for **publication titles**, **emphasis in definitions**, and *less critical emphasis*
  - `_Scratch-like visual programming language_`, *note: this is optional*

### Code/Technical Elements
- Use **backticks** for things the reader sees on screen, types, or reads off the hardware:
  - Block and command names: `` `when flag clicked` ``, `` `LED all shows color red` ``
  - Buttons, menus, and labels in mBlock: `` `Connect` ``, `` `Upload Code` ``, `` `File > Open from your computer` ``
  - File paths: `` `files/programs/MyFirstProgram.mblock` ``
  - Variables: `` `count` ``, `` `preferred_distance` ``
  - Markings printed on the board: `` `M1` ``, `` `IR_T` ``, `` `A0` ``
- **Do not** backtick ordinary technical nouns. `` `RJ25` `` is wrong: RJ25 is the name of a
  connector, like USB, not something the reader types. The same goes for mCore, mBot, and port
  numbers in running prose — the Terminology tables below write them plain, and prose should match.
- Use **code blocks** (```) for:
  - Multi-line code
  - Program examples
  - Command sequences

### Callouts (Notes, Tips, Warnings)
- Use blockquote syntax with bold labels
- Capitalize first word after the colon
- End the label line with a colon
- Leave a blank line before the content

```markdown
> **Note**
>
> The dongle flashes at two speeds, and they mean opposite things.

> **Tip**
>
> Test in small pieces. Run the program as soon as there is anything to test.

> **Warning**
>
> Do not charge the robot while it runs on the 4 AA batteries.
```

### Images and captions

**The text in `![...]` is the caption, not alt text.** The build runs pandoc with
`implicit_figures`, so that text is printed under the figure in the PDF and becomes the
`<figcaption>` in the HTML. A reader sees every word of it.

- **Never shorten a caption to make it "concise alt text".** There is no separate alt text to
  protect: pandoc uses the same string for both. Shortening deletes content from the page.
- A caption should carry what the picture cannot say for itself: what to look at, why it matters,
  and any number, port, or measurement the picture is evidence for.
  - **Do:** "An RJ25 cable. Both ends are identical, so it cannot be plugged in the wrong way. Two
    come with the robot, and in the default configuration both are already in use, which is why the
    materials list asks for a spare per robot."
  - **Don't:** "RJ25 cable: identical ends, telephone-style connector" (the purchasing implication
    is gone)
- **Walk multi-panel figures panel by panel**, using bold markers that match what is drawn on the
  image: **A**, **B**, **Left**, **Right**, **Top right**. A two-panel figure whose caption does not
  say which panel is which cannot be read.
- **Credit borrowed figures in the caption**: the creator, the licence with a link, and — if we
  changed anything — what we changed. Figures we drew ourselves say so ("Redrawn by us from ...").
  The licence table in *About these materials* must list the same items.
- Place images **on their own line** with blank lines before and after.

### Links
- **Never hand-edit a cross-reference anchor.** An anchor such as `#adding-color-sensor-extension` is
  generated from the heading it points at, by lowercasing it and joining the words with hyphens. It
  is not prose and must not be "corrected" to read better: making it
  `#adding-the-color-sensor-extension` because the link text says "the" silently breaks the link.
  If an anchor looks wrong, fix the *heading*, then every link to it.
- **Run `python3 book/tools/check-links.py` after any editing pass.** It reports broken anchors, and
  `build.sh` prints them too. Neither the PDF nor the HTML fails on a broken internal link, so
  nothing else will tell you.
- Use descriptive link text (avoid "click here" or "this link")
- **Do:** `[Assemble mBot](https://support.makeblock.com/...)`
- **Don't:** `[click here](https://support.makeblock.com/...)`
- For file links, include the file type in parentheses
- **Do:** `[Rules for Kinesis (.docx)](files/Rules_for_Kinesis.docx)`

### External Content
- **Preserve original capitalization, spelling, and punctuation** in external content:
  - External video titles
  - Publication titles
  - Proper names of organizations, products, or events
- **Do:** `[Video: Kinesis (Animal Movement) — Animal Behaviour](url)`
- **Don't:** Edit external titles to match this style guide

---

## Terminology

### Product Names
| Term | Correct Form | Notes |
|------|--------------|-------|
| Robot | mBot | Capital M, capital B, no space |
| Software | mBlock | Capital M, capital B, no space |
| Board | mCore | Capital M, capital C |
| Dongle | Bluetooth dongle | Or just "dongle" after first mention |
| Manufacturer | Makeblock | One word, capital M |

### Sensor Names
| Term | Correct Form |
|------|--------------|
| Sonar | sonar sensor |
| Sound | sound sensor |
| Light | light sensor (onboard) or external light sensor |
| Line follower | line follower |
| Color | color sensor |
| Whisker | whisker sensor |

### Ports and Connections
| Term | Correct Form |
|------|--------------|
| Port numbers | port 1, port 2, port 3, port 4 |
| Motor ports | `M1`, `M2` |
| Connection types | USB cable, Bluetooth dongle |

### Modes and States
| Term | Correct Form |
|------|--------------|
| Live Mode | Live mode |
| Upload Mode | Upload mode |
| Online Firmware | Online firmware |

### Spelling
- Use **American English** throughout
- **color** (not colour)
- **program** (not programme)
- **firmware** (one word)
- **realize** (not realise)
- **center** (not centre)

### Units of Measure
- Use **abbreviations without periods**: `ft`, `cm`, `in`, `mm`
- Spell out when used as a standalone noun: "The pipe is 6 feet long"
- Use abbreviations with numbers: "6 ft", "20 cm", "2 ft long"

---

## Facts, numbers, and sources

This manual is used by teachers standing in front of a class, and it feeds a support bot that will
repeat whatever it says. A wrong number here becomes a robot that behaves oddly for a reason nobody
can find.

### Every number must be traceable
- Say where a number came from: a measurement we made, a datasheet, a paper, or an estimate.
  - **Do:** "Makeblock's datasheet gives the microphone a signal-to-noise ratio of 54 dB, so the
    floor is 94 − 54 = 40 dB SPL"
  - **Do:** "Five distances from 42 to 106 cm, ratios 1.29 to 1.33"
  - **Don't:** "about 36 dB SPL" with no source and no date
- **Do not carry a number forward because it was already in the text.** The sonar correction sat at
  1.25 for years; when it was finally re-measured it was 1.30. The off-axis ranges quoted from a beam
  pattern were wrong by a factor of two until someone measured the plot.
- Show the arithmetic when it is short. It lets a reader check us, and it teaches.

### Do not fill a gap with a plausible inference
- If we have not checked something, the manual says so, or says nothing. It never guesses in the
  manual's own voice.
  - **Do:** "the `T` and `R` letters are not on the face shown here"
  - **Don't:** "the letters are on the underside of the board" (nobody had turned one over)
- This matters twice over because the teacher-support bot fills silences on its own. Asked why the
  sound sensor needs port 3 or 4, it invented an explanation about digital pins — which happened to
  be true, but was a guess. Where the prose stops short, write the missing sentence rather than
  leaving a hole for something else to fill.

### Figures are evidence
- A figure that supports a claim should show the claim. If it cannot, say so in the caption rather
  than letting the picture appear to prove something it does not.
- When a figure and the prose disagree, one of them is wrong. The programs said × 1.3 while their
  screenshots still said × 1.25 for one commit; that is the kind of thing a teacher notices and
  loses confidence over.

---

## Punctuation

### Em Dashes vs En Dashes
- **Em dash (—):** allowed, sparingly, with spaces, for a genuine break in thought or an aside that
  a comma is too weak to carry. Roughly 60 of them are in the chapters and most are earning their
  place. A comma or parentheses is often better, so reach for those first — but this is a preference,
  not a ban.
  - **Do:** "It does not, and it also works over the browser's direct connection — so a room with no
    cables can still recover a robot."
  - **Better, where it fits:** "The value is below 500 (the threshold for triggering)."
- **Never convert em dashes in bulk.** An em dash is not a long en dash: replacing `—` with `–`
  leaves the sentence exactly as unrephrased as before, in a narrower dash. If a dash should go, the
  sentence has to be rewritten by hand.
- **En dash (–):** Use without spaces for ranges
  - **Do:** "25–100%" (no spaces)
  - **Do:** "500–1000" (no spaces)

### Commas
- Use **Oxford comma** (serial comma) before "and" in lists
  - **Do:** "red, green, and blue"
  - **Don't:** "red, green and blue"
- Use commas to separate independent clauses
  - **Do:** "Press the button, and the light turns on."
  - **Don't:** "Press the button and the light turns on." (comma splice risk)

### Semicolons
- Use **sparsely**
- Prefer periods or rephrasing
- **Acceptable:** "Two cables come with the robot; both are already in use."
- **Better:** "Two cables come with the robot. Both are already in use."

### Parentheses
- Use for **clarifications, asides, and definitions**
- Keep content inside brief
- **Do:** "The onboard sensor reads 0 to 1000 (checked on the robot)."
- Avoid nesting parentheses

### Hyphens
- Use hyphens in **compound adjectives before a noun**: `3D-printed brackets`, `Lego-compatible blocks`, `100-pack`
- **Do:** "Use the 3D-printed brackets"
- **Don't:** "Use the 3D printed brackets"
- Do not hyphenate compound adjectives after the noun: "The brackets are 3D printed" (no hyphen needed)

---

## Common Patterns

### Instruction Format
```markdown
To [action]:

1. [First step].
2. [Second step].
3. [Third step].
```

### Definition Format
```markdown
**Term:** Brief definition that clarifies the concept.
```

### Example Format
```markdown
**Example:**
```
[Code or example]
```
```

### Important Notes
```markdown
**Important:** [Critical information].
```

---

## What to Avoid

### Redundancy
- **Don't:** "in order to" → use "to"
- **Don't:** "due to the fact that" → use "because"
- **Don't:** "at this point in time" → use "now"
- **Don't:** "in the near future" → use "soon"

### Wordiness
- **Don't:** "It is important to note that..." → use "Note:" or just state it directly
- **Don't:** "It has been found that..." → use active voice
- **Don't:** "There are several ways in which..." → use "Several ways exist:"

### Passive Voice
- **Don't:** "The program was run by the student" → "The student ran the program"
- **Don't:** "It can be seen that..." → "Notice that..." or just state the observation

### Jargon Without Explanation
- Explain technical terms on first use
- Use analogies where helpful
- **Do:** "A variable is a named container holding a value. Think of it as a labeled box."

### Inconsistent References
- **Don't:** Mix "the robot", "mBot", and "the mBot robot" in the same paragraph
- **Do:** Pick one and stick with it (preferably "the mBot" or "the robot")

### Overusing "However"
- Use sparingly; prefer "But" for a more natural flow
- **Do:** "But this approach has limitations."
- **Use "However"** when starting a new paragraph or for formal contrast

### Starting sentences with "It is" or "There are"
- **Don't:** "It is important that the robot is turned off."
- **Do:** "Turn the robot off." or "The robot must be turned off."
- **Don't:** "There are several ways to do this."
- **Do:** "You have several options:" or "Several approaches work:"

---

## Chapter Structure

Each lesson chapter should follow this structure when applicable:

```markdown
# Chapter Title

## Materials

| Item | Description |
| :--- | :--- |

## Prerequisites

[What students should know/be able to do]

## Investigating / Essential Questions

- Question 1?
- Question 2?

## Educational Standards

The standards applicable to this lesson are listed in the [Educational standards](#educational-standards) chapter.

## Learning Objectives

1. Objective 1
2. Objective 2

## Introduction

[Context and motivation]

## Activity: [Name]

[Detailed activity description]
```

Only *Introduction to Programming* ends with a `### Conclusion`, and there it earns its place by
telling the teacher what to discuss after the game. Most lessons end with the activity, the
assessment questions, or the troubleshooting table instead. Do not add a conclusion to satisfy the
template; add one when there is something to say after the last activity.

---

## Proofreading Checklist

Before finalizing a chapter, verify:

- [ ] All headings use sentence case
- [ ] "mBot", "mBlock", "mCore" are correctly capitalized
- [ ] American English spelling throughout (color, program, license, etc.)
- [ ] Active voice used consistently
- [ ] "We" means the project; "you" means the teacher reading. No reader action written as "we"
- [ ] Sentences are 25 words or fewer (most)
- [ ] Em dashes are earning their place (they are allowed); en dashes (–) without spaces for ranges
- [ ] Oxford comma used in lists
- [ ] Compound adjectives are hyphenated (3D-printed, Lego-compatible)
- [ ] Possessives use correct apostrophe forms (Gaffer's, students')
- [ ] Callouts (Note/Tip/Warning) are properly formatted
- [ ] Captions carry their content: no caption shortened to "alt text", panels named, borrowed
      figures credited with their licence
- [ ] `python3 book/tools/check-links.py` reports no broken anchors
- [ ] Every number added or changed has a stated source
- [ ] Code and block names use backticks
- [ ] Links use descriptive text
- [ ] Tables have consistent punctuation and sentence case in Item column
- [ ] Lists use parallel structure

---

## Tools for Consistency

> **Warning**
>
> Every pattern below changes meaning somewhere. Re-read each hit in context before accepting it.
> Replacing em dashes globally produced "released under that same ShareAlike license and marked as
> changed, and, going the other way, those five may be used commercially" — where the dash had been
> doing real work. Replacing "you" with "we" moved reader actions into the authors' voice across a
> whole chapter. A find-and-replace pass is a proposal, not a result.

### Search and Replace Patterns

| Find | Replace | Reason |
|------|---------|--------|
| colour | color | American spelling |
| programme | program | American spelling |
| m block | mBlock | Product name |
| Mbot | mBot | Product name |
| MBlock | mBlock | Product name |
| Port 1 | port 1 | Lowercase ports — but not at the start of a sentence |
| Port 2 | port 2 | Lowercase ports — but not at the start of a sentence |
| Port 3 | port 3 | Lowercase ports — but not at the start of a sentence |
| Port 4 | port 4 | Lowercase ports — but not at the start of a sentence |
| 3D printed | 3D-printed | Compound adjective |
| Lego compatible | Lego-compatible | Compound adjective |
| Gaffers tape | Gaffer's tape | Possessive form |
|  - | - | Remove extra spaces before list items |

### Regular Expressions for Cleanup

- Fix double spaces: `\s\s+` → ` ` (single space)
- Fix spaces before punctuation: `\s([,.!?;:])` → `\1`
- Fix list item spacing: `^\s*[-*+]\s+` → `- ` (standardize to one space)

---

## Revision History

- **v1.0** (2025): Initial style guide based on editing of chapters 10-65
- **v1.1** (2025-08-06): Added sections for Hyphens, Possessives, External Content, Units of Measure, and clarified Table capitalization rules based on editing of chapters 93 and 95
- **v1.2** (2025-08-06): Updated voice preference from direct address ("you") to first-person plural ("we"); clarified American English requirement in proofreading checklist
- **v1.3** (2026-08-06): Corrected v1.2, which had been read as licensing "we" for reader actions
  as well as ours: "we" is the project, "you" is the teacher. Established that the text in `![...]`
  is a printed caption and must not be shortened as though it were alt text. Added rules on
  cross-reference anchors, backtick scope, sourcing every number, not guessing in the manual's
  voice, and re-reading find-and-replace in context. All five were written after an editing pass
  broke a link, deleted 1,600 characters of caption, and moved reader actions into our voice.
  Also settled four rules that contradicted either themselves or the manual: em dashes are allowed
  and must never be bulk-converted (the `—` → `–` replacement row is deleted, as it fixed nothing);
  UI labels take backticks rather than bold; the chapters use no contractions and the guide now says
  so; and sentence length is guidance rather than a cap. Moved to `book/`, which is where the thing
  it governs lives, and which is inside the tracked whitelist in `.gitignore`.
