# Introduction to the robot

Our lesson plans use the mBot, an educational robot made by [Makeblock](https://www.makeblock.com). We selected this robot because it easily connects to various sensors and is programmed using mBlock, a Scratch-like visual programming language.

If your robots still need assembly, follow Makeblock's instructions: [Assemble mBot](https://support.makeblock.com/hc/en-us/articles/12822859943959-A-Beginner-s-Guide-to-mBot#Assemble%20mBot). The rest of this chapter covers the parts and connections you need to know for the lessons.

![An mBot in its default configuration. The sonar sensor is bolted to the front with its two metal cylinders facing forward, and the line follower is on the underside just behind it, angled down at the floor. This is how the robot arrives, and it is the configuration most lessons start from. The white stickers on the board are the colored port labels, with `2` and `1` visible here and the sonar's cable plugged into port 1.](images/introduction-to-the-robot-default-configuration.jpg)

![A program for the robot in mBlock.](images/introduction-to-the-robot-1979a40e.png)

## Ports and sensor compatibility

The robot has four RJ25 ports (Makeblock's name for these connectors).

Pay attention to the color labels on each port. These indicate which sensors the port accepts:

- **Sound sensor** (black label): Use port 3 or 4 only (these are the only ports with analog inputs, which sound sensors require)
- **Sonar sensor** (yellow label): Works in any port (1-4)
- **Line follower** (white label): Works in any port (1-4)
- **Color sensor** (white label): Works in any port (1-4)

The board confirms this in its own labeling, though the print is small and requires good light to read. Here is how the ports connect to the microcontroller:

- **Port 1:** Digital pins 11, 12
- **Port 2:** Digital pins 9, 10
- **Port 3:** Analog pins A2, A3
- **Port 4:** Analog pins A0, A1

Because sound sensors output a continuously varying voltage, they require an analog pin and must use port 3 or 4. Using two sound sensors (or two whiskers) consumes all available analog pins.

**Important:** The ports are not interchangeable. When a lesson specifies a port, use that exact port—our programs expect sensors on the specified ports. mBlock also enforces these restrictions: if you add a sound sensor block, its port dropdown only offers ports 3 and 4, preventing errors even if you forget the rule. The [Block reference](#block-reference) notes which ports each block's dropdown offers.

![The four RJ25 ports on top of the mBot, where sensors plug in.](images/introduction-to-the-robot-0c87735b.jpg)

![Left: a sound sensor with its black label. Right: a sonar sensor with its yellow label.](images/introduction-to-the-robot-c0775633.jpg)

![An RJ25 cable. Both ends are identical, so it cannot be plugged in the wrong way. The plug clips in like a telephone connector—press the tab to release it rather than pulling on the cable. Two cables come with the robot. In the default configuration, both are already in use (one for the sonar, one for the line follower), which is why the materials list asks for a spare per robot.](images/introduction-to-the-robot-rj25-cable.jpg)

The sound and color sensors require an mBlock extension before their blocks appear. Our example programs load the extension automatically. If you start from scratch, you must add it yourself. See [Adding the sound sensor extension](#adding-the-sound-sensor-extension) and [Adding the color sensor extension](#adding-color-sensor-extension).

## Switches and onboard sensors

The mBot runs on four AA batteries. If you prefer not to replace batteries constantly, a rechargeable battery pack is also available. See [the rechargeable battery pack](#optional-the-rechargeable-battery-pack) below.

All components in this section are on one board: the **mCore**. This sits on top of the robot under a clear case. The on/off switch and USB port are both on it and are reachable without opening the case. You can program over USB, but we recommend the wireless connection. See [Getting started with the robot](#getting-started-with-the-robot).

Even without external sensors, the mBot has several built-in components:

- **Light sensor** – Measures ambient light levels
- **Buzzer/speaker** – Plays tones and simple sounds
- **Two RGB LEDs** – Programmable brightness and color
- **Onboard button** – Can be read by your programs

The image below shows where these are located.

![The mCore in two views. **Left**: As it comes in the robot. The case is clear, so you can read the four ports (arrowed) and the case's own printed labels (`Motor Connector M1 M2`, `Power Switch OFF ON`, `Power Connector`, `USB`, `Reset`) without taking anything apart. **Right**: The same board with the case off. The parts this section refers to are marked: the two RGB LEDs with the light sensor between them, the buzzer, the motor connectors, the on/off switch, the USB port, and the Bluetooth board the dongle pairs with. Only port 3 is arrowed on the right as an example—the four ports are the four stickered connectors along the two sides.](images/introduction-to-the-robot-mcore-labelled.png)

Three additional components are on the board but not marked in the picture. The board names all three:

- **Push button:** The small black square at the top left of the right-hand view, with `Button` printed beside it. Programs can read it, though none of our lessons do.
- **Infrared transmitter (`IR_T`):** The tall clear dome to the right of the button.
- **Infrared receiver (`IR_R`):** Beside the transmitter. No lesson uses either component.

## Optional: the rechargeable battery pack

By default, the mBot runs on four AA batteries. You can replace them with a rechargeable battery pack that charges via USB. This avoids repeatedly purchasing disposable batteries and takes only a few minutes per robot to install.

![The rechargeable battery pack: a lithium cell in a clear holder, with a two-wire lead ending in a small white plug. The polarity is printed on the cell (red is positive, black is negative), but you do not need to check it—the plug is keyed and only fits one way.](images/optional-using-the-battery-pack-pack.jpg)

To install the battery pack:

1. Unplug the AA battery holder from the robot.
2. Unscrew and remove the top board.

![The top board unscrewed and lifted clear, with the AA battery holder unplugged.](images/optional-using-the-battery-pack-4f020b9a.jpg)

3. Clip the battery pack to the underside of the top board.
4. Connect it to the board using the red and black cables. The connector only fits in one orientation.

![The pack clipped into the underside of the top board, with the red and black cables ready to plug in.](images/optional-using-the-battery-pack-db21ceea.jpg)

5. Reattach the top board to the robot. The AA battery holder is no longer needed.

![The top board screwed back on, with the AA battery holder set aside.](images/optional-using-the-battery-pack-b8f42f1d.jpg)

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
2. Locate the two motor connections on the main board, labeled `M1` and `M2`. These are the pair of white connectors between the ports and the power switch. **`M2` is next to the power switch** and, with the board mounted in the chassis, is also nearer the back of the robot. `M1` is on the side of ports 1 and 2, towards the front. The board prints both names, but the type is small, so use the power switch as your landmark.
3. Verify the motor cable connections:
   - Left motor to `M1`
   - Right motor to `M2`
4. If reversed, unplug the cables and swap them.
5. Ensure both cables are securely seated.
6. Reconnect power and turn on the robot.
7. Test movement to confirm the correction.
