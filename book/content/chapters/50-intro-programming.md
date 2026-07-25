# Introduction to Programming

## Materials

| Item | Description |
| :--- | :--- |
| Printed programming blocks | These are the paper stubs used during the Cheese Sandwich Factory game. |

## What is programming

In the next chapter we introduce mBlock, the language we use to program the robot. Before that, this unit introduces programming in the abstract — away from the robot, and away from a screen.

Programming is telling a machine what to do in a language it accepts. The machine here is a robot, which is really a computer with some sensors and motors attached.

A **programming language** gives you two things: a fixed set of instructions, and rules for combining them. The instructions on their own do very little. Almost everything a program does comes from the way they are put together, and that is where most of the difficulty lives. In this unit the language is a made-up one with four instructions; in the next chapter it will be mBlock.

Before delving into programming the robot, explore the challenges programmers face through the following simple (made-up) example. Engage students with the scenario pictured below.

> You are an engineer hired to program a mobile robot to reach the house's front door (indicated with an arrow) when the bell rings. The robot should be able to get to the front door from any location in the house.

![This image depicts the layout of an imaginary building. The building is serviced by a robot, and we want to program it to answer the door when the doorbell rings.](images/introduction-to-programming-b71247e9.png)

Discuss this with students. Programmers face two quite different challenges here, and it is worth separating them.

- **Challenge 1: working out how to solve the problem at all.** What are the main difficulties? What would a solution look like? How can the problem be broken into smaller pieces? The outcome is an **algorithm**: a method that solves the problem, set out clearly enough that someone else could follow it, but not yet written in any programming language.
- **Challenge 2: expressing that algorithm in the language.** The language will not have an instruction for "answer the door". You have to build what you want out of the instructions you were given. This is the implementation problem.

Students often assume that knowing how to do something is the same as being able to program it. Separating the two challenges is the point of the activity below, where they will find that they know perfectly well how to make a cheese sandwich and still struggle to say it in four instructions.

## Activity: Cheese Sandwich Factory Game

In this game students write a program for a hypothetical robot, and meet both challenges in turn. First they have to work out how a cheese sandwich can be built at all, given an awkward supply of ingredients. Then they have to squeeze that idea into the four commands the robot understands, which means understanding what those commands actually do.

### Problem description

Imagine you are an engineer hired to write the program controlling a robot arm in a cheese sandwich factory. The image below shows that the robot arm can reach three locations labeled 1-3. You are asked to write a program for the robot such that it makes complete cheese sandwiches. A complete sandwich consists of a slice of bread, a slice of cheese, and another slice of bread.

![Image of the challenge faced in the Cheese Sandwich Maker game. Students are asked to program the robot arm to use the materials delivered on the conveyor belt (at location 1) to build cheese sandwiches on the loading deck of a truck (location 3). Unneeded materials (bread and cheese) can be discarded on another conveyor belt (location 2).](images/introduction-to-programming-0aeb7e34.png)

1. Location 1 corresponds to the end of a conveyor belt. This conveyor belt delivers slices of bread and cheese. **However, and this is important, the order is random.** You do not know in advance what the following item will be. It can be either bread or cheese.
2. Location 2 corresponds to the start of a second conveyor belt. This conveyor belt leads to additional robot arms in the factory. This conveyor belt can be used to drop off items that are not needed by the robot. For example, if the conveyor belt 1 delivers a run of bread, the superfluous slices of bread can be dropped onto conveyor belt two.
3. Location 3 corresponds to a place where cheese sandwiches are assembled. For the purpose of this game, we assume that the truck can only carry one cheese sandwich. Whenever a complete sandwich is assembled on the truck's back, it drives off, and another truck takes its place. For this game, a completed sandwich consists of a slice of cheese between two slices of bread.

The random delivery order is the heart of the problem. If students knew what was coming next, a fixed list of instructions would do. Because they do not, the program has to decide what to do as it goes.

### Robot programming language

For the purpose of the game, we imagine that the robot arm comes with a simple programming language that consists of just four commands. Each is printed on its own slip, and each has a different colour and a different symbol in the corner, which is what makes them easy to tell apart on a desk.

Every slip starts with `Step nr` and a pointing finger. That is where students write the number of the instruction, and those numbers are what the `Go to step nr` command refers to.

![`Robot go to location ____` sends the arm to location 1, 2 or 3. Students write the location in the blank.](images/introduction-to-programming-8607b09d.png)

![`Go to step nr ____` jumps to another instruction, by its step number. This is how students skip past part of a program, or go back to an earlier part and run it again.](images/introduction-to-programming-9b5c7cb1.png)

