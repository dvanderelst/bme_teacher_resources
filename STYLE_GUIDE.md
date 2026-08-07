# Style Guide for Biology Meets Engineering Teacher Manual

*Version 1.0 | Last updated: 2025*

This style guide establishes writing conventions for the Biology Meets Engineering teacher manual. It ensures consistency, clarity, and professionalism across all chapters.

---

## Table of Contents

1. [General Principles](#general-principles)
2. [Voice and Tone](#voice-and-tone)
3. [Grammar and Mechanics](#grammar-and-mechanics)
4. [Formatting](#formatting)
5. [Terminology](#terminology)
6. [Punctuation](#punctuation)
7. [Common Patterns](#common-patterns)
8. [What to Avoid](#what-to-avoid)

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

### Use direct address
- Use "you" to speak directly to the teacher
- **Do:** "You must pair each dongle to a specific robot"
- **Don't:** "Each dongle must be paired to a specific robot" (less direct)

### Maintain a professional but approachable tone
- Friendly and helpful, like a knowledgeable colleague
- Avoid sounding patronizing or overly casual
- Use complete sentences; avoid fragments in formal sections

---

## Grammar and Mechanics

### Sentence Structure
- **Target length:** 15-25 words per sentence
- **Maximum:** Break up sentences longer than 30 words
- Vary sentence length for rhythm, but keep most sentences concise

### Break up complex ideas
- One idea per sentence when possible
- Use bullet points or numbered lists for multi-part concepts
- Use parallel structure in lists

### Contraction usage
- **Use contractions** for a natural, conversational tone: "don't", "can't", "won't", "it's"
- **Avoid contractions** in formal definitions or when emphasis is needed

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
- **Bold:** Use for **UI elements**, **button names**, **key terms on first mention**, and **emphasis**
  - `**mBlock**`, `**Start menu**`, `**Live mode**`
- *Italics:* Use for **publication titles**, **emphasis in definitions**, and *less critical emphasis*
  - `_Scratch-like visual programming language_`, *note: this is optional*

### Code/Technical Elements
- Use **backticks** for:
  - Code and block names: `` `when flag clicked` ``, `` `LED all shows color red` ``
  - File paths: `` `files/programs/MyFirstProgram.mblock` ``
  - Technical terms in context: `` `port 1` ``, `` `mCore` ``
  - Variables: `` `count` ``, `` `preferred_distance` ``
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

### Images
- Use markdown image syntax: `![Alt text](path/to/image.png)`
- **Alt text:** Describe the image content clearly and concisely
- **Do:** `![The mCore in two views](images/mcore-labelled.png)`
- **Don't:** `![Image](images/mcore.png)` (vague)
- **Don't:** `![The mCore in two views: Left, as it comes in the robot...](images/mcore.png)` (too long in alt text)
- Place images **on their own line** with blank lines before and after
- For captions that are part of the alt text, keep them under 80 characters if possible

### Links
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

## Punctuation

### Em Dashes vs En Dashes
- **Em dash (—):** Use with spaces around it for parenthetical phrases
  - **Do:** "The value is below 500 — the threshold for triggering."
  - Actually, **prefer** to rephrase: "The value is below 500, the threshold for triggering."
  - Or: "The value is below 500 (the threshold for triggering)."
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

## Conclusion

[Wrap-up and key takeaways]
```

---

## Proofreading Checklist

Before finalizing a chapter, verify:

- [ ] All headings use sentence case
- [ ] "mBot", "mBlock", "mCore" are correctly capitalized
- [ ] "color" not "colour" throughout
- [ ] Active voice used consistently
- [ ] Direct address ("you") used where appropriate
- [ ] Sentences are 25 words or fewer (most)
- [ ] No em dashes (—) with spaces; use en dashes (–) without spaces for ranges
- [ ] Oxford comma used in lists
- [ ] Compound adjectives are hyphenated (3D-printed, Lego-compatible)
- [ ] Possessives use correct apostrophe forms (Gaffer's, students')
- [ ] Callouts (Note/Tip/Warning) are properly formatted
- [ ] Image alt text is descriptive and concise
- [ ] Code and block names use backticks
- [ ] Links use descriptive text
- [ ] Tables have consistent punctuation and sentence case in Item column
- [ ] Lists use parallel structure

---

## Tools for Consistency

### Search and Replace Patterns

| Find | Replace | Reason |
|------|---------|--------|
| colour | color | American spelling |
| programme | program | American spelling |
| m block | mBlock | Product name |
| Mbot | mBot | Product name |
| MBlock | mBlock | Product name |
| Port 1 | port 1 | Lowercase ports |
| Port 2 | port 2 | Lowercase ports |
| Port 3 | port 3 | Lowercase ports |
| Port 4 | port 4 | Lowercase ports |
| 3D printed | 3D-printed | Compound adjective |
| Lego compatible | Lego-compatible | Compound adjective |
| Gaffers tape | Gaffer's tape | Possessive form |
| — | – | En dash for ranges |
|  - | - | Remove extra spaces before list items |

### Regular Expressions for Cleanup

- Fix double spaces: `\s\s+` → ` ` (single space)
- Fix spaces before punctuation: `\s([,.!?;:])` → `\1`
- Fix list item spacing: `^\s*[-*+]\s+` → `- ` (standardize to one space)

---

## Revision History

- **v1.0** (2025): Initial style guide based on editing of chapters 10-65
- **v1.1** (2025-08-06): Added sections for Hyphens, Possessives, External Content, Units of Measure, and clarified Table capitalization rules based on editing of chapters 93 and 95
