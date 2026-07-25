# Getting started with the robot

This chapter assumes you already have **mBlock**, the software used to program the robot, either running in your browser or installed on your computer. If you do not, work through [Installing mBlock](#installing-mblock) first and then come back here.

## Connection options

To program and control your mBot, you need to connect it to your computer. There are two ways to do that:

1. **Using the Bluetooth dongle.** A wireless connection using a Makeblock Bluetooth dongle, shown in the first image below.
2. **Using a USB cable.** A wired connection between your computer and the robot, using the cable shown in the second image.

Older mBots could also be connected using a 2.4 GHz module and dongle, or over direct Bluetooth. We do not support either. Makeblock has discontinued the 2.4 GHz hardware, and with direct Bluetooth every robot in a classroom presents the same address, so students cannot tell which robot they are connecting to.

![The Bluetooth dongle that can be used to connect to the robot.](images/getting-started-draft-6fb3632a.png)

![The USB cable that can be used to connect to the robot.](images/getting-started-draft-dd60485a.png)

## Pairing the Bluetooth dongle and the robot

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
> If a student presses the dongle's button, it will return to pairing mode. Therefore, you should stress that students should not press the button when working with the robot. It might be a good idea to put some tape over the button to reduce the chance of a student pressing it.

![Blue LED blinking on the robot's Bluetooth module.](images/getting-started-draft-1f093a0d.jpg)

![When the dongle and the robot are paired, the blue LEDs on both will stop blinking.](images/getting-started-draft-f62edb5b.jpg)

## Checking whether a dongle and a robot are paired

Labels come off, and after a term of use you may not trust the ones that are left. You can check a pair without opening mBlock at all, using the fact that a paired device starts blinking as soon as it loses its partner.

1. Switch the robot on and plug the dongle in. Both should settle to a **steady** blue light. If either keeps blinking, they are not paired with each other.
2. Unplug the dongle. After a few seconds the robot's blue light starts **blinking** — it has lost its partner.
3. Plug the dongle back in. Both should go steady again.
4. Now switch the robot off. After five to ten seconds the dongle's light starts **blinking**.

If breaking the pair from either end makes the other one blink, the two belong together and you can relabel them with confidence. If a light never settles in the first place, or stays steady once its partner is gone, pair them again as described above.

## Adding the mBot to mBlock

When you start creating programs from scratch, you must add the robot to mBlock to access the correct block to write programs. This is not needed if you use or start from our programs.

Look at the `Devices` area in mBlock. If the mBot is not listed in this area (like in the left image below), you must first add it. To do so, click the `Add (+)` button in the window's device area (left bottom corner. See also image below). This will allow you to select multiple devices (See image below). In the window listing the devices, select mBot (**not mBot2**) and click `OK`. The mBot has now been added (see the right image below).

![Click this button to add the robot to mBlock.](images/getting-started-draft-c19638ac.png)

![The devices area before adding the mBot.](images/getting-started-draft-bcbd96a0.png)

![Select the mBot from the menu.](images/getting-started-draft-f2ecdd41.png)

![The devices area after adding the mBot.](images/getting-started-draft-7bfc097d.png)

## Live versus Upload mode

When programming your mBot, you can run your code in **Live mode** or **Upload mode**.

> **The short version**
>
> Use Live mode for everything except the Color Vision lesson. Live mode lets you watch sensor readings and variable values as the program runs, which is what makes the robot useful for teaching. The color sensor is the one exception: mBlock does not support it in Live mode, so the Color Vision programs have to be uploaded. The cost of that is that the robot's firmware gets overwritten, and you have to reset it before the robot can be used in Live mode again.

**Live mode**

In Live mode, the mBot remains connected to your computer using the Bluetooth dongle or USB cable, and commands are sent to the robot in real time. The robot responds instantly when you run a program. You can test and modify your code quickly without uploading it. You can see sensor values and variables updating in real time in mBlock.

**Upload mode**

In Upload mode, the program is stored directly on the mBot. The robot can run the program independently without being connected to a computer. After uploading, you can unplug the Bluetooth dongle or USB cable, and the robot will still follow the programmed instructions. However, you cannot see live sensor values or make real-time adjustments in this mode. If you want to change the program, you must upload it again.

**Switching from Upload back to Live mode**

Once you have used Upload mode, reset the robot's firmware to use Live mode again. This is described in [Resetting the firmware](#resetting-the-firmware).

> **Why?**
>
> Why must you reset the firmware to switch from Upload to Live mode? In Live mode, the robot runs a small program whose only job is to talk to the computer — Makeblock calls this the **Online firmware**. When you use Upload mode, your own program replaces it. Resetting the firmware puts the Online firmware back, which is what restores Live mode. (Makeblock's own documentation refers to this as *updating* the firmware, which is the wording you will see in mBlock.)

## Connecting to the robot

### Requirements

Before attempting to connect to the robot, ensure the following:

1. You have mBlock, either in the browser or installed. See [Installing mBlock](#installing-mblock).
2. You have decided whether to connect using the USB cable or the Bluetooth dongle. See [Connection options](#connection-options).
3. If you use the Bluetooth dongle, ensure the dongle is paired with the robot. See [Pairing the Bluetooth dongle and the robot](#pairing-the-bluetooth-dongle-and-the-robot).
4. Make sure you have added the mBot to mBlock. See [Adding the mBot to mBlock](#adding-the-mbot-to-mblock).

### Using mBlock in the browser

> **Note**
>
> These instructions are for connecting to the robot when running mBlock in the browser. If you use a locally installed version of mBlock, please refer to the correct instructions below.

![mBlock running in the browser, with the mBot already added to the `Devices` panel.](images/getting-started-draft-6bb9e606.png)

#### Direct connection or mLink?

The browser version of mBlock can reach the robot in two different ways, and a link at the top of the `Devices` panel switches between them.

- **Direct connection.** The browser talks to the robot itself. Nothing extra has to be installed, but it only works in Chrome and Chromium.
- **mLink.** The small helper program described in [Installing mBlock](#installing-mblock) does the talking instead. This is the route for browsers that cannot do the job themselves.

**The instructions below use the direct connection**, because it is the simpler of the two and needs nothing installed — which matters on school computers that are locked down. So if the `Devices` panel offers `Switch to direct connection`, click it. If it offers `Switch to mLink`, you are already using the direct connection and there is nothing to do.

![If the panel offers `Switch to direct connection`, click it.](images/getting-started-draft-1dd0fc6c.png)

#### Using the Bluetooth dongle

- Switch on the robot and plug the corresponding, paired dongle into the computer or device running mBlock. The Bluetooth symbol on the dongle should light up (steady). The blue light on the robot should flash for a few seconds. Once the LED turns steady, the robot is connected to the dongle.
- Make sure mBlock is set to the direct connection, as described above.
- Click `Serial`. This is confusing the first time: the dongle is a Bluetooth device and has a Bluetooth symbol printed on it, but it presents itself to the computer as a serial port. So `Serial` is the right choice here and `Bluetooth` is not.
- The browser now asks which serial port you want to use. Select the entry for the dongle and click `Connect`.

![With the direct connection selected, click `Serial` — not `Bluetooth`, even though the dongle is a Bluetooth device.](images/getting-started-draft-bd535d8d.png)

![The browser asks which serial port to use. Select the dongle and click `Connect`.](images/getting-started-draft-42631685.png)

#### Using the USB cable

Connecting over the USB cable works in exactly the same way. Plug the cable in instead of the dongle, leave mBlock on the direct connection, and choose `Serial` as above. The only difference is which port appears in the browser's dialog.

### Using locally installed mBlock

> **Note**
>
> These instructions are for connecting to the robot when running mBlock installed locally on your computer. If you use mBlock in the browser, please refer to the correct instructions above.

The choice between a direct connection and mLink does not arise here. A locally installed mBlock talks to the robot itself, so there is no helper program and no connection mode to pick.

![mBlock installed on Windows, with the mBot already added to the `Devices` panel.](images/getting-started-draft-45dbe002.png)

#### Using the Bluetooth dongle

- Switch on the robot and plug the corresponding, paired dongle into the computer or device running mBlock. The Bluetooth symbol on the dongle should light up (steady). The blue light on the robot should flash for a few seconds. Once the LED turns steady, the robot is connected to the dongle.
- In mBlock, click `Connect`.

![In the installed version, click `Connect`.](images/getting-started-draft-230537db.png)

- This will give you a window to choose how you want to connect to the robot. In this window, select `USB`. This is somewhat confusing. The dongle uses Bluetooth technology and has a Bluetooth icon on it. Yet, we must choose USB since the dongle sets up a (virtual) serial connection. If the dongle is correctly identified, you will notice that the window dropdown box is populated with a (serial port). Click `Connect` in this window to connect to the robot.

![Choose the `USB` tab, check that a port is listed in the dropdown, and click `Connect`.](images/getting-started-draft-e90f8ba9.png)

#### Using the USB cable

The steps are the same as for the dongle: connect the robot with the cable, click `Connect`, and choose the `USB` tab. The dropdown will list the cable's port rather than the dongle's.

## Uploading a program to the robot

Most of our programs run in Live mode, so you will not normally need this. The exception is the Color Vision lesson, whose programs have to be uploaded because the color sensor does not work in Live mode.

1. Make sure the program starts with the `when mBot (mcore) starts up` block rather than `when flag clicked`. An uploaded program runs when the robot is switched on, so it needs that starting block.
2. Use the toggle to switch mBlock to `Upload` mode.
3. Connect to the robot as described above, then click `Upload`.

The program is compiled and transferred to the robot. Switch the robot off and on again to start it. To upload a changed program, repeat these steps.

Once you have uploaded a program, the robot cannot be used in Live mode again until you reset its firmware. That is covered in the next section.

## Resetting the firmware

Before running your first program, you may need to reset the mBot's firmware. As explained in [Live versus Upload mode](#live-versus-upload-mode), running a program in **Live mode** requires the mBot to have its standard firmware (pre-installed onboard software).

Resetting the firmware is not necessary in most cases. However, if you suspect someone has previously used the mBot in **Upload mode**, its firmware may have been overwritten. To ensure compatibility with Live mode, reset the firmware before running your first program.

To reset the firmware, connect the robot to your computer using the USB cable. Then click `Setting`, followed by `Update Firmware`. In the pop-up that appears, click `Updates`. The firmware will be reset, and once it has finished the robot can be used in `Live` mode again.

You do **not** need to switch between `Live` and `Upload` mode first.

![The `Live` and `Upload` slider. You do not need to change it before resetting the firmware.](images/getting-started-draft-bf1a09ed.png)

![Select `Update Firmware`.](images/getting-started-draft-8aa4d6fa.png)

![Click `Updates`.](images/getting-started-draft-05ea3950.png)

## Next step

Once you can connect to the robot, run the example program in [Running your first program](#running-your-first-program). It checks the whole chain — software, connection and robot — in a couple of minutes, and it introduces the pattern every lesson uses for opening its programs.
