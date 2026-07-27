---
chapter: "Programming the robot"
source: 55-programming-the-robot.md
edition: "27 July 2026"
fingerprint: "6a5b178-stale"
---

# Programming the robot

**Tip:** This introduction assumes you and your students have mBlock installed or accessible online (Installing mBlock), can connect to the robot (Getting started with the robot), and have successfully run a test program (Running your first program).

This chapter introduces students to programming the mBot robot using mBlock, a visual programming language. Unlike text-based languages, users create programs by manipulating graphical blocks. While often considered simpler, specialized visual languages are widely used in engineering and science, making them compelling alternatives to traditional programming depending on context.

This chapter presents four simple programming challenges. Before the challenges, we introduce mBlock's interface, block categories, basic program structure, and variables. In our experience, students typically learn these quickly.

## Materials

| Item | Description |
| :--- | :--- |
| mBot Robot | The mBot robot |
| Bluetooth Dongle | A dongle for connecting the robot to a computer. Currently the recommended connection method. |
| Makeblock Sound Sensor | A sensor that reads current sound intensity. Used in the Sound Localization lesson and programming introduction. |
| Extra motors | Motors occasionally fail. Provide replacement motors for students. |
| Extra cables (short) | Extra cables for connecting sensors. These allow students to add sensors without removing existing connections, preventing lost cables. Cables come in packs of 4; we suggest supplying 1 extra cable per robot. Each is 20 cm long, matching the two cables included with the robot. |
| Gaffer's tape | Versatile tape useful throughout the activities. |
| Batteries | The robot requires 4 AA batteries. A 100-pack provides sufficient spares: with more than 8 batteries per robot, you can swap batteries without interrupting the curriculum. |

## Prerequisites

Algebra I

## Investigating/Essential Questions

- How can instructions be written so that a computer understands them?
- How can a robot be controlled through programming?

## Educational Standards

The educational standards applicable to this lesson are listed in the Educational standards chapter.

## Learning objectives

1. Students will write algorithms.
2. Students will use computational thinking to design solutions.
3. Students will learn to use a visual programming language.
4. Students will be able to write basic programs that control a robot’s actions.
5. Students will develop, test, and refine prototypes.

## Getting started with mBlock

Below we cover key aspects of mBlock to help you write programs for the robot.

### Explore the mBlock interface

Below is the mBlock interface, which appears nearly identical in both installed and online versions. The mBot has already been added in this screenshot, explaining its presence in the devices panel. On a fresh start, the mBot is not there and block categories differ; add it first to match this view.

1. **Program area:** Drag and drop blocks here to build a program.
2. **Block palette:** Lists available blocks, organized into categories such as Sensing and Control. Drag blocks from here to the program area. The [extension] button at the bottom adds more blocks by installing extensions.
3. **Stage:** Displays variable values while a program runs. Useful for debugging.
4. **Devices panel:** Shows devices whose blocks are available. The mBot appears here once added; see Adding the mBot to mBlock.

Figure: The four regions of the mBlock window, with the mBot already added: (1) where you build the program, (2) the blocks you build it from, listed by category, (3) the stage, where variable values appear while a program runs, and (4) the devices the blocks belong to. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-interface.png))

### Useful blocks

The mBlock interface provides many blocks organized into color-coded categories. Below is a brief introduction to the most relevant categories for these lessons. Every block, with what it does and what its dropdowns offer, is listed in the Block reference.

1. **Looks:** Only relevant if the robot has an LCD (sold separately). For our purposes, this category is not needed.
2. **Show:** Controls the onboard LEDs and buzzer. Blocks come in two forms: `LED all shows color red` sets the LEDs and continues, while `LED all shows color red for 1 secs` holds for that second then turns them off.
3. **Action:** Controls the motors. Two forms exist with an important difference: `move forward at power 50 % for 1 secs` moves for a set time then hands control back, while `move forward at power 50 %` starts the motors and immediately proceeds to the next block. Also includes `stop moving`.
4. **Sensing:** Reads the robot's sensors — onboard light sensor, ultrasonic (sonar) sensor, line follower, button. Blocks for additional sensors (sound, color) are available as extensions.
5. **Events:** Determines when a program starts. Two are relevant: `when flag clicked` starts programs in Live mode (used throughout these materials), while `when mBot (mcore) starts up` starts uploaded programs (needed for the Color Vision lesson). See Live versus Upload mode.
6. **Control:** Controls program flow: `forever` and `repeat` for repetition, `if ... then` and `if ... then ... else` for conditionals, and `wait` for pausing.
7. **Operators:** Arithmetic and comparison — add, subtract, multiply, divide, `<`, `=`, `>`. The `abs of` block (used in the last challenge) is here, accessible via a dropdown.
8. **Variables:** Contains blocks for working with variables. When you assign a sensor's output to a variable, its block appears here.
9. **My blocks:** Define your own custom blocks here.

### The basic structure of programs

Most programs follow a repeating pattern:

