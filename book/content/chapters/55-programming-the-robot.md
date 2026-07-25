# Programming the robot

> **Tip**
>
> This brief introduction to mBlock assumes you (and the students) have installed mBlock on the computer or have access to mBlock online. Please see [our guide on this topic here](#installing-mblock). We also assume you (and the students) understand how to connect to the robot. Our [guide on connecting to the robot can be found here](#getting-started-with-the-robot). We also assume that you (and the students) have successfully run a first test program to ensure the robot is connected to the computer. If not, [the guide can be found here](#running-your-first-program).

This lesson is intended to introduce students to programming the mBot robot. The mBot can be programmed using the mBlock programming language. This is a visual programming language. In contrast to most programming languages, users write a program by manipulating elements graphically instead of typing text. While visual programming languages are often considered simpler, many examples of specialized visual programming languages are used in engineering and science. Therefore, depending on the context, visual programming languages can be compelling alternatives to text-based programming.

In this guide, we present four quite simple programming challenges you can present to the students to familiarize themselves with programming the robot. Before listing the challenges, we provide an introduction to mBlock. We cover the interface, where to find blocks to create programs, and how to work with variables. We also explain the basic structure of most programs. In our experience, this can be covered quite quickly with students as they usually find out these things quickly.

> **Tip**
>
> This unit was created collaboratively with faculty from the University of Cincinnati College of Arts and Sciences, College of Engineering, and School of Education. Combining biology with engineering activities gives students a unique opportunity to understand the parallels between animal and robot behavior and sensory/sensor function. It addresses broad Next Generation Science Standards (NGSS Lead States, 2013) and International Society for Technology in Education Standards (International Society for Technology in Education, 2022).

## Materials

| Item | Description |
| :--- | :--- |
| mBot Robot | The mBot robot |
| Bluetooth Dongle | This is a dongle that allows to connect to the robot from a computer. This is currently the recommended way to work with the robot. |
| Makeblock Sound Sensor | Sensor reading the current sound intensity. Used in the sound localization plan and the intro to programming. |
| Extra motors | Motors seem to be a component that fails from time to time. Students should be provided with replacement motors |
| Extra cables (short) | Extra cables for connecting sensors. This allows students to add sensors without removing cables and covers for losing cables.  The cables come in a pack of 4. I suggest supplying 1 extra cable per robot.  This cable is 20 cm long and has the same length as the 2 cables that come with the robot. |
| Gaffers tape | It’s tape. What else can I say. I comes in handy everywhere. |
| Batteries | The robot takes 4 AA batteries. These should last a while. This is a 100 pack of AA batteries Providing more than 8 batteries per robot should allow swapping out the batteries and getting new stock without interruption to the curriculum. |

## Prerequisites

Algebra I

## Investigating/Essential Questions

- How can instructions be written so that a computer understands them?
• How can a robot be controlled through programming?

## Educational Standards

The educational standards applicable to this lesson are listed in the [Educational standards](#educational-standards) chapter.

## Learning objectives

1. Students will write algorithms.
2. Students will use computational thinking to design solutions.
3. Students will learn to use a visual programming language.
4. Students will be able to write basic programs that control a robot’s actions.
5. Students will develop, test, and refine prototypes.

## Getting started with mBlock

As mentioned in a previous guide, mBlock is the software we will use to program the robot. Below, we cover some basic aspects of mBlock to help you get started writing programs for the robot.

### Explore the mBlock interface

Below, we show the mBlock interface. The interface looks very similar regardless of whether you use the installed program or the online version. We explain the use for each region in the interface below.

1. This area is used for constructing a program. You will drag and drop blocks onto this field to form a program.
2. This window area lists the blocks that can be used to create a program. The blocks are organized into categories such as [Sensing] and [Control]. To use a block, you drag and drop it to area (1). Notice the [extension] button at the bottom of this area (2). Additional blocks can be added by installing extensions.
3. This part of the screen shows the values of variables in a program. This information is useful when trying to figure out why a program does not work as expected.
4. Here, the robots for which blocks are available are listed. When the program first starts, the mBot is not listed, which means we have to load it. We have [explained how to do this here](#getting-started-with-the-robot).

![](images/programming-the-robot-111bd9e8.png)

### Useful blocks

The mBlock interface provides many blocks, organized in multiple categories. Below, we briefly introduce the blocks found in each category. Note that mBlock color codes the groups. This makes it easier to find the blocks we use in the programs in the lesson plans.

1. Looks: These blocks are only relevant if you equip the robot with an LCD (sold separately). For
our purposes, this category is irrelevant.
2. Show: Here, you can find blocks that control the robot's onboard LEDs. You can also use these
blocks to make the robot play tones.
3. Action: These blocks control the motors. In other words, these blocks make the robot move.
4. Sensing: This category lists special blocks that allow you to get the sensors' state and set the
motor speeds. Blocks for reading additional sensors can be installed as extensions.
5. Events: From this category, you will most likely only use the `when flag is clicked` block. This block indicates the start of a program.
6. Control: This category consists of blocks that allow you to repeat parts of a program, execute
part of the program depending on a condition (if ... then ...), or pause the program for a small amount of time.
7. Operators: This category contains some blocks allowing you to perform simple math and
comparisons.
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

![](images/programming-the-robot-658b06bf.png)

### Working with variables in mBlock

Solving the next challenge will require using a variable. Therefore, this is a good time to introduce students to variable use.

The technical definition of a variable is a named container that stores a value. It can hold different types of information, such as numbers, strings, or Boolean values. Variables allow you to keep track of and manipulate data within your project. However, more intuitively (and practically), they are labels that can be assigned values (including the values returned by the sensors) such that they can be reused later in the program.

Before using a variable, you must define (or “make”) it. In mBlock, you can create variables by clicking the `variables` menu and then clicking `Make a Variable`. See the images below for an illustration. This will bring up a window where you can enter the name of your new variable. The name of the variable is arbitrary. However, it’s usually a good idea to give the variable a name you can remember and has some connection to what you wish to use the variable for. In this introduction to variables, we will create a simple program that counts to 10. Therefore, we will name our variable `count`. Once you have created a variable, a block with that name will be created under the `variables` menu.

![Step 1: select the category `variables`.](images/programming-the-robot-496da0e0.png)

![Step 2: Click `make a variable`.](images/programming-the-robot-4703540e.png)

![Step 3: choose a name for your variable.](images/programming-the-robot-32dcbd91.png)

![Step 4: use the new blocks.](images/programming-the-robot-f6a631e9.png)

Now, we can use our newly created variable in a simple program (that does not involve the robot but demonstrates the use of a variable). Even though the program does not use the robot’s sensors or motors, you will need to connect to the robot to run it (otherwise, the program will not run).

The program starts by setting the variable `count` to zero. Then, it increases the value of `count` by 1 before waiting a second and repeating this. Once the value of `count` is larger than 10, `count` is reset to zero.

![](images/programming-the-robot-292d0d09.png)

![](images/programming-the-robot-43ff905e.png)

> **Note**
>
> The green block can be found under `Operators`. To add the `count` block inside the green block, go to `Variables` and drag the `count` block to the left hand hole in the green block.

> **Tip**
>
> You can make as many variables as you need for a program. Also, the current values of all variables are displayed in the panda window. A picture of this window is shown below.

## Programming challenges

The topics covered above should prepare the students to address the following challenges.

### Challenge 1: Blinking the LEDs

> Challenge: Construct a program that switches on the onboard LEDs for a second and turns them off for a second.
>

In this challenge, students will construct a program to make the onboard LEDs of the robot blink. Blinking LEDs is a prevalent first example in tutorials about programming hardware. Here, we adhere to this tradition.  An example program is below.

The program below repeatedly sets the value of the onboard LEDs to red. Then, it waits for a second before switching the LEDs off (turning their color to black). Next, the program pauses for a second before repeating this cycle. This program's backbone consists of the `when flag is clicked` and `forever` blocks.

![](images/programming-the-robot-2224f883.png)

### Challenge: Reading a sensor

> Challenge: Construct a program that briefly blinks the onboard LEDs when the onboard light sensor registers a value smaller than 500.
>

The robot has an onboard light intensity sensor. The sensor gives a value from 0 to 1000, depending on the light's intensity falling on the sensor. In this example, we will use this sensor to program the robot to do the following:

1. Read the onboard light sensor and store the result in a variable.
2. If the light value is smaller than 500, blink the lights briefly.

The program below is one solution to this challenge. The program starts by switching the LEDs to ensure they are off at the program's start. Next, the program repeatedly reads the value of the onboard light sensor. If the sensor (stored in the variable `light`) is smaller than 500, the program switches on and off the onboard LEDs.

![](images/programming-the-robot-efc4bf9d.png)

### Challenge: Sound Detection

> Challenge:  Construct a program that blinks the LEDs if the sound is louder than a set value. The duration of the LEDs' blink should depend on the loudness of the sound.
>

For this activity, we will connect a single sound sensor to the robot using a cable. An example of a robot equipped with a sound sensor is shown below.

![A single sound sensor is attached to the robot and taped to the top of the robot.](images/programming-the-robot-1dea6db5.jpg)

#### Adding the sound sensor to mBlock

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
duration = (loudness – min) / 50
$$

With `min` set to 200. This program should respond to noise: louder noises result in a longer blink of the LEDs.

![](images/programming-the-robot-d2e74147.png)

### Challenge: Keeping your Distance

The following programming challenge will use the motors. Using the sonar sensor, we will program the robot to maintain a fixed distance from an object. When starting the program, the robot will read the distance to the nearest object (detected by the sonar). Next, the robot will move forward if the distance increases and backward if the distance decreases.

> Challenge: Program the robot to keep a fixed distance from an object in front of the sonar.
>

Below is an example of this challenge in action. The robot tries to maintain a fixed distance from the box. Moving the box back and forth causes the robot to move back and forth. We will use the blocks from the `action` category for this exercise. These blocks allow you to have the robot move forward or backward and turn. These blocks assume you have connected the motors to the correct motor ports (Left motor to M1 and Right motor to M2). If you notice the robot moving in the opposite direction you ask it to move, you have probably swapped the motor connectors. As always, there are different solutions. The program below is one possible solution.

![](images/programming-the-robot-e395427b.jpg)

This program works as follows. At the program's start, we read the nearest object's distance and store it in a variable `preferred distance` (see step 1). Next, we repeat several steps forever. We read the current distance (and store the value in the variable `current_distance`) and calculate the difference with the `preferred distance`. If the absolute value of the difference is smaller than 2 cm (step 3), we stop the robot (step 6). In this case, we do not move the robot. If `abs(difference) > 2`, we must move the robot. If the `difference is < 0`, we are too close to the object and switch on the motors to move backward. If the `difference is> 0`, we move forward. This way, the robot will try to keep at a distance `preferred distance` from the obstacle. Remember, to create this program, you will need to make the blocks for the variables `difference`, `current distance` and `preferred distance` as discussed above (See [Working with variables in mBlock](#working-with-variables-in-mblock) )

Moving the box in the picture back and forth causes the robot to move back and forth. It tries to maintain a fixed distance from the box.

In this program, we tolerate an error of 2 cm. You can experiment with lower values. However, you will notice that the program will become unstable at some point: the robot will never stop and oscillate back and forth. This is because the distance read by the sonar is noisy. Also, the program has some delay between moving and getting updated distance values. Even if the sonar were noise-free, this delay would cause some oscillation.

![](images/programming-the-robot-55d3603f.png)
