---
chapter: "Introduction to Programming"
source: 50-intro-programming.md
edition: "27 July 2026"
fingerprint: "6a5b178-stale"
---

# Introduction to Programming

## Materials

| Item | Description |
| :--- | :--- |
| Printed programming blocks | These are the paper slips used in the Cheese Sandwich Factory game. |

## What is programming

The next chapter introduces mBlock, the language used to program the robot. This unit first introduces programming in the abstract, away from the robot and computer screen.

Programming is telling a machine what to do in a language it accepts. Here, the machine is a robot — essentially a computer with sensors and motors.

A **programming language** provides two things: a fixed set of instructions and rules for combining them. The instructions themselves do very little. Almost everything a program accomplishes comes from how they are combined, which is where most of the difficulty lies. In this unit, the language is a hypothetical one with four instructions; in the next chapter, it will be mBlock.

Before programming the robot, explore the challenges programmers face through this simple hypothetical example. Present students with the scenario below.

**Aside:** You are an engineer hired to program a mobile robot to reach the house's front door (indicated by an arrow) when the bell rings. The robot must reach the front door from any location in the house.

Figure: This image depicts the layout of an imaginary building. The building is serviced by a robot, which must be programmed to answer the door when the bell rings. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-programming-b71247e9.png))

Discuss this with students. Programmers face two distinct challenges here, worth separating:

- **Challenge 1: determining how to solve the problem.** What are the main difficulties? What would a solution look like? How can the problem be broken into smaller pieces? The outcome is an **algorithm**: a method that solves the problem, described clearly enough for someone else to follow, but not yet written in any programming language.
- **Challenge 2: expressing that algorithm in the language.** The language lacks an "answer the door" instruction. You must construct the desired behavior from the available instructions. This is the implementation problem.

Students often assume knowing how to do something means being able to program it. The activity below addresses this misconception: students will find they know perfectly well how to make a cheese sandwich yet still struggle to express it in just four instructions.

## Activity: Cheese Sandwich Factory Game

In this game, students write a program for a hypothetical robot and encounter both challenges. First, they must determine how to build a cheese sandwich at all given an awkward supply of ingredients. Then they must express that solution using only the four commands the robot understands, which requires understanding what each command actually does.

### Problem description

Imagine you are an engineer hired to write the program controlling a robot arm in a cheese sandwich factory. The image below shows the robot arm can reach three locations labeled 1-3. Your task is to write a program that directs the robot to make complete cheese sandwiches, each consisting of bread, cheese, and bread.

Figure: The Cheese Sandwich Maker game. Program the robot arm to use materials delivered on the conveyor belt (location 1) to build sandwiches on the truck's loading deck (location 3). Unneeded materials can be discarded on another conveyor belt (location 2). ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-programming-0aeb7e34.png))

1. **Location 1** is the end of a conveyor belt delivering slices of bread and cheese. **Importantly, the order is random.** You cannot predict whether the next item will be bread or cheese.
2. **Location 2** is the start of a second conveyor belt leading to additional factory robot arms. Use this to discard unneeded items. For example, if conveyor belt 1 delivers consecutive bread slices, the excess can be dropped onto conveyor belt 2.
3. **Location 3** is where sandwiches are assembled. For this game, each truck carries only one sandwich. Whenever a complete sandwich is assembled on the truck, it drives off and another truck takes its place. A complete sandwich consists of cheese between two bread slices.

The random delivery order is the core of the problem. With predictable deliveries, a fixed list of instructions would suffice. Because deliveries are random, the program must decide what to do as it executes.

### Robot programming language

For this game, the robot arm uses a simple programming language with just four commands. Each command is printed on its own slip, with a distinct color and symbol in the corner to distinguish them on a desk.

Every slip starts with `Step nr` and a pointing finger. Students write the instruction number here; these numbers are what the `Go to step nr` command references.

Figure: `Robot go to location ____` sends the arm to location 1, 2, or 3. Students write the location in the blank. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-programming-8607b09d.png))

Figure: `Go to step nr ____` jumps to another instruction by its step number. This allows students to skip part of a program or return to an earlier part to run it again. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-programming-9b5c7cb1.png))

Figure: `Pick up` and `Drop` act on whatever is at the arm's current location. Students check the box for the desired action. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-programming-331392b1.jpg))

Figure: `If holds ____ and below ____:` runs the indented instructions beneath it, but only when both conditions match the current situation. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-programming-8dc64988.png))

Each blank in the `If` command can be filled with: Bread, Cheese, Not Bread, Not Cheese, Any, or Nothing.

Clarify two conventions with the class before they start, as the slips do not show these:

**What `below` means.** This refers to whatever is on top of the pile at the arm's current location — the item the arm would pick up if it picked up now. At location 3, where sandwiches are built slice by slice, this is the most recently added slice, not the bottom one.

**How far an `If` reaches.** The `If` command controls the indented instructions placed directly beneath it. Establish this convention first, as slips laid out on a desk provide no other indication of which instructions belong to the `If` block.

