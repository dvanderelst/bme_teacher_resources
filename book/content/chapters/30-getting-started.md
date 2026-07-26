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
> With more than one robot in the room, pair each dongle with a particular robot. The computer holding that dongle will then reach that robot and no other, which is what makes it possible to tell a set of identical mBots apart. You only have to do this once per robot.

The order matters: every robot goes off first, then the dongle goes in, and only then does the robot you are pairing come on.

1. Switch **every** robot off, including the one you are about to pair. Do this even when there is only one robot in the room.
2. Plug the dongle into a computer. Its Bluetooth symbol starts flashing.
3. Switch on the robot you are pairing. Its blue LED starts flashing as well.
4. After a few seconds both stop flashing and stay lit. They are paired.
5. Label the robot and the dongle as a set. The dongle will now only connect to this robot, and the labels are what let you match them up later.
6. Repeat for each remaining robot, switching that robot off again before starting the next one.

> **Note**
>
> Pressing the button on the dongle puts it back into pairing mode, which undoes the work above. Tell students to leave it alone, and consider putting a piece of tape over it. It is also how you deliberately re-pair a dongle that is already committed to another robot: press it to release the old pairing, then run the sequence above.

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

When you write a program from scratch, you have to tell mBlock which robot you are writing it for. You do not need to do this if you start from one of our programs, which already know.

Look at the `Devices` panel in mBlock. If the mBot is not listed there, click the `Add (+)` button at the bottom of the panel. A window opens listing the devices mBlock supports: choose **mBot** — not mBot2, which is a different robot — and click `OK`. The mBot then appears in the panel, and the blocks for driving it appear in the palette.

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

The robot stays connected to the computer, over the dongle or the cable, and mBlock sends it commands as the program runs. The robot reacts immediately, you can change the program and try it again without waiting, and — the part that matters for teaching — you can watch sensor readings and variable values update on screen while the robot works.

**Upload mode**

The program is copied onto the robot itself, so it runs without a computer: upload it, unplug the dongle or cable, and the robot carries on by itself. The trade is that nothing is visible while it runs — no sensor values, no variables, no changes on the fly — and every edit means uploading again.

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

### Switching on and plugging in

Whichever version of mBlock you use, the robot end of the job is the same. Switch the robot on and plug its paired dongle into the computer. The Bluetooth symbol on the dongle lights up and stays lit, and the robot's blue LED flashes for a few seconds before going steady. A steady light on both means the robot and the dongle have found each other. If you are using the cable instead, simply plug it in.

That much is the robot talking to the dongle, not to mBlock. The rest is done in mBlock, and it differs between the browser and the installed version.

### Using mBlock in the browser

![mBlock running in the browser, with the mBot already added to the `Devices` panel.](images/getting-started-draft-6bb9e606.png)

#### Direct connection or mLink?

The browser version of mBlock can reach the robot in two different ways, and a link at the top of the `Devices` panel switches between them.

- **Direct connection.** The browser talks to the robot itself. Nothing extra has to be installed, but it only works in Chrome and Chromium.
- **mLink.** The small helper program described in [Installing mBlock](#installing-mblock) does the talking instead. This is the route for browsers that cannot do the job themselves.

**The instructions below use the direct connection**, because it is the simpler of the two and needs nothing installed — which matters on school computers that are locked down. So if the `Devices` panel offers `Switch to direct connection`, click it. If it offers `Switch to mLink`, you are already using the direct connection and there is nothing to do.

![If the panel offers `Switch to direct connection`, click it.](images/getting-started-draft-1dd0fc6c.png)

#### Using the Bluetooth dongle

With the robot on and the dongle plugged in, click `Serial`. This looks wrong the first time: the dongle is a Bluetooth device with a Bluetooth symbol printed on it, and there is a `Bluetooth` button right beside the one you want. But the dongle presents itself to the computer as a serial port, so `Serial` is the right choice.

The browser then asks which serial port to use. Pick the entry for the dongle and click `Connect`.

![With the direct connection selected, click `Serial` — not `Bluetooth`, even though the dongle is a Bluetooth device.](images/getting-started-draft-bd535d8d.png)

![The browser asks which serial port to use. Select the dongle and click `Connect`.](images/getting-started-draft-42631685.png)

#### Using the USB cable

The cable works in exactly the same way. Leave mBlock on the direct connection and choose `Serial` as above; the only difference is which port the browser offers you.

### Using locally installed mBlock

The choice between a direct connection and mLink does not arise here. A locally installed mBlock talks to the robot itself, so there is no helper program and no connection mode to pick.

![mBlock installed on Windows, with the mBot already added to the `Devices` panel.](images/getting-started-draft-45dbe002.png)

#### Using the Bluetooth dongle

With the robot on and the dongle plugged in, click `Connect`.

![In the installed version, click `Connect`.](images/getting-started-draft-230537db.png)

A window opens asking how you want to connect. Choose the `USB` tab. This looks wrong too, and for the same reason as in the browser: the dongle is a Bluetooth device, and the window has a `Bluetooth` tab sitting right next to the one you want. But the dongle appears to the computer as a virtual serial port, and `USB` is where mBlock lists serial ports. If the dongle has been recognised, a port shows up in the dropdown. Click `Connect`.

![Choose the `USB` tab, check that a port is listed in the dropdown, and click `Connect`.](images/getting-started-draft-e90f8ba9.png)

#### Using the USB cable

The steps are the same as for the dongle: click `Connect` and choose the `USB` tab. The dropdown will list the cable's port rather than the dongle's.

## Uploading a program to the robot

Most of our programs run in Live mode, so you will not normally need this. The exception is the Color Vision lesson, whose programs have to be uploaded because the color sensor does not work in Live mode.

1. Make sure the program starts with the `when mBot (mcore) starts up` block rather than `when flag clicked`. An uploaded program runs when the robot is switched on, so it needs that starting block.
2. Use the toggle to switch mBlock to `Upload` mode.
3. Connect to the robot as described above, then click `Upload`.

The program is compiled and transferred to the robot. Switch the robot off and on again to start it. To upload a changed program, repeat these steps.

Once you have uploaded a program, the robot cannot be used in Live mode again until you reset its firmware. That is covered in the next section.

## Resetting the firmware

Running a program in **Live mode** needs the robot to be carrying its standard firmware, as explained in [Live versus Upload mode](#live-versus-upload-mode). Most of the time it is, and there is nothing to do here.

But if the robot has been used in Upload mode — by a previous class, or by you for the Color Vision lesson — that firmware has been overwritten by the uploaded program, and Live mode will not work until you put it back. If you are unsure, resetting does no harm.

Connect the robot to the computer with the USB cable. Click `Setting`, then `Update Firmware`, then `Updates` in the pop-up that appears. When it has finished, the robot works in `Live` mode again.

You do **not** need to switch between `Live` and `Upload` mode first.

![The `Live` and `Upload` slider. You do not need to change it before resetting the firmware.](images/getting-started-draft-bf1a09ed.png)

![Select `Update Firmware`.](images/getting-started-draft-8aa4d6fa.png)

![Click `Updates`.](images/getting-started-draft-05ea3950.png)

## Next step

Once you can connect to the robot, run the example program in [Running your first program](#running-your-first-program). It checks the whole chain — software, connection and robot — in a couple of minutes, and it introduces the pattern every lesson uses for opening its programs.
