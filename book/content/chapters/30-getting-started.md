# Getting started with the robot

This chapter assumes you already have **mBlock** installed or running in your browser. If not, complete [Installing mBlock](#installing-mblock) first, then return here.

## Connection options

To program and control your mBot, connect it to your computer using one of these methods:

1. **Using the Bluetooth dongle.** A wireless connection with a Makeblock Bluetooth dongle, shown in the first image below.
2. **Using a USB cable.** A wired connection between your computer and the robot, using the cable shown in the second image.

Older mBots could connect via a 2.4 GHz module or direct Bluetooth. We do not support these. Makeblock has discontinued the 2.4 GHz hardware, and with direct Bluetooth all robots in a classroom share the same address, preventing students from identifying which robot they are connecting to.

![The Bluetooth dongle that can be used to connect to the robot. The Bluetooth symbol on its top face is the pairing button as well as the indicator light — press it to put the dongle into pairing mode.](images/getting-started-draft-6fb3632a.png)

![The USB cable that can be used to connect to the robot.](images/getting-started-draft-dd60485a.png)

## Pairing the Bluetooth dongle and the robot

> **Note**
>
> With multiple robots in the room, pair each dongle to a specific robot. This ensures the computer using that dongle connects only to its paired robot, allowing you to distinguish identical mBots. Pairing is only needed once per robot.

Follow this sequence precisely: turn all robots off first, then put the dongle into pairing mode, then power on only the robot you are pairing.

1. Switch **all** robots off, including the one you are pairing. Do this even if only one robot is present.
2. Plug the dongle into a computer.
3. Press the Bluetooth symbol on the top of the dongle — the symbol is the button, and it is also the light. It begins flashing **quickly**, which means the dongle is in pairing mode and has released whatever robot it was paired with before. Press it every time you pair, including on a dongle straight out of its packaging: you cannot tell by looking whether a dongle has been paired before, and pressing one that is already in pairing mode does no harm.
4. Switch on the robot you are pairing. Its blue LED starts flashing as well.
5. After a few seconds, both lights stop flashing and remain lit. They are now paired.
6. Label the robot and dongle as a set. The dongle will only connect to this robot; use the labels to match them later.
7. Repeat for each remaining robot, turning it off before pairing the next one.

> **Note**
>
> The dongle flashes at two speeds, and they mean opposite things. **Fast** means it is in pairing mode and will bond with the next robot switched on nearby. **Slow** means it is already paired and cannot find its robot — usually because that robot is switched off, out of range, or is not the one this dongle belongs to. A slowly flashing dongle looks like a dongle waiting to pair, and this is the single most likely reason for a pairing that appears to work and then does not connect. It is why step 3 presses the button rather than checking the light first.

> **Note**
>
> The button is also how a pairing gets broken: pressing it releases the robot, and that dongle will no longer connect to it until they are paired again. Once a set is paired and labelled, instruct students not to press it, and consider covering it with tape for the rest of the lesson. Remove the tape when you next need to pair that dongle to a different robot.

![Blue LED blinking on the robot's Bluetooth module.](images/getting-started-draft-1f093a0d.jpg)

![When the dongle and the robot are paired, the blue LEDs on both will stop blinking.](images/getting-started-draft-f62edb5b.jpg)

## Checking whether a dongle and a robot are paired

Labels can fall off, and after extended use existing labels may no longer be reliable. You can verify a pair without opening mBlock by observing that paired devices blink when separated from their partner.

1. Switch the robot on and plug in the dongle. Both should display a **steady** blue light. If either keeps blinking, they are not paired to each other — a slow blink on the dongle means it is paired to some other robot.
2. Unplug the dongle. After a few seconds, the robot's blue light starts **blinking** — it has lost its partner.
3. Plug the dongle back in. Both should return to steady lights.
4. Switch the robot off. After five to ten seconds, the dongle's light starts blinking **slowly**, for the same reason.

If separating the pair from either end causes the other to blink, they are correctly paired and you can relabel them confidently. If a light never becomes steady initially, or remains steady after its partner is removed, re-pair them as described above.

## Adding the mBot to mBlock

When writing a program from scratch, you must tell mBlock which robot to target. This is not necessary when starting from one of our programs, which are pre-configured.

If the mBot does not appear in the `Devices` panel, click the `Add (+)` button at the bottom. A window listing supported devices appears. Select **mBot** — not mBot2, which is a different robot — and click `OK`. The mBot appears in the panel, and its control blocks become available in the palette.

![Click this button to add the robot to mBlock.](images/getting-started-draft-c19638ac.png)

![The devices area before adding the mBot.](images/getting-started-draft-bcbd96a0.png)

![Select the mBot from the menu.](images/getting-started-draft-f2ecdd41.png)

![The devices area after adding the mBot.](images/getting-started-draft-7bfc097d.png)

## Live versus Upload mode

When programming your mBot, you can run code in **Live mode** or **Upload mode**.

> **The short version**
>
> Use Live mode for all lessons except Color Vision. Live mode displays sensor readings and variable values in real time, making the robot effective for teaching. The color sensor is the exception: mBlock does not support it in Live mode, so Color Vision programs must be uploaded. However, uploading overwrites the robot's firmware, requiring a reset before returning to Live mode.

**Live mode**

The robot remains connected to the computer (via dongle or cable), and mBlock sends commands as the program runs. The robot responds immediately, you can modify and re-test the program without delay, and — critically for teaching — you can monitor sensor readings and variable values on screen in real time.

**Upload mode**

The program is copied to the robot, allowing it to run independently: upload it, then unplug the dongle or cable. The robot operates on its own. The trade-off is that nothing is visible during operation — no sensor values, no variables, no on-the-fly changes — and each modification requires re-uploading.

**Switching from Upload back to Live mode**

After using Upload mode, reset the robot's firmware to return to Live mode, as described in [Resetting the firmware](#resetting-the-firmware).

> **Why?**
>
> Live mode requires special firmware — Makeblock calls this the **Online firmware** — that enables communication with the computer. When you use Upload mode, your program replaces this firmware. Resetting restores the Online firmware, which re-enables Live mode. (Makeblock's documentation refers to this as *updating* the firmware, which is the terminology used in mBlock.)

## Connecting to the robot

### Requirements

Before connecting to the robot, verify the following:

1. You have mBlock, either in the browser or installed. See [Installing mBlock](#installing-mblock).
2. You have chosen a connection method: USB cable or Bluetooth dongle. See [Connection options](#connection-options).
3. If using the Bluetooth dongle, it is paired with the robot. See [Pairing the Bluetooth dongle and the robot](#pairing-the-bluetooth-dongle-and-the-robot).
4. You have added the mBot to mBlock. See [Adding the mBot to mBlock](#adding-the-mbot-to-mblock).

### Switching on and plugging in

Regardless of which mBlock version you use, the robot setup is the same. Switch the robot on and plug its paired dongle into the computer. The Bluetooth symbol on the dongle lights up and remains lit, while the robot's blue LED flashes for a few seconds before becoming steady. Steady lights on both indicate the robot and dongle have connected. If using a USB cable, simply plug it in.

This establishes the robot-to-dongle connection. The mBlock connection process varies between browser and installed versions.

### Using mBlock in the browser

![mBlock running in the browser, with the mBot already added to the `Devices` panel.](images/getting-started-draft-6bb9e606.png)

#### Direct connection or mLink?

The browser version of mBlock can connect to the robot in two ways, selected via a link at the top of the `Devices` panel:

- **Direct connection.** The browser communicates directly with the robot. No additional software is required, but this only works in Chrome and Chromium.
- **mLink.** The helper program described in [Installing mBlock](#installing-mblock) handles communication. Use this for browsers that cannot connect directly.

**The instructions below use direct connection**, as it is simpler and requires no installation — important for locked-down school computers. If the `Devices` panel shows `Switch to direct connection`, click it. If it shows `Switch to mLink`, you are already using direct connection.

![If the panel offers `Switch to direct connection`, click it.](images/getting-started-draft-1dd0fc6c.png)

#### Using the Bluetooth dongle

With the robot on and dongle plugged in, click `Serial`. This may seem counterintuitive: the dongle is a Bluetooth device, and a `Bluetooth` button appears beside it. However, the dongle presents itself to the computer as a serial port, so `Serial` is the correct choice.

The browser then prompts you to select a serial port. Choose the dongle's entry and click `Connect`.

![With direct connection selected, click `Serial` — not `Bluetooth`, even though the dongle is a Bluetooth device.](images/getting-started-draft-bd535d8d.png)

![The browser asks which serial port to use. Select the dongle and click `Connect`.](images/getting-started-draft-42631685.png)

#### Using the USB cable

The cable works identically. Keep mBlock on direct connection and select `Serial` as above; the only difference is which port the browser presents.

### Using locally installed mBlock

The browser's choice between direct connection and mLink does not apply here. Installed mBlock communicates directly with the robot, so no helper program or connection mode selection is needed.

![mBlock installed on Windows, with the mBot already added to the `Devices` panel.](images/getting-started-draft-45dbe002.png)

#### Using the Bluetooth dongle

With the robot on and dongle plugged in, click `Connect`.

![In the installed version, click `Connect`.](images/getting-started-draft-230537db.png)

A window opens asking how to connect. Select the `USB` tab. This may also seem counterintuitive: the dongle is a Bluetooth device, yet a `Bluetooth` tab appears beside `USB`. However, the dongle appears to the computer as a virtual serial port, and `USB` is where mBlock lists serial ports. If the dongle is recognized, a port appears in the dropdown. Click `Connect`.

![Select the `USB` tab, verify a port is listed in the dropdown, and click `Connect`.](images/getting-started-draft-e90f8ba9.png)

#### Using the USB cable

The steps are identical to the dongle: click `Connect` and select the `USB` tab. The dropdown lists the cable's port instead of the dongle's.

## Uploading a program to the robot

Most programs run in Live mode, so this is rarely needed. The exception is the Color Vision lesson, where programs must be uploaded because the color sensor does not work in Live mode.

1. Ensure the program starts with the `when mBot (mcore) starts up` block rather than `when flag clicked`. An uploaded program runs when the robot powers on, requiring this starting block.
2. Use the toggle to switch mBlock to `Upload` mode.
3. Connect to the robot as described above, then click `Upload`.

The program compiles and transfers to the robot. Power the robot off and on again to start it. To upload a modified program, repeat these steps.

After uploading a program, the robot cannot be used in Live mode until you reset its firmware, as described in the next section.

## Resetting the firmware

Live mode requires the robot to have its standard firmware, as explained in [Live versus Upload mode](#live-versus-upload-mode). Typically this is already in place.

However, if the robot was used in Upload mode — by a previous class or for the Color Vision lesson — that firmware has been overwritten by the uploaded program. Live mode will not function until you restore it. If uncertain, resetting causes no harm.

Connect the robot to the computer using the USB cable. Click `Setting`, then `Update Firmware`, then `Updates` in the pop-up window. Once complete, the robot works in Live mode again.

You do **not** need to switch between `Live` and `Upload` mode first.

![The `Live` and `Upload` slider. You do not need to change it before resetting the firmware.](images/getting-started-draft-bf1a09ed.png)

![Select `Update Firmware`.](images/getting-started-draft-8aa4d6fa.png)

![Click `Updates`.](images/getting-started-draft-05ea3950.png)

## Next step

Once you can connect to the robot, run the example program in [Running your first program](#running-your-first-program). It verifies the entire setup — software, connection, and robot — in a couple of minutes, and introduces the pattern used throughout the lessons for opening programs.