The `If holds ___ and below ___` command sometimes confuses students. Here are two examples. The following is a valid program fragment.

```text
1 [If holds bread and below cheese:]
2     [Robot go to location 3]
3     [Drop]
4 [Robot go to location 2]
```

This directs the robot to check whether it is holding bread and whether cheese is at its current location. If both conditions are true, it moves to location 3 and drops the bread. It then proceeds to location 2, as that is the next instruction. If at the start the robot is not holding bread, or there is no cheese at its location, it skips lines 2 and 3 and proceeds directly to line 4.

Here is a second example.

```text
1 [Robot go to location 3]
2 [If holds cheese and below bread:]
3     [Drop]
4 [If holds nothing and below any:]
5     [Pick up]
```

This moves the robot to location 3, then checks whether it is holding cheese with bread below it; if so, it drops the cheese. It then checks whether it is holding nothing with either bread or cheese below it; if so, it picks that up.

This program contains a logic error. If the robot holds cheese with bread below, it drops the cheese at line 3. Then line 4 finds an empty hand with something below, so line 5 immediately picks up the same slice it just dropped. Walk students through this carefully. Each instruction makes sense individually; together they fail because the first changes the state that the second tests.

**Tip:** If students question the example's realism, reassure them. Many robots come with a specific set of instructions — a specialized programming language for that particular robot. For example, ST Robotics' robot arms use a custom language called RoboForth. Interested students can [consult the RoboForth manual](https://sandstechnology.com/manuals/manual17.htm).

### Playing the game

The commands are printed one per slip, formatted for [Avery Template 16154 Tickets With Tear-Away Stubs](https://www.avery.com/templates/16154) as front and back sheets. They also print well on ordinary paper and can be cut out by hand.

[Slips, front sheet (.doc)](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/files/Avery16154cheese_sandwich_front_windows.doc)

[Slips, back sheet (.doc)](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/files/Avery16154cheese_sandwich_back_windows.doc)

If you prefer not to print and cut these yourself, we can send you a pre-printed set. Contact **Dieter Vanderelst** at vanderdt@ucmail.uc.edu.

Before distributing the slips, have students write down in plain English how they would build a sandwich from a randomly ordered supply. This addresses Challenge 1 independently and prevents the activity from becoming trial and error with the slips. Only then distribute the slips and ask students to translate their plan into instructions.

The printed strips let students "write" a program by arranging and rearranging slips on their desks. Each student or group needs one set of instructions (both front and back sheets). This provides enough slips to construct a cheese sandwich-building program. Clarify that students need not use all slips — only those they require. Allocate sufficient time for them to attempt solving the problem and encourage peer review of each other's work.

### Possible Solution

Multiple solutions exist. The only way to verify a student's solution is to step through the program and confirm it builds cheese sandwiches. Here is one solution:

```text
 1  Robot go to location 1
 2  Pick up
 3  Robot go to location 3
 4  If holds cheese and below bread:
 5      Drop
 6  If holds bread and below cheese:
 7      Drop
 8  If holds bread and below nothing:
 9      Drop
10  Robot go to location 2
11  Drop
12  Go to step nr 1
```

This solution picks up whatever appears at location 1 and carries it to location 3. The three `If` instructions handle the three valid cases: placing cheese on bread, bread on cheese, and bread on an empty truck. If none match, the arm retains its item until line 10, where it is discarded at location 2.

Note that completed sandwiches are driven away, so any bread at location 3 is always the bottom slice of a new sandwich, not the top of a finished one. The `Drop` at line 11 executes regardless of whether the arm holds anything; this is harmless and ensures the arm is empty before returning to location 1.

### What the game taught

Students have just applied three concepts they will encounter again in mBlock. Name them before moving on.

**Sequence.** Instructions execute in the order they are placed, one after another. Most of the solution above relies solely on this.

**Selection.** `If holds ___ and below ___:` runs certain instructions only in specific situations. This allows the program to handle a conveyor belt delivering items in random order, explaining why a fixed list of instructions could never solve the problem.

**Repetition.** The `Go to step nr 1` at the end returns the program to the beginning, causing the entire sequence to repeat indefinitely. Students create a loop here without being explicitly taught the concept.

A fourth, less visible concept: at every moment, the program depends on **what the arm is holding** and **what is on the truck**. Neither appears in the written program, yet every decision depends on both. This is the program's **state**. The flawed example above fails precisely because the first instruction changes the state that the second tests.

All four concepts reappear in the next chapter. mBlock uses stacked blocks for sequences, provides an `if ... then` block for selection, and a `forever` block for repetition. It also allows creating variables to manage state explicitly. The solution above translates directly: the jump back to step 1 becomes a `forever` block enclosing all other instructions.

### Conclusion

After playing the game, discuss students' experiences. What difficulties did they encounter? Relate their experience to the two challenges programmers consistently face, both here and when programming the robot: determining what to do, then expressing it in a language with only a limited set of instructions.
