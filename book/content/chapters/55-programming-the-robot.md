# Programming the robot

> **Tip**
>
> This brief introduction to mBlock assumes you (and the students) have installed mBlock on the computer or have access to mBlock online. See [Installing mBlock](#installing-mblock). We also assume you (and the students) understand how to connect to the robot. See [Getting started with the robot](#getting-started-with-the-robot). We also assume that you (and the students) have successfully run a first test program to ensure the robot is connected to the computer. If not, see [Running your first program](#running-your-first-program).

This lesson is intended to introduce students to programming the mBot robot. The mBot can be programmed using the mBlock programming language. This is a visual programming language. In contrast to most programming languages, users write a program by manipulating elements graphically instead of typing text. While visual programming languages are often considered simpler, many examples of specialized visual programming languages are used in engineering and science. Therefore, depending on the context, visual programming languages can be compelling alternatives to text-based programming.

In this chapter, we present four quite simple programming challenges you can present to the students to familiarize themselves with programming the robot. Before listing the challenges, we provide an introduction to mBlock. We cover the interface, where to find blocks to create programs, and how to work with variables. We also explain the basic structure of most programs. In our experience, this can be covered quite quickly with students as they usually find out these things quickly.

## Materials

| Item | Description |
| :--- | :--- |
| mBot Robot | The mBot robot |
| Bluetooth Dongle | This is a dongle that allows to connect to the robot from a computer. This is currently the recommended way to work with the robot. |
| Makeblock Sound Sensor | Sensor reading the current sound intensity. Used in the sound localization plan and the intro to programming. |
| Extra motors | Motors seem to be a component that fails from time to time. Students should be provided with replacement motors |
| Extra cables (short) | Extra cables for connecting sensors. This allows students to add sensors without removing cables and covers for losing cables.  The cables come in a pack of 4. I suggest supplying 1 extra cable per robot.  This cable is 20 cm long and has the same length as the 2 cables that come with the robot. |
| Gaffers tape | It’s tape. What else can I say. It comes in handy everywhere. |
| Batteries | The robot takes 4 AA batteries. These should last a while. This is a 100 pack of AA batteries Providing more than 8 batteries per robot should allow swapping out the batteries and getting new stock without interruption to the curriculum. |

## Prerequisites

Algebra I

## Investigating/Essential Questions

- How can instructions be written so that a computer understands them?
- How can a robot be controlled through programming?

## Educational Standards

The educational standards applicable to this lesson are listed in the [Educational standards](#educational-standards) chapter.

## Learning objectives

1. Students will write algorithms.
2. Students will use computational thinking to design solutions.
3. Students will learn to use a visual programming language.
4. Students will be able to write basic programs that control a robot’s actions.
5. Students will develop, test, and refine prototypes.

## Getting started with mBlock

As mentioned in an earlier chapter, mBlock is the software we will use to program the robot. Below, we cover some basic aspects of mBlock to help you get started writing programs for the robot.

### Explore the mBlock interface

Below, we show the mBlock interface. It looks much the same whether you use the installed program or the online version. The mBot has already been added in this screenshot, which is why it appears in the devices panel; on a fresh start it is not there and the block categories are different, so add it first and the window will look like this.

1. This area is used for constructing a program. You will drag and drop blocks onto this field to form a program.
2. This window area lists the blocks that can be used to create a program. The blocks are organized into categories such as [Sensing] and [Control]. To use a block, you drag and drop it to area (1). Notice the [extension] button at the bottom of this area (2). Additional blocks can be added by installing extensions.
3. This part of the screen shows the values of variables in a program. This information is useful when trying to figure out why a program does not work as expected.
4. The devices whose blocks are available. The mBot is listed here because it has been added; on a fresh start it is not, and adding it is the first thing to do. See [Adding the mBot to mBlock](#adding-the-mbot-to-mblock).

![The four regions of the mBlock window, with the mBot already added: (1) where you build the program, (2) the blocks you build it from, listed by category, (3) the stage, where variable values appear while a program runs, and (4) the devices the blocks belong to.](images/programming-the-robot-interface.png)

### Useful blocks

The mBlock interface provides many blocks, organized in multiple categories. Below, we briefly introduce the blocks found in each category. Note that mBlock color codes the groups. This makes it easier to find the blocks we use in the programs in the lesson plans.

1. Looks: These blocks are only relevant if you equip the robot with an LCD (sold separately). For
our purposes, this category is irrelevant.
2. Show: The onboard LEDs and the buzzer. As with the motor blocks below, there are two forms: `LED all shows color red` sets the LEDs and moves on, while `LED all shows color red for 1 secs` holds the program for that second and then switches them off again.
3. Action: The motors. These blocks come in two forms, and the difference matters more than it looks: `move forward at power 50 % for 1 secs` moves for a set time and then hands control back, while `move forward at power 50 %` starts the motors and moves straight on to the next block. There is also `stop moving`.
4. Sensing: These blocks read the robot's own sensors — the onboard light sensor, the ultrasonic (sonar) sensor, the line follower, the button. Blocks for sensors that do not come with the robot, such as the sound sensor and the color sensor, arrive as extensions.
5. Events: These blocks say when a program should start. Two matter here. `when flag clicked` starts a program in Live mode, and is the one used almost everywhere in these materials. `when mBot (mcore) starts up` starts a program that has been uploaded to the robot, which is what the Color Vision lesson needs. See [Live versus Upload mode](#live-versus-upload-mode).
6. Control: These blocks decide what runs and how often: `forever` and `repeat` for repetition, `if ... then` and `if ... then ... else` for choosing between alternatives, and `wait` for pausing.
7. Operators: Arithmetic and comparison — add, subtract, multiply, divide, and the `<`, `=`, `>` blocks. The `abs of` block, which the last challenge in this chapter uses, is one of these: it sits behind the dropdown on the block that starts out reading `abs of`.
8. Variables: This category contains the blocks keeping track of variables. For example, if you assign a sensor's output to a variable, you would find a block representing that variable here.
9. My blocks: Here, you can define your own blocks.

### The basic structure of programs

Most programs we will be constructing will repeat the following steps over and over again:

1. Read the selected sensors' status and store the results in (a) variable(s). The next section explains how to work with variables.
2. Perform some operations on the variables. For example, we might calculate the difference
between variables, compare their values, or sum them.
3. Depending on the outcome of the operations, decide what the motors should do. For example,
should the robot turn left or right?

Steps 1-3 will typically be repeated over and over again. Constructing a program that adheres to this logic would be started using the following blocks. The top block (found in the events category) is the program's starting point. This tells mBlock where to start reading your program. The next block reads `forever` and can be found in the `control` category. This indicates that whatever blocks are added inside this block will be repeated (until you stop the program). This basic template can be used to get started on most programs.

![The starting point for most programs in these lessons: `when flag clicked` from Events, with `forever` from Control underneath it. Everything else goes inside the `forever` block.](images/programming-the-robot-658b06bf.png)

### Working with variables in mBlock

Most programs will require using a variable. Therefore, this is a good time to introduce students to using variables.

A variable is a box with a name written on it, holding a value you can read back later. `set count to 0` puts a value in the box, `change count by 1` alters what is in it, and writing `count` anywhere else in the program means "whatever is in that box at this moment".

It is worth telling students *why* a program needs one, because the answer is not obvious until they hit it. Sensor readings do not hold still: ask the sonar for a distance twice and you get two different numbers. So if you want to compare the distance now against the distance a moment ago, one of them has to be put in a box and kept. That is exactly what the last challenge in this chapter does — it holds the distance the robot started at in `preferred_distance`, and lets `current_distance` change underneath it. Without a variable there is nothing to compare against.

Before using a variable, you must define (or “make”) it. In mBlock, you can create variables by clicking the `variables` menu and then clicking `Make a Variable`. See the images below for an illustration. This will bring up a window where you can enter the name of your new variable. The name of the variable is arbitrary. However, it’s usually a good idea to give the variable a name you can remember and has some connection to what you wish to use the variable for. In this introduction to variables, we will create a simple program that counts to 10. Therefore, we will name our variable `count`. Once you have created a variable, a block with that name will be created under the `variables` menu.

![Step 1: select the category `variables`.](images/programming-the-robot-496da0e0.png)

![Step 2: Click `make a variable`.](images/programming-the-robot-4703540e.png)

![Step 3: choose a name for your variable.](images/programming-the-robot-32dcbd91.png)

![Step 4: use the new blocks.](images/programming-the-robot-f6a631e9.png)

Now, we can use our newly created variable in a simple program (that does not involve the robot but demonstrates the use of a variable). Even though the program does not use the robot’s sensors or motors, you will need to connect to the robot to run it (otherwise, the program will not run).

The program starts by setting the variable `count` to zero. Then, it increases the value of `count` by 1 before waiting a second and repeating this. Once the value of `count` is larger than 10, `count` is reset to zero.

![The counting program. `count` is set to zero, then raised by one every second until it passes 10, at which point it is set back to zero.](images/programming-the-robot-292d0d09.png)

![The value of `count` shown on the stage while the program runs. Every variable you make appears here, which is what makes it possible to see what a program is doing.](images/programming-the-robot-43ff905e.png)

> **Note**
>
> The green block can be found under `Operators`. To add the `count` block inside the green block, go to `Variables` and drag the `count` block to the left hand hole in the green block.

> **Tip**
>
> You can make as many variables as a program needs. The current value of every one of them is shown on the stage — the white area at the top left, where the panda sits — as in the second figure above. This display is the most useful debugging tool in mBlock, and the next section leans on it heavily.

### Advice worth passing on

Two habits make more difference than anything else in the challenges below, and both cut against what students naturally do.

**Test in small pieces.** Students tend to build a whole program and run it for the first time when it is finished, at which point anything could be wrong and there is no way to tell what. Get them into the habit of running the program as soon as there is anything to run at all.

In particular, the moment a program reads a sensor into a variable, run it and watch that variable on the stage. Is the number in the range you expect? Does it change when it should — does the light reading drop when a hand covers the sensor, does the distance change when a book is moved towards the robot? Two minutes of this catches the two commonest faults in the whole course: a sensor plugged into a port the program is not reading, and the right port picked in the wrong block. Both are invisible in the finished program and obvious in the variable display.

**Slower robots do better.** Nearly every failed attempt at the sensor challenges involves a robot driving or turning too fast. A robot that moves a little, takes a fresh reading, and moves a little again will find a light, a sound or a wall. One that crosses the room in a single burst, or spins ninety degrees at a time, overshoots and never settles.

The blocks to reach for are the timed ones — `move forward at power 25 % for 0.2 secs`, `turn left at power 25 % for 0.2 secs`. They move a definite amount and then hand control back, so the next thing the program does is take a fresh reading. The plain `move forward at power 50 %` block is different: it starts the motors and moves straight on to the next block, so the robot is still accelerating while the program is deciding what to do about a reading it took some time ago. Lower power helps for the same reason. There is no prize for speed, and a robot at 25 % power succeeds at these challenges far more often than one at 100 %.

Both habits pay off again in the last challenge in this chapter, where the robot has to settle at a fixed distance rather than oscillate around it.

## Programming challenges

Everything the four challenges need has been covered above: the starting blocks, the `forever` loop, variables, the sensor blocks, `if ... then` and `if ... then ... else`, the comparison and arithmetic blocks, and the motor blocks. The one thing each challenge adds is an idea rather than a block — reacting to a reading, then reacting proportionally, then acting on the difference between two readings.

Students will still have to hunt for individual blocks, which is part of the exercise. The two most often searched for in vain are `abs of`, hidden behind a dropdown in Operators, and `if ... then ... else`, which sits directly below the plain `if ... then` in Control and is easy to miss.

### Challenge 1: Blinking the LEDs

> Challenge: Construct a program that switches on the onboard LEDs for a second and turns them off for a second.
>

In this challenge, students will construct a program to make the onboard LEDs of the robot blink. Blinking LEDs is a prevalent first example in tutorials about programming hardware. Here, we adhere to this tradition.  An example program is below.

The program below needs only two blocks inside the loop. `LED all shows color red for 1 secs` lights the LEDs red, holds the program for a second, and then turns them off; the block below it does the same with black, which is how the LEDs are switched off for the second half of the cycle. Because each block holds the program while it runs, no `wait` blocks are needed — adding them would stretch the cycle rather than set it. The backbone is the usual `when flag clicked` and `forever`.

![One solution to the blinking challenge. Each `shows color ... for 1 secs` block holds the program for its second, so the two together give one second on and one second off.](images/programming-the-robot-blink-solution.png)

### Challenge: Reading a sensor

> Challenge: Construct a program that briefly blinks the onboard LEDs when the onboard light sensor registers a value smaller than 500.
>

The robot has an onboard light sensor, one of the inputs described in [Switches and onboard sensors](#switches-and-onboard-sensors). The sensor gives a value from 0 to 1000, depending on the light's intensity falling on the sensor. In this example, we will use this sensor to program the robot to do the following:

1. Read the onboard light sensor and store the result in a variable.
2. If the light value is smaller than 500, blink the lights briefly.

The program below is one solution to this challenge. The program starts by switching the LEDs to ensure they are off at the program's start. Next, the program repeatedly reads the value of the onboard light sensor. If the sensor (stored in the variable `light`) is smaller than 500, the program switches on and off the onboard LEDs.

![One solution to the light sensor challenge. The reading is stored in the variable `light` on every pass, and the LEDs blink only while that value is below 500.](images/programming-the-robot-efc4bf9d.png)

### Challenge: Sound Detection

> Challenge:  Construct a program that blinks the LEDs if the sound is louder than a set value. The duration of the LEDs' blink should depend on the loudness of the sound.
>

For this activity, we will connect a single sound sensor to the robot using a cable. An example of a robot equipped with a sound sensor is shown below.

![A single sound sensor is attached to the robot and taped to the top of the robot.](images/programming-the-robot-1dea6db5.jpg)

#### Adding the sound sensor extension

![The sound sensor.](images/programming-the-robot-8b214556.jpg)

> **Tip**
>
> By default, the sound sensor is not available in the code. We need to install an extension to use it, as explained below.

We need to install an extension to mBlock to use the sound sensor. Click the (rather small) `+` button at the bottom of the block panel in mBlock. In the list of extensions, select `Light Sound` and click `Add` . This makes a new category of block available: `light sound`. In this category, you can find a block to access the value of the sound sensor.

![Step 1: click the `+` button.](images/programming-the-robot-7fb8f50a.png)

![Step 3: Select the `Light Sound` extension.](images/programming-the-robot-6f149564.png)

![Adding the extension to mBlock gives you access to a new category of blocks.](images/programming-the-robot-29c70a6b.png)

![One of the new blocks is a block that allows you to read out the sound sensor.](images/programming-the-robot-8267ed01.png)

#### Solution

There are various ways to solve the challenge. The example below sets a variable `min` = 200. The LEDs are not switched on if the loudness is lower than this value. If the loudness is higher than this threshold, the LEDs are switched on for a duration (in seconds) given as follows:

$$
duration = (loudness - min) / 50
$$

With `min` set to 200. This program should respond to noise: louder noises result in a longer blink of the LEDs.

![One solution to the sound challenge. The sound sensor is read on port 3; `min` holds the threshold, and the LEDs stay lit for a time that grows with how far the reading exceeds it.](images/programming-the-robot-d2e74147.png)

### Challenge: Keeping your Distance

The following programming challenge will use the motors. Using the sonar sensor, we will program the robot to maintain a fixed distance from an object. When starting the program, the robot will read the distance to the nearest object (detected by the sonar). Next, the robot will move forward if the distance increases and backward if the distance decreases.

> Challenge: Program the robot to keep a fixed distance from an object in front of the sonar.
>

Below is an example of this challenge in action. The robot tries to maintain a fixed distance from the box. Moving the box back and forth causes the robot to move back and forth. We will use the blocks from the `action` category for this exercise. These blocks allow you to have the robot move forward or backward and turn. These blocks assume you have connected the motors to the correct motor ports (Left motor to M1 and Right motor to M2). If you notice the robot moving in the opposite direction you ask it to move, you have probably swapped the motor connectors. As always, there are different solutions. The program below is one possible solution.

![The distance challenge in action. The robot holds its distance from the box; moving the box along the arrow makes the robot follow it.](images/programming-the-robot-e395427b.jpg)

This program works as follows. At the program's start, we read the nearest object's distance and store it in a variable `preferred_distance` (see step 1). Next, we repeat several steps forever. We read the current distance (and store the value in the variable `current_distance`) and calculate the difference with `preferred_distance`. If the absolute value of the difference is smaller than 2 cm (step 3), we stop the robot (step 6). In this case, we do not move the robot. If `abs(difference) > 2`, we must move the robot. If `difference < 0`, we are too close to the object and switch on the motors to move backward. If `difference > 0`, we move forward. This way, the robot will try to keep at `preferred_distance` from the obstacle. Remember, to create this program, you will need to make the blocks for the variables `difference`, `current_distance` and `preferred_distance` as discussed above (See [Working with variables in mBlock](#working-with-variables-in-mblock) )

Moving the box in the picture back and forth causes the robot to move back and forth. It tries to maintain a fixed distance from the box.

In this program, we tolerate an error of 2 cm. You can experiment with lower values. However, you will notice that the program will become unstable at some point: the robot will never stop and oscillate back and forth. This is because the distance read by the sonar is noisy. Also, the program has some delay between moving and getting updated distance values. Even if the sonar were noise-free, this delay would cause some oscillation.

![One solution to the distance challenge. (1) The starting distance is stored in `preferred_distance`. Then, on every pass: (2) the current distance is read and the difference worked out, (3) the difference is tested against a tolerance of 2 cm, (4) the robot moves forward if it is too far away, (5) backward if it is too close, and (6) stops if it is near enough. The numbers appear again in the description below.](images/programming-the-robot-55d3603f.png)
