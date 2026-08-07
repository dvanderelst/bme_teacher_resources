# Introduction to the robot

Our lesson plans use the mBot, an educational robot made by [Makeblock](https://www.makeblock.com). We selected this robot because it easily connects to various sensors and is programmed using mBlock, a Scratch-like visual programming language.

If your robots still need assembly, follow Makeblock's instructions: [Assemble mBot](https://support.makeblock.com/hc/en-us/articles/12822859943959-A-Beginner-s-Guide-to-mBot#Assemble%20mBot). The rest of this chapter covers the parts and connections we need to know for the lessons.

![mBot in default configuration: sonar sensor front, line follower underside](images/introduction-to-the-robot-default-configuration.jpg)

![A program for the robot in mBlock.](images/introduction-to-the-robot-1979a40e.png)

## Ports and sensor compatibility

The robot has four `RJ25` ports (Makeblock's name for these connectors).

Pay attention to the color labels on each port. These indicate which sensors the port accepts:

- sound sensor (black label): Use port 3 or 4 only (these are the only ports with analog inputs, which sound sensors require)
- sonar sensor (yellow label): Works in any port (1-4)
- line follower (white label): Works in any port (1-4)
- color sensor (white label): Works in any port (1-4)

The board confirms this in its own labeling, though the print is small and requires good light to read. Here is how the ports connect to the microcontroller:

- port 1: Digital pins 11, 12
- port 2: Digital pins 9, 10
- port 3: Analog pins A2, A3
- port 4: Analog pins A0, A1

Because sound sensors output a continuously varying voltage, they require an analog pin and must use port 3 or 4. Using two sound sensors (or two whiskers) consumes all available analog pins.

**Important:** The ports are not interchangeable. When a lesson specifies a port, use that exact port—our programs expect sensors on the specified ports. mBlock also enforces these restrictions: if we add a sound sensor block, its port dropdown only offers ports 3 and 4, preventing errors even if we forget the rule. The [Block reference](#block-reference) notes which ports each block's dropdown offers.

![Four RJ25 ports on top of the mBot](images/introduction-to-the-robot-0c87735b.jpg)

![Sound sensor (black label) and sonar sensor (yellow label)](images/introduction-to-the-robot-c0775633.jpg)

![RJ25 cable: identical ends, telephone-style connector](images/introduction-to-the-robot-rj25-cable.jpg)

The sound and color sensors require an mBlock extension before their blocks appear. Our example programs load the extension automatically. If we start from scratch, we must add it ourselves. See [Adding the sound sensor extension](#adding-the-sound-sensor-extension) and [Adding the color sensor extension](#adding-color-sensor-extension).

## Switches and onboard sensors

The mBot runs on four AA batteries. If we prefer not to replace batteries constantly, a rechargeable battery pack is also available. See [the rechargeable battery pack](#optional-the-rechargeable-battery-pack) below.

All components in this section are on one board: the mCore. This sits on top of the robot under a clear case. The on/off switch and USB port are both on it and are reachable without opening the case. We can program over USB, but we recommend the wireless connection. See [Getting started with the robot](#getting-started-with-the-robot).

Even without external sensors, the mBot has several built-in components:

- light sensor: Measures ambient light levels
- buzzer/speaker: Plays tones and simple sounds
- two RGB LEDs: Programmable brightness and color
- onboard button: Can be read by our programs

The image below shows where these are located.

![The mCore in two views: case on and off, with ports and components labeled](images/introduction-to-the-robot-mcore-labelled.png)

Three additional components are on the board but not marked in the picture. The board names all three:

- push button: The small black square at the top left of the right-hand view, with `Button` printed beside it. Programs can read it, though none of our lessons do.
- infrared transmitter (`IR_T`): The tall clear dome to the right of the button.
- infrared receiver (`IR_R`): Beside the transmitter. No lesson uses either component.

## Optional: the rechargeable battery pack

The mBot runs on four AA batteries by default. We can replace them with a rechargeable battery pack that charges via USB. This avoids repeatedly purchasing disposable batteries and takes only a few minutes per robot to install.

![Rechargeable battery pack: lithium cell with keyed plug](images/optional-using-the-battery-pack-pack.jpg)

To install the battery pack:

1. Unplug the AA battery holder from the robot.
2. Unscrew and remove the top board.

![Top board unscrewed, AA battery holder unplugged](images/optional-using-the-battery-pack-4f020b9a.jpg)

3. Clip the battery pack to the underside of the top board.
4. Connect it to the board using the red and black cables. The connector only fits in one orientation.

![Battery pack clipped to top board, cables ready to plug in](images/optional-using-the-battery-pack-db21ceea.jpg)

5. Reattach the top board to the robot. The AA battery holder is no longer needed.

![Top board screwed back on, AA battery holder set aside](images/optional-using-the-battery-pack-b8f42f1d.jpg)

Charge the pack by connecting the robot to a USB power source. A red LED indicates charging is in progress; it turns green when complete.

> **Tip**
>
> Do not charge the robot while it runs on the 4 AA batteries.

![Charging in progress. Notice the red LED.](images/optional-using-the-battery-pack-9d9b2d0d.jpg)

![Charging complete. Note the green LED.](images/optional-using-the-battery-pack-b758c100.jpg)

## Robot moving in the wrong direction?

If the mBot moves backward when it should move forward, or turns left when it should turn right, the motor cables may be connected to the wrong ports.

To correct this:

1. Turn off the mBot and disconnect the power source.
2. Locate the two motor connections on the main board, labeled `M1` and `M2`. These are the pair of white connectors between the ports and the power switch. `M2` is next to the power switch and, with the board mounted in the chassis, is also nearer the back of the robot. `M1` is on the side of ports 1 and 2, towards the front. The board prints both names, but the type is small, so use the power switch as your landmark.
3. Verify the motor cable connections:
   - Left motor to `M1`
   - Right motor to `M2`
4. If reversed, unplug the cables and swap them.
5. Ensure both cables are securely seated.
6. Reconnect power and turn on the robot.
7. Test movement to confirm the correction.
