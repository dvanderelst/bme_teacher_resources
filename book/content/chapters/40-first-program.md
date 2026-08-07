# Running your first program

Once mBlock is working and you can connect to the robot, run a small example program first. This program verifies the entire setup (software, connection, and robot) in a couple of minutes. It also introduces the pattern used throughout the lessons for opening programs.

> **Note**
>
> First complete [Installing mBlock](#installing-mblock) and [Connecting to the robot](#connecting-to-the-robot).

## Step 1: Open the example program

Our lesson plans include example programs for the robot. Running one now familiarizes you with the pattern used to open programs in each lesson.

Each program is available in two locations: on the mBlock website and as a file in our repository. Both are identical; the repository copy is provided for schools that block the Makeblock site. Each lesson provides both links, as shown below.

[Open the mBlock project](https://planet.mblock.cc/project/3934903). If your school blocks the Makeblock site, [download `MyFirstProgram.mblock`](files/programs/MyFirstProgram.mblock) instead.

The two methods differ from this point:

- **From the mBlock website.** The link opens the project page shown below. Click `Source code`, and the program opens in the online version of mBlock.

  ![The project page on the mBlock website. Click `Source code` to open the program.](images/getting-started-draft-0e4e97c5.png)

  ![The program open in the online version of mBlock.](images/getting-started-draft-390bb096.png)

- **From the downloaded file.** No project page appears. Open mBlock, select `File > Open from your computer`, and choose the downloaded `.mblock` file. The program opens directly.

In either case, you can save your own copy. Use `File > Save to your computer` to save as an `.mblock` file, and `File > Open from your computer` to reopen it later. Both options work identically in browser and installed versions, so files saved in one open in the other.

## Step 2: Connect to the robot in Live mode

Connect to the robot using either the Bluetooth dongle or USB cable, as described in [Connecting to the robot](#connecting-to-the-robot). Ensure mBlock is in `Live` mode. If the robot was previously used in Upload mode, reset its firmware first. See [Resetting the firmware](#resetting-the-firmware).

![Ensure `Live` mode is selected.](images/getting-started-draft-65345555.png)

Once connected in Live mode, click the green flag to start the program. The adjacent red button stops it.

![The green flag starts the program; the red button stops it.](images/running-your-first-program-752f3ce5.png)

## What the program does

The program is simple: it cycles the robot's LED lights between blue and green, holding each color for one second. If you see the LEDs flashing blue and green, you have successfully run your first program. This confirms the software, connection, and robot all work.

![MyFirstProgram: the robot's LEDs alternate between blue and green, one second each, for as long as the program runs.](images/getting-started-draft-40ce24ad.png)

You can now edit the program by adding blocks and re-running it. For more, see [Introduction to Programming](#introduction-to-programming) and [Programming the robot](#programming-the-robot).
