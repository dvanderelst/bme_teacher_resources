# Introduction to the robot


In our lesson plans, we use the mBot, an educational robot made by [Makeblock](https://www.makeblock.com). We selected this robot because it easily connects different sensors and can be programmed using a Scratch-like programming language, mBlock.

If your robots still need to be assembled, follow Makeblock's own instructions: [Assemble mBot](https://support.makeblock.com/hc/en-us/articles/12822859943959-A-Beginner-s-Guide-to-mBot#Assemble%20mBot). The rest of this page covers the parts and connections you will need to know about when running the lessons.

![The robot is equipped with a sonar sensor on the front and a line follower sensor on the bottom, which is its default configuration.](images/introduction-to-the-robot-15c3c66e.jpg)

![Screenshot of a program for the robot. The software used to program the robot is called mBlock](images/introduction-to-the-robot-1979a40e.png)

The robot has four ports (Makeblock calls them RJ25 ports), as indicated in the top view of the robot shown below. Each of these ports has several color labels. For example, port 1 is labeled yellow, blue, and white. The color labels are important. They indicate which type of sensor can be connected to which port. For example, the right image shows sound and sonar sensors. The sound sensor is labeled with a black sticker. Therefore, this sensor can only be connected to ports 3 and 4. The sonar sensor is labeled with a yellow sticker. Therefore, sonar sensors can be attached to ports 1, 2, 3, and 4. The type of cable used to connect sensors to the robot is also depicted below.

![Image pointing out the four ports on the robot to which sensors can be attached.](images/introduction-to-the-robot-0c87735b.jpg)

![Left: a sound sensor (notice the black sticker). Right: a sonar sensor (notice the yellow sticker).](images/introduction-to-the-robot-c0775633.jpg)

![This image shows the cable used to connect sensors to the robot.](images/introduction-to-the-robot-676c1e4d.png)

## Which port for which lesson

The lesson plans assume particular ports, and the supplied programs read those ports. This table collects them in one place:

| Lesson or activity | Sensor | Port |
| --- | --- | --- |
| Color Vision | Me Color Sensor | 2 |
| Sonar — Activity 1: measuring directivity | Sonar | 1 |
| Sonar — Activity 2: acoustic mirrors | Sonar | 1 |
| Sonar — Robot obstacle avoidance | Left sonar / right sonar | 1 / 2 |
| Sound Localization — Robot phonotaxis | Left microphone / right microphone | 3 / 4 |

A few things worth knowing alongside that table.

- **Sonar sensors work in any of the four ports.** The table only records what the supplied programs expect, so if you write your own program, you are free to use a different port.
- **The sound sensors have to go in ports 3 or 4.** Those are the only two ports wired to the board's analog inputs,
- **The sound sensor and the color sensor each need an mBlock extension** before their blocks appear in the palette. If you open one of our example programs, the extension loads automatically, but if you start a program from scratch, you have to add it yourself — see [Adding the sound sensor extension](#adding-the-sound-sensor-extension) and [Adding the color sensor extension](#adding-color-sensor-extension).

## Switches, sensors, and ports

The robot takes 4 AA batteries. The on/off switch is indicated in the image below. The robot also has a USB port. As we will explain in upcoming guides, a USB cable is one way the robot can be programmed. However, the preferred way to connect to the robot is wirelessly ([see one of the next guides](#getting-started-with-the-robot)).

![Image pointing out the location of the on/off switch and the USB port.](images/introduction-to-the-robot-b3cee238.jpg)

Even without attaching external sensors to the robot with a cable, the robot has several inputs and outputs.

1. An onboard light sensor that can measure the amount of ambient light.
2. A tiny speaker that can play tones
3. Two LED lights. We can set their brightness and color.
4. The robot has a button that can be used in programs.

If you are curious, the image below shows the location of these devices on the robot’s main board.

![](images/introduction-to-the-robot-51abd850.png)

## Robot moving in the wrong direction?

If the robot is moving backward when it should be moving forward, or if it turns left when it should be turning right, you might have plugged the motors into the wrong ports.

To fix this issue, follow these steps:

1. Turn off the robot and disconnect the power source.
2. Locate the two motor connections on the main board. They are labeled `M1` and `M2`.
3. Check if the motor cables are connected to the correct ports:
    - The left motor should be connected to `M1`.
    - The right motor should be connected to `M2`.
4. If the connections are reversed, carefully unplug the motor cables and swap them.
5. Ensure the cables are securely plugged in.
6. Reconnect the power source and turn on the robot.
7. Test the robot's movement to confirm that the issue is resolved.