1. Read sensor values and store them in variable(s). The next section explains working with variables.
2. Perform operations on the variables (calculating differences, comparing values, summing, etc.).
3. Based on those results, decide what the motors should do (e.g., turn left or right).

These steps repeat continuously. Programs following this pattern start with two key blocks: `when flag clicked` from Events (the program's starting point, telling mBlock where to begin) and `forever` from Control (which repeats all enclosed blocks until the program stops). This template provides a foundation for most programs.

Figure: The starting point for most programs in these lessons: `when flag clicked` from Events, with `forever` from Control underneath it. Everything else goes inside the `forever` block. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-658b06bf.png))

### Working with variables in mBlock

Most programs require variables, making this a good time to introduce them.

A variable is a named container holding a value. Think of it as a labeled box: `set count to 0` places a value in the box, `change count by 1` modifies what is inside, and referencing `count` elsewhere means "use whatever value is currently in that box."

Students often do not initially understand why variables are necessary. Explain that sensor readings change constantly: asking the sonar for a distance twice yields two different numbers. To compare the current distance with a previous reading, one value must be stored. This is what the last challenge does — it stores the starting distance in `preferred_distance` while allowing `current_distance` to update. Without a variable, there is nothing to compare against.

To use a variable, first create it. In mBlock, click the `Variables` menu, then `Make a Variable`.
The images below illustrate this process. A window appears where you enter the variable's name.
Choose descriptive names connected to the variable's purpose. For this introduction, we create a simple counting program, so we name the variable `count`.
After creation, a block with that name appears under the `Variables` menu.

Figure: Step 1: select the `Variables` category. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-496da0e0.png))

Figure: Step 2: Click `Make a Variable`. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-4703540e.png))

Figure: Step 3: choose a name for your variable. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-32dcbd91.png))

Figure: Step 4: use the new blocks. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-f6a631e9.png))

Now use the new variable in a simple program (demonstrating variable use without the robot).
Although this program does not use the robot's sensors or motors, you must connect to the robot to run it.

The program sets `count` to zero, then repeatedly increments it by 1, waits a second, and checks if `count` exceeds 10, at which point it resets to zero.
Figure: The counting program. `count` is set to zero, then raised by one every second until it passes 10, at which point it is set back to zero. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-292d0d09.png))

Figure: The value of `count` shown on the stage while the program runs. Every variable you make appears here, which is what makes it possible to see what a program is doing. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-43ff905e.png))

**Note:** The green block can be found under `Operators`. To add the `count` block inside the green block, go to `Variables` and drag the `count` block to the left hand hole in the green block.

**Tip:** You can make as many variables as a program needs. The current value of every one of them is shown on the stage — the white area at the top left, where the panda sits — as in the second figure above. This display is the most useful debugging tool in mBlock, and the next section leans on it heavily.

### Advice worth passing on

Two habits matter most for the challenges below, both counter to students' natural tendencies.

**Test in small pieces.** Students typically build an entire program before first running it, making errors hard to diagnose. Encourage them to run the program as soon as there is anything to test.

In particular, immediately after a program reads a sensor into a variable, run it and monitor that variable on the stage. Is the value in the expected range? Does it change appropriately — does the light reading drop when a hand covers the sensor? Does the distance change when an object moves toward the robot? Two minutes of this testing catches the most common issues: a sensor plugged into the wrong port, or the right port selected in the wrong block. Both problems are invisible in a finished program but obvious in the variable display.

**Slower robots perform better.** Nearly every failed sensor challenge involves a robot moving too fast. A robot that moves slightly, takes a reading, and moves slightly again will reliably find lights, sounds, or walls. One that crosses the room in one burst or spins ninety degrees at a time overshoots and never settles.

Use the timed motor blocks — `move forward at power 25 % for 0.2 secs`, `turn left at power 25 % for 0.2 secs`. These move a definite amount then return control, allowing the next action to use fresh sensor data. The plain `move forward at power 50 %` block behaves differently: it starts the motors and immediately proceeds to the next block, so the robot continues accelerating while the program acts on stale sensor data. Lower power settings help for the same reason. There is no benefit to speed; a robot at 25 % power succeeds far more often than one at 100 %.

Both habits are especially valuable for the last challenge, where the robot must stabilize at a fixed distance rather than oscillate.

## Programming challenges

The four challenges use blocks covered above: starting blocks, `forever` loops, variables, sensor blocks, `if ... then` and `if ... then ... else`, comparison and arithmetic blocks, and motor blocks. Each challenge introduces a new concept rather than a new block: reacting to a reading, then reacting proportionally, then acting on the difference between two readings.

Students must locate individual blocks themselves, which is part of the learning. The two most frequently overlooked blocks are `abs of` (hidden behind a dropdown in Operators) and `if ... then ... else` (directly below `if ... then` in Control, easy to miss).

### Challenge 1: Blinking the LEDs