![`Pick up` and `Drop` act on whatever is at the arm's current location. Students tick the box for the one they want.](images/introduction-to-programming-331392b1.jpg)

![`If holds ____ and below ____:` runs the instructions beneath it, but only when both blanks match the current situation.](images/introduction-to-programming-8dc64988.png)

Each blank in the last command can be filled with one of: Bread, Cheese, Not Bread, Not Cheese, Any, Nothing.

Two things are worth settling with the class before they start, because the slips do not show them.

**What `below` means.** It is whatever is on top of the pile at the arm's current location — the thing the arm would pick up if it picked up now. At location 3, where a sandwich is being built up slice by slice, that is the most recently added slice, not the bottom one.

**How far an `If` reaches.** The instructions controlled by an `If` are the ones placed indented underneath it. Agree this convention before students begin, since a row of slips on a desk gives no other clue about where a block ends.

The `If holds ___ and below ___` command sometimes confuses students, so here are two examples. The following is a valid program fragment.

```text
1 [If holds bread and below cheese:]
2     [Robot go to location 3]
3     [Drop]
4 [Robot go to location 2]
```

This makes the robot check whether it is holding bread and whether there is a slice of cheese at its current location. If so, it goes to location 3 and drops what it is holding, in this case the bread. It then moves to location 2, because that is the next instruction. If at the start of the fragment the robot is not holding bread, or there is no cheese at its location, it skips lines 2 and 3 and goes straight to line 4.

Here is a second example.

```text
1 [Robot go to location 3]
2 [If holds cheese and below bread:]
3     [Drop]
4 [If holds nothing and below any:]
5     [Pick up]
```

This moves the robot to location 3, then checks whether it is holding cheese with bread below it; if so, it drops the cheese. It then checks whether it is holding nothing with either bread or cheese below it; if so, it picks that up.

This program is quite silly. If the robot holds cheese and there is bread below, it drops the cheese at line 3 — and then line 4 finds an empty hand with something below it, so line 5 picks the very same slice straight back up. It is worth walking students through this one slowly. The two instructions are each sensible on their own; what makes them useless together is that the first one changes the situation the second one tests.

> **Tip**
>
> If students think the example is not realistic, you can reassure them. Robots often come with a specific set of instructions, which is a specialized programming language for this particular robot. For example, the robot arms distributed by ST Robotics use a custom programming language called Roboforth. The brave could [consult this manual](https://sandstechnology.com/manuals/manual17.htm) for the RoboForth language.

### Playing the game

The commands are printed one to a slip. They are laid out for [Avery Template 16154 Tickets With Tear-Away Stubs](https://www.avery.com/templates/16154), as a front sheet and a back sheet, but they print perfectly well on ordinary paper and can be cut out by hand.

[Slips, front sheet (.doc)](files/Avery16154cheese_sandwich_front_windows.doc)

[Slips, back sheet (.doc)](files/Avery16154cheese_sandwich_back_windows.doc)

If you would rather not print and cut them yourself, ask us and we will send you a set. Write to **Dieter Vanderelst**, [vanderdt@ucmail.uc.edu](mailto:vanderdt@ucmail.uc.edu).

Before handing out the slips, ask students to write down in plain English how they would build a sandwich from a supply that arrives in a random order. That is Challenge 1 on its own, and doing it first is what keeps the activity from becoming trial and error with bits of paper. Only then give out the slips, and ask them to turn their plan into instructions.

Providing the students with printed strips allows them to "write" a program by placing and moving the slips around on their desks. Each student (group) should receive one set of printed instructions (i.e., a front and a back version of the strips). This should be sufficient to construct a program for making the robot build cheese sandwiches. Make it clear to students they are not expected to use all the slips. Only as many as they think they need. Give students sufficient time to try to construct a program that solves the problem. Encourage them to check each other's work.

### Possible Solution

There are different solutions to the game. The only way to test whether a solution provided by a student works is to step through the program and work out whether it results in cheese sandwiches being built. Here is one solution:

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

This solution picks up whatever is presented at location 1 and carries it to location 3. The three `If` instructions cover the three cases where the item in the arm is the one the sandwich needs next: cheese onto bread, bread onto cheese, and bread onto an empty truck. In every other case none of them matches, the arm still holds its item when it reaches line 10, and the item is discarded at location 2.

Remember that a finished sandwich is driven away, so bread at location 3 is always the bottom slice of a new sandwich rather than the top of a finished one. The `Drop` at line 11 runs whether or not the arm is holding anything, which is harmless and guarantees the arm is empty before it returns to location 1.

### What the game taught

Students have just used three ideas that they will meet again in mBlock, and it is worth naming them before moving on.

**Sequence.** Instructions run in the order they are placed, one after the next. Most of the solution above is nothing more than this.

**Selection.** `If holds ___ and below ___:` runs some instructions only in some situations. This is what lets the program cope with a conveyor belt delivering in a random order, and it is the reason a fixed list of instructions could never have solved the problem.

**Repetition.** The `Go to step nr 1` at the end sends the program back to the beginning, so the whole thing runs again, and again, indefinitely. Students build a loop here without being told the word for it.

There is a fourth idea, harder to see because nothing on the desk represents it: at every moment the program depends on **what the arm is holding** and **what is on the truck**. Neither is written anywhere in the program, yet every decision turns on both. This is what programmers call the state of a program, and it is why the silly example above goes wrong — the first instruction changes the state that the second one tests.

All four ideas reappear in the next chapter. mBlock stacks blocks to make a sequence, has an `if ... then` block for selection and a `forever` block for repetition, and lets you create variables to hold state explicitly. The solution above translates almost directly: the jump back to step 1 becomes a `forever` block wrapped around everything else.

### Conclusion

After playing the game, ask students about their experiences. What difficulties did they encounter? Try to relate their experience to the two challenges programmers face, and will face again when programming the robot: working out what to do, and then saying it in a language that only understands a handful of instructions.
