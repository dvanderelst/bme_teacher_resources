# Introduction to the robot

Our lesson plans use the mBot, an educational robot made by [Makeblock](https://www.makeblock.com). We selected this robot because it easily connects various sensors and is programmed using mBlock, a Scratch-like language.

If your robots still need assembly, follow Makeblock's instructions: [Assemble mBot](https://support.makeblock.com/hc/en-us/articles/12822859943959-A-Beginner-s-Guide-to-mBot#Assemble%20mBot). The rest of this chapter covers the parts and connections you need to know for the lessons.

![An mBot in its default configuration: the sonar sensor bolted to the front, its two metal cylinders facing forward, and the line follower on the underside just behind it, angled down at the floor. This is how the robot arrives, and it is the configuration most of the lessons start from. The white stickers on the board are the coloured port labels the next section is about — `2` and `1` are visible here, with the sonar's cable plugged into port 1.](images/introduction-to-the-robot-default-configuration.jpg)

![A program for the robot. The software we use to write these programs is called mBlock.](images/introduction-to-the-robot-1979a40e.png)

## Ports and sensor compatibility

The robot has four RJ25 ports (Makeblock's name for these connectors).

Each port has several color labels. Port 1, for example, is labeled yellow, blue, and white. Pay attention to these labels, as they indicate which sensors each port accepts. The sound sensor has a black label; only ports 3 and 4 include black, so it must be plugged into one of those. These are the only ports with analog inputs, which sound sensors require. The sonar sensor has a yellow label, and all four ports have yellow, so a sonar will work in any of them.

The board says so itself, in print small enough that you need the board out of the robot and good light to read it. Ports 3 and 4 are wired to the microcontroller's four analog pins — port 3 to `A2` and `A3`, port 4 to `A0` and `A1` — while ports 1 and 2 get digital pins only: port 1 gets `11` and `12`, port 2 gets `9` and `10`. That is the whole of the restriction. A sound sensor reports a continuously varying voltage, which needs an analog pin to read, so it needs port 3 or port 4; the sonar, the line follower and the colour sensor do not, so they do not care. Two sound sensors, or two whiskers, use up every analog pin the robot has.

Importantly, the ports are not interchangeable, so check which one you are using. When a lesson specifies a port, use that port; our programs expect sensors on the specified ports. mBlock also enforces these restrictions. If you add a sound sensor block, its port dropdown only offers ports 3 and 4, preventing serious errors even if you forget. The [Block reference](#block-reference) notes, for each block, which ports its dropdown offers.

![The four RJ25 ports on top of the robot, where sensors plug in.](images/introduction-to-the-robot-0c87735b.jpg)

![Left: a sound sensor (with black label). Right: a sonar sensor (with yellow label).](images/introduction-to-the-robot-c0775633.jpg)

![An RJ25 cable, which is how every external sensor reaches the robot. Both ends are identical, so it cannot be plugged in the wrong way round, and the plug clips in like a telephone connector — press the tab to release it rather than pulling on the cable. Two come with the robot, and in the default configuration both are already in use — one for the sonar, one for the line follower — which is why the materials list asks for a spare per robot.](images/introduction-to-the-robot-rj25-cable.jpg)

The sound and color sensors require an mBlock extension before their blocks appear. Our example programs load the extension automatically. If you start from scratch, you must add it yourself. See [Adding the sound sensor extension](#adding-the-sound-sensor-extension) and [Adding the color sensor extension](#adding-color-sensor-extension).

## Switches and onboard sensors

The robot runs on four AA batteries. If you prefer not to replace batteries constantly, a rechargeable battery pack is also available; see [the rechargeable battery pack](#optional-the-rechargeable-battery-pack) below.

Everything in this section is on one board, the **mCore**, which sits on top of the robot under a clear case. The on/off switch and the USB port are both on it, and both are reachable without opening anything. You can program over USB, but the recommended method is the wireless connection (see [Getting started with the robot](#getting-started-with-the-robot)).

Even without external sensors, the robot has several built-in inputs and outputs:

1. A light sensor that measures the amount of ambient light.
2. A small speaker that can play tones.
3. Two RGB LEDs, whose brightness and color you can set.
4. A button that your programs can read.

The picture below shows where these sit.

![The mCore in two views. **Left**, as it comes in the robot: the case is clear, so the four ports (arrowed) and the case's own printed labels — `Motor Connector M1 M2`, `Power Switch OFF ON`, `Power Connector`, `USB`, `Reset` — can all be read without taking anything apart. **Right**, the same board with the case off, and the parts this section refers to marked: the two RGB LEDs with the light sensor between them, the buzzer, the motor connectors, the on/off switch, the USB port, and the Bluetooth board the dongle pairs with. Only port 3 is arrowed on the right, as an example — the four ports are the four stickered connectors along the two sides.](images/introduction-to-the-robot-mcore-labelled.png)

Three components are on the board but not marked in the picture, and the board names all three itself. The push button is the small black square at the top left of the right-hand view, with `Button` printed beside it; programs can read it, though none of ours do. Just to its right, `IR_T` labels the infrared transmitter — the tall clear dome — and `IR_R` the infrared receiver beside it. No lesson uses either.

## Optional: the rechargeable battery pack

By default, the robot runs on four AA batteries, but you can replace them with a rechargeable battery pack that charges via USB. This avoids repeatedly purchasing disposable batteries and takes only a few minutes per robot to install.

![The rechargeable battery pack: a lithium cell in a clear holder, with a two-wire lead ending in a small white plug. The polarity is printed on the cell itself — red is positive, black negative — but you do not have to act on it, because the plug is keyed and only goes in one way round.](images/optional-using-the-battery-pack-pack.jpg)

Begin by unplugging the AA battery holder from the robot. You must also unscrew the top board, so remove it now rather than later in the process.

![The top board unscrewed and lifted clear, with the AA battery holder unplugged.](images/optional-using-the-battery-pack-4f020b9a.jpg)

Clip the battery pack to the underside of the top board. Then connect it to the board using the red and black cables. The connector only fits in one orientation.

![The pack clipped into the underside of the top board, with the red and black cables ready to plug in.](images/optional-using-the-battery-pack-db21ceea.jpg)

Reattach the top board to the robot. The AA battery holder is no longer required.

![The top board screwed back on, with the AA battery holder set aside.](images/optional-using-the-battery-pack-b8f42f1d.jpg)

Charge the pack by connecting the robot to a USB power source. A red LED indicates charging in progress; it turns green when complete.

> **Tip**
>
> Do not charge the robot while it runs on the 4 x AA batteries.

![Charging. Notice the red LED.](images/optional-using-the-battery-pack-9d9b2d0d.jpg)

![Charging complete. Note the green LED.](images/optional-using-the-battery-pack-b758c100.jpg)

## Robot moving in the wrong direction?

If the robot moves backward when it should move forward, or turns left when it should turn right, the motor cables may be connected to the wrong ports.

To correct this:

1. Turn off the robot and disconnect the power source.
2. Locate the two motor connections on the main board, labeled `M1` and `M2`. They are the pair of white connectors between the ports and the power switch. **`M2` is the one next to the power switch**, and, with the board mounted in the chassis, it is also the one nearer the back of the robot; `M1` is on the side of ports 1 and 2, towards the front. The board prints both names, but in type small enough that the power switch is the quicker landmark.
3. Verify the motor cable connections:
    - Left motor to `M1`
    - Right motor to `M2`
4. If reversed, unplug the cables and swap them.
5. Ensure both cables are securely seated.
6. Reconnect power and turn on the robot.
7. Test movement to confirm the correction.