**Aside:** Challenge: Construct a program that turns the onboard LEDs on for a second and off for a second.

In this challenge, students create a program to blink the robot's onboard LEDs, a common introductory hardware programming example.

The solution requires only two blocks inside the loop. `LED all shows color red for 1 secs` lights the LEDs red for one second then turns them off; the block below does the same with black for the second half of the cycle. Since each block holds the program while active, no `wait` blocks are needed — adding them would extend the cycle. Use the standard `when flag clicked` and `forever` blocks as the backbone.

Figure: One solution to the blinking challenge. Each `shows color ... for 1 secs` block holds the program for its second, so the two together give one second on and one second off. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-blink-solution.png))

### Challenge 2: Reading a sensor

**Aside:** Challenge: Construct a program that briefly blinks the onboard LEDs when the light sensor reads below 500.

The robot has an onboard light sensor (described in Switches and onboard sensors). This sensor returns values from 0 to 1000 depending on the light intensity. For this challenge:

1. Read the light sensor and store the value in a variable.
2. If the value is below 500, briefly blink the LEDs.

One solution appears below. The program first ensures the LEDs are off, then repeatedly reads the light sensor. If the reading (stored in `light`) is below 500, it briefly toggles the onboard LEDs.

Figure: One solution to the light sensor challenge. The reading is stored in the variable `light` on every pass, and the LEDs blink only while that value is below 500. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-efc4bf9d.png))

### Challenge 3: Sound detection

**Aside:** Challenge: Construct a program that blinks the LEDs when sound exceeds a threshold. The blink duration should scale with loudness.

For this activity, connect a sound sensor to the robot via a cable, as shown below.

Figure: A sound sensor attached to the robot and taped to the top. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-1dea6db5.jpg))

#### Adding the sound sensor extension

Figure: The sound sensor. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-8b214556.jpg))

**Tip:** The sound sensor is not available by default; install an extension to use it.

To use the sound sensor, install an extension in mBlock. Click the `+` button at the bottom of the block panel, select `Light Sound` from the list, and click `Add`. This adds a new `light sound` category containing the sound sensor block.

Figure: Step 1: click the `+` button. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-7fb8f50a.png))

Figure: Step 3: Select the `Light Sound` extension. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-6f149564.png))

Figure: Adding the extension to mBlock gives you access to a new category of blocks. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-29c70a6b.png))

Figure: One of the new blocks is a block that allows you to read out the sound sensor. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-8267ed01.png))

#### Solution

Multiple solutions exist. The example below sets a threshold variable `min` to 200. If loudness is below this value, the LEDs stay off. If loudness exceeds the threshold, the LEDs turn on for a duration (in seconds) calculated as:

$$
duration = (loudness - min) / 50
$$

With `min` set to 200, the program responds to noise: louder sounds produce longer LED blinks.

Figure: One solution to the sound challenge. The sound sensor on port 3 is read; `min` holds the threshold, and LED duration scales with how far the reading exceeds it. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-d2e74147.png))

### Challenge 4: Keeping your distance

This challenge uses the motors and sonar sensor. The robot must maintain a fixed distance from an object: it moves forward if the distance increases and backward if it decreases.

**Aside:** Challenge: Program the robot to maintain a fixed distance from an object in front of the sonar.

Below is this challenge in action. The robot maintains its distance from the box; moving the box causes the robot to follow. This uses blocks from the `Action` category for motor control. These assume motors are connected to the correct ports (left motor to M1, right motor to M2). If the robot moves opposite to the command, the motor connectors are likely swapped. Multiple solutions exist; the program below is one approach.

Figure: The distance challenge in action. The robot holds its distance from the box; moving the box along the arrow makes the robot follow it. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-e395427b.jpg))

The program works as follows: at startup, it reads and stores the initial distance in `preferred_distance` (step 1). It then repeatedly reads the current distance into `current_distance` and calculates the difference from `preferred_distance`. If the absolute difference is less than 2 cm (step 3), the robot stops (step 6). If `abs(difference) > 2`, the robot moves: if `difference < 0`, it is too close and moves backward; if `difference > 0`, it moves forward. This maintains the robot at approximately `preferred_distance` from the obstacle. Create variables `difference`, `current_distance`, and `preferred_distance` first (see Working with variables in mBlock).

Moving the box causes the robot to follow while maintaining distance.

The program tolerates a 2 cm error margin. You can experiment with smaller values. However, the program becomes unstable at a certain point: the robot oscillates without stopping. This happens for two reasons: the sonar distance readings contain noise, and the program has a delay between movement and updated distance readings. Even with a noise-free sonar, this delay would cause oscillation.

Figure: One solution to the distance challenge. (1) The starting distance is stored in `preferred_distance`. Then, on each pass: (2) current distance is read and the difference calculated, (3) the difference is compared against a 2 cm tolerance, (4) the robot moves forward if too far, (5) backward if too close, and (6) stops if within range. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/programming-the-robot-55d3603f.png))
