# Getting started with the robot

## Accessing mBlock

This guide assumes you already have access to **mBlock**, the software used to program the robot — either running in your browser or installed on your computer. If you do not, work through Installing mBlock first, then come back here.

The two links below take you straight to the online editor and to the installation instructions.

### mBlock in the browser

- No installation is required
- You can access mBlock through the link below:

[mBlock Block-Based IDE- Coding for Beginners](https://ide.mblock.cc/)

### mBlock installed on your computer

- This option is only available for Windows and Mac.
- mBlock installation instructions for Windows and Mac are available below:

[Install mBlock 5 on Windows and macOS](https://support.makeblock.com/hc/en-us/articles/14779090584599-Install-mBlock-5-on-Windows-and-macOS)

## Preliminary Information

> **Note**
>
> Please read through this preliminary information before moving on. This section contains important information to help you understand and work more efficiently with the robot.

### Connection options

To program and control your mBot, you need to connect it to your computer. There are two ways to establish a connection:

1. **Using the Bluetooth Dongle:** A wireless connection using a Makeblock Bluetooth dongle.
2. **Using a USB Cable:** A wired connection between your computer and the robot.

Older mBots could also be connected using a 2.4 GHz module and dongle, or over direct Bluetooth. We do not support either. Makeblock has discontinued the 2.4 GHz hardware, and with direct Bluetooth every robot in a classroom presents the same address, so students cannot tell which robot they are connecting to.

![The Bluetooth Dongle that can be used to connect to the robot.](images/getting-started-draft-6fb3632a.png)

![The USB cable that can be used to connect to the robot.](images/getting-started-draft-dd60485a.png)

### Pairing the Bluetooth dongle and the robot

> **Note**
>
> In a classroom setting with multiple robots, it is advisable to pair each Bluetooth dongle with a specific robot. This ensures that the computer or device to which the dongle is inserted will connect to that robot. Below, we provide instructions for this setup. You should only have to do this once for each robot.

1. Turn off all robots except the one you want to pair with a dongle. The robot's blue LED will start blinking, as shown in the image below.
2. Insert the dongle into a computer and press its Bluetooth symbol. The symbol will flash rapidly. The unpaired robot and the dongle will now pair.
3. When pairing is complete, both the robot's LED and the dongle's symbol will stop blinking. See the image below.
4. Label both the robot and dongle as a paired set. The dongle will now only connect to this specific robot, and labels make it easy to identify which dongle belongs to which robot.
5. To pair additional robots, repeat these steps with each robot-dongle pair.

> **Note**
>
> If a student presses the dongle’s button, it will return to pairing mode. Therefore, you should stress that students should not press the button when working with the robot. It might be a good idea to put some tape over the button to reduce the chance of a student pressing it.

![Blue LED blinking on the robot’s Bluetooth module.](images/getting-started-draft-1f093a0d.jpg)

![When the dongle and the robot are paired, the blue LEDs on both will stop blinking.](images/getting-started-draft-f62edb5b.jpg)

### Adding the mBot to mBlock

When you start creating programs from scratch, you must add the robot to mBlock to access the correct block to write programs. This is not needed if you use or start from our programs.

Look at the `Devices` area in mBlock. If the mBot is not listed in this area (like in the left image below), you must first add it. To do so, click the `Add (+)` button in the window's device area (left bottom corner. See also image below). This will allow you to select multiple devices (See image below). In the window listing the devices, select mBot (**not mBot2**) and click `OK`. The mBot has now been added (see the right image below).

![Click this button to add the robot to mBlock.](images/getting-started-draft-c19638ac.png)

![The devices area before adding the mBot.](images/getting-started-draft-bcbd96a0.png)

![Select the mBot from the menu.](images/getting-started-draft-f2ecdd41.png)

![The devices area after adding the mBot.](images/getting-started-draft-7bfc097d.png)

### Live versus Upload mode

When programming your mBot, you can run your code in **Live Mode** or **Upload Mode**.

The short version: **use Live Mode for everything except the Color Vision lesson.** Live Mode lets you watch sensor readings and variable values as the program runs, which is what makes the robot useful for teaching. The one exception is the color sensor, which mBlock does not support in Live Mode — so the Color Vision lesson has to use Upload Mode. The cost of that is that the robot's firmware gets overwritten, and you have to reset it before the robot can be used in Live Mode again. That reset is described below.

**Live Mode**

In Live Mode, the mBot remains connected to your computer using the Bluetooth dongle or USB cable, and commands are sent to the robot in real time. The robot responds instantly when you run a program. You can test and modify your code quickly without uploading it. You can see sensor values and variables updating in real time in mBlock.

**Upload Mode**

In Upload Mode, the program is stored directly on the mBot. The robot can run the program independently without being connected to a computer. After uploading, you can unplug the Bluetooth Dongle or USB, and the robot will still follow the programmed instructions. However, you cannot see live sensor values or make real-time adjustments in this mode. If you want to change the program, you must upload it again.

> **Important**
>
> All programs we provide are meant to be run in Live mode, except for the programs for the Color Vision module. The color sensor is not compatible with Live mode. Therefore, programs using this sensor need to be run using  Upload mode.

**Switching from Upload to Live mode**

Once you have used the Upload mode, reset the robot's firmware to use the Live mode again. Instructions on how to do this are given below: [Resetting the firmware](#getting-started-with-the-robot)

> **Why?**
>
> Why must you reset the firmware to switch from Upload to Live mode? In Live mode, the robot runs a small program whose only job is to talk to the computer — Makeblock calls this the **Online firmware**. When you use Upload mode, your own program replaces it. Resetting the firmware puts the Online firmware back, which is what restores Live mode. (Makeblock's own documentation refers to this as *updating* the firmware, which is the wording you will see in mBlock.)

## Connecting to the robot

### Requirements

Before attempting to connect to the robot, ensure the following:

1. You can access mBlock through the browser or installed on your computer. See above for instructions: [Accessing mBlock](#getting-started-with-the-robot)
2. You have decided to connect using the USB cable or the Bluetooth dongle. See above for information on these two ways to connect to the robot: [Connection options](#getting-started-with-the-robot)
3. If you use the Bluetooth dongle, ensure the dongle is paired with the robot. Instructions on this are listed above: [Pairing the Bluetooth dongle and the robot](#getting-started-with-the-robot) 
4. Make sure you have added the mBot to mBlock. See instructions on this here: [Adding the mBot to mBlock](#getting-started-with-the-robot)

### Connecting to the robot using mBlock in the browser

> **Note**
>
> These instructions are for connecting to the robot when running mBlock in the browser. If you use a locally installed version of mBlock, please refer to the correct instructions below.

Below is a screenshot of mBlock running in the browser. Note that the mBot has been added to the program.

![](images/getting-started-draft-6bb9e606.png)

#### Using the Bluetooth dongle

- Switch on the robot and plug the corresponding, paired dongle into the computer or device running mBlock. The Bluetooth symbol on the dongle should light up (steady). The blue light on the robot should flash for a few seconds. Once the LED turns steady, the robot is connected to the dongle.
- In mBlock, ensure you have switched to Direct Connection. If mBlock shows the option to `Switch to direct connection` (like in the image below), click it.

![](images/getting-started-draft-1dd0fc6c.png)

- Click `Serial` to connect to the robot. This is somewhat confusing. The dongle uses Bluetooth technology, and it has a Bluetooth icon on it. However, the Bluetooth dongle sets up a serial connection; therefore, we must select `Serial` from this menu.
- This will bring up a window allowing you to choose the device you want to connect to the robot. If the Bluetooth dongle is correctly detected, you can select this and click `Connect`

![](images/getting-started-draft-bd535d8d.png)

![](images/getting-started-draft-42631685.png)

#### Using the USB cable

Connecting to the robot using the USB cable and the online version of mBlock is identical to the dongle instructions. However, instead of plugging the dongle into the computer, you use the USB cable to connect the robot to the computer. Just as for when using the dongle, you select the serial connection option.

### Connecting to the robot using locally installed mBlock

> **Note**
>
> These instructions are for connecting to the robot when running mBlock installed locally on your computer. If you use mBlock in the browser, please refer to the correct instructions above.

Below is a screenshot of mBlock running locally on Windows. Note that the mBot has been added to the program.

![](images/getting-started-draft-45dbe002.png)

#### Using the Bluetooth dongle

- Switch on the robot and plug the corresponding, paired dongle into the computer or device running mBlock. The Bluetooth symbol on the dongle should light up (steady). The blue light on the robot should flash for a few seconds. Once the LED turns steady, the robot is connected to the dongle.
- In mBlock, click connect.

![](images/getting-started-draft-230537db.png)

- This will give you a window to choose how you want to connect to the robot. In this window, select `USB`. This is somewhat confusing. The dongle uses Bluetooth technology and has a Bluetooth icon on it. Yet, we must choose USB since the dongle sets up a (virtual) serial connection. If the dongle is correctly identified, you will notice that the window dropdown box is populated with a (serial port). Click `Connect` in this window to connect to the robot.

![](images/getting-started-draft-e90f8ba9.png)

## Uploading a program to the robot

Most of our programs run in Live mode, so you will not normally need this. The exception is the Color Vision lesson, whose programs have to be uploaded because the color sensor does not work in Live mode.

1. Make sure the program starts with the `when mBot (mcore) starts up` block rather than `when flag clicked`. An uploaded program runs when the robot is switched on, so it needs that starting block.
2. Use the toggle to switch mBlock to `Upload` mode.
3. Connect to the robot as described above, then click `Upload`.

The program is compiled and transferred to the robot. Switch the robot off and on again to start it. To upload a changed program, repeat these steps.

Once you have uploaded a program, the robot cannot be used in Live mode again until you reset its firmware. That is covered in the next section.

## Resetting the firmware

Before running your first program, you may need to reset the mBot's firmware. As explained in the section [Live versus Upload mode](#getting-started-with-the-robot), running a program in **Live Mode** requires the mBot to have its standard firmware (pre-installed onboard software).

Resetting the firmware is not necessary in most cases. However, if you suspect someone has previously used the mBot in **Upload Mode**, its firmware may have been overwritten. To ensure compatibility with Live Mode, reset the firmware before running your first program.

To reset the firmware, connect the robot to your computer using the USB cable. Then click `Setting`, followed by `Update Firmware`. In the pop-up that appears, click `Updates`. The firmware will be reset, and once it has finished the robot can be used in `Live` mode again.

You do **not** need to switch between `Live` and `Upload` mode first.

![Use the slider to switch the software to `Live` mode.](images/getting-started-draft-bf1a09ed.png)

![Select `Update Firmware`.](images/getting-started-draft-8aa4d6fa.png)

![Click `Updates`.](images/getting-started-draft-05ea3950.png)

## Running your first program

### Step 1: Open the example program

As part of our lesson plans, we've included several example programs for the robot. We'll run one of these programs to help familiarize you with using our example programs. All our programs are uploaded to the mBlock website, and the instructions for using them are similar across all programs.

Start by navigating to the test program on the mBlock website:

[MyFirstProgram](https://planet.mblock.cc/project/3934903) — or [download `MyFirstProgram.mblock` directly](https://drive.google.com/file/d/1XCEIlMv4KOro7h_ZQQajJ_j_5QhLtC34/view?usp=sharing) if your school blocks the Makeblock site.

This should bring up the webpage shown in the screenshot below.

![](images/getting-started-draft-0e4e97c5.png)

Next, click on `Source Code`. This will show the program in the online version of mBlock, as shown in the screenshot below.

![](images/getting-started-draft-390bb096.png)

You can run the program using this online version or download it to your computer. To download the program, use the file menu: `File > Save to your computer`.

> **Tip**
>
> You can also download the program to your computer by clicking `File` and selecting `Save to my computer`. This allows you to open and edit the program if you have installed mBlock on your computer (windows and Mac only. Chromebooks need to use the online version of mBlock)

### Step 2: Connect to the robot in Live mode

Use the instructions to connect to the robot provided above using either the Bluetooth dongle or the USB cable. Ensure you have switched on the Live mode in mBlock. If you are connected to the robot and have switched to Live mode, you can click the green flag to start the program.

![Make sure Live mode is selected.](images/getting-started-draft-65345555.png)

![Once you have connected to the robot, you can run the program by clicking the green flag.](images/getting-started-draft-d0b359dd.png)

The program is very simple. It sets the robot’s LED light to blue for a second, then to green. This is repeated indefinitely. If you see the lights on the robot flashing blue and green, you have successfully run your first program. You can now edit the program by adding more blocks and rerunning it.

![](images/getting-started-draft-40ce24ad.png)
