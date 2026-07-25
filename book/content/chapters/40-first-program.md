# Running your first program

Once mBlock is working and you can connect to the robot, it is worth running a small example program before anything else. It tests the whole chain — software, connection, robot — in a couple of minutes, and it introduces the pattern that every lesson uses to open its own programs.

> **Note**
>
> Work through [Installing mBlock](#installing-mblock) and [Connecting to the robot](#connecting-to-the-robot) first.

## Step 1: Open the example program

Our lesson plans come with several example programs for the robot. We will run one of them here, so that the pattern is familiar when a lesson asks you to open another.

We publish every program in two places: on the mBlock website, and as a file in our own repository. They are the same program — the second copy is there for schools whose network blocks the Makeblock site. Each lesson gives you both links, in the form you see just below.

[MyFirstProgram](https://planet.mblock.cc/project/3934903) — or [download `MyFirstProgram.mblock` directly](files/programs/MyFirstProgram.mblock) if your school blocks the Makeblock site.

The two routes differ from here on.

**From the mBlock website.** The link opens the project page shown below. Click `Source code`, and the program opens in the online version of mBlock.

![The project page on the mBlock website. Click `Source code` to open the program.](images/getting-started-draft-0e4e97c5.png)

![The program open in the online version of mBlock.](images/getting-started-draft-390bb096.png)

**From the downloaded file.** There is no project page on this route. Open mBlock, choose `File > Open from my computer`, and select the `.mblock` file you downloaded. The program opens straight away.

Either way, you can keep your own copy of the program. `File > Save to my computer` writes it out as an `.mblock` file, and `File > Open from my computer` opens it again later. Both work the same way in the browser and in the installed version, so a copy you save on one will open on the other.

## Step 2: Connect to the robot in Live mode

Connect to the robot with either the Bluetooth dongle or the USB cable, as described in [Connecting to the robot](#connecting-to-the-robot), and make sure mBlock is set to `Live` mode. If the robot has been used in Upload mode before, reset its firmware first — see [Resetting the firmware](#resetting-the-firmware).

![Make sure `Live` mode is selected.](images/getting-started-draft-65345555.png)

With the robot connected and Live mode selected, click the green flag to start the program. The red button beside it stops the program again.

![The green flag starts the program; the red button beside it stops it.](images/running-your-first-program-752f3ce5.png)

## What the program does

The program is very simple. It sets the robot's LED lights to blue for a second, then to green, and repeats that indefinitely. If you see the lights on the robot flashing blue and green, you have successfully run your first program, and the software, the connection and the robot are all working.

![MyFirstProgram: the robot's LEDs alternate between blue and green, a second each, for as long as the program runs.](images/getting-started-draft-40ce24ad.png)

You can now edit the program by adding more blocks and running it again. [Introduction to Programming](#introduction-to-programming) and [Programming the robot](#programming-the-robot) take that further.
