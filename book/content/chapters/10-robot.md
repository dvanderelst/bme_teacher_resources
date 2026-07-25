# Introduction to the robot

In our lesson plans, we use the mBot, an educational robot made by [Makeblock](https://www.makeblock.com). We selected this robot because it easily connects different sensors and can be programmed using a Scratch-like programming language, mBlock.

If your robots still need to be assembled, follow Makeblock's own instructions: [Assemble mBot](https://support.makeblock.com/hc/en-us/articles/12822859943959-A-Beginner-s-Guide-to-mBot#Assemble%20mBot). The rest of this chapter covers the parts and connections you will need to know about when running the lessons.

![The robot is equipped with a sonar sensor on the front and a line follower sensor on the bottom, which is its default configuration.](images/introduction-to-the-robot-15c3c66e.jpg)

![A program for the robot. The software we use to write these programs is called mBlock.](images/introduction-to-the-robot-1979a40e.png)

## Ports and sensor labels

The robot has four ports, which Makeblock calls RJ25 ports. The top view below shows where they are. Each port carries several color labels — port 1, for example, is labeled yellow, blue, and white — and those labels are the thing to pay attention to, because they tell you which kind of sensor a port can accept. The sound sensor carries a black label, and only ports 3 and 4 have black among their colors, so a sound sensor has to go in one of those two. They are the only ports wired to the board's analog inputs, which is what a sound sensor needs. The sonar sensor carries a yellow label, and all four ports have yellow, so a sonar will work in any of them.

The point to take away is that the ports are not interchangeable, so it is worth checking which one you are plugging into. When a lesson plan asks for a particular port, use that port: the programs we supply read the port the lesson names. mBlock knows about the restrictions too — add a sound sensor block to a program and its port dropdown will offer you only 3 and 4 — so the software will stop you making the worst of these mistakes even if you forget.

![The four RJ25 ports on top of the robot, where sensors plug in.](images/introduction-to-the-robot-0c87735b.jpg)

![Left: a sound sensor (notice the black sticker). Right: a sonar sensor (notice the yellow sticker).](images/introduction-to-the-robot-c0775633.jpg)

![The cable used to connect a sensor to one of the robot's ports.](images/introduction-to-the-robot-676c1e4d.png)

Two of the sensors we use, the sound sensor and the color sensor, need an mBlock *extension* installed before their blocks appear in the palette. Opening one of our example programs loads the right extension for you, but starting a program from scratch does not, so in that case you have to add it yourself. See [Adding the sound sensor extension](#adding-the-sound-sensor-extension) and [Adding the color sensor extension](#adding-color-sensor-extension).

## Switches and onboard sensors

The robot runs on four AA batteries. If you would rather not keep replacing them, a rechargeable battery pack is available as well; see [Optional: the rechargeable battery pack](#optional-the-rechargeable-battery-pack) below.

The on/off switch is indicated in the image below. The robot also has a USB port. As we will explain in upcoming guides, a USB cable is one way to program the robot. However, the preferred way to connect to the robot is wirelessly ([see one of the next guides](#getting-started-with-the-robot)).

![The location of the on/off switch and the USB port.](images/introduction-to-the-robot-b3cee238.jpg)

Even without attaching external sensors to the robot with a cable, the robot has several inputs and outputs.

1. A light sensor that measures the amount of ambient light.
2. A small speaker that can play tones.
3. Two RGB LEDs, whose brightness and color you can set.
4. A button that your programs can read.

If you are curious, the image below shows where these sit on the robot's main board. The board also carries an infrared receiver and transmitter, which our lessons do not use.

![The mBot's main board, the mCore, with its connectors and onboard devices labeled. Diagram by Makeblock.](images/introduction-to-the-robot-51abd850.png)

## Optional: the rechargeable battery pack

By default the robot runs on four AA batteries, but it can also be powered by a rechargeable battery pack that charges over USB. If you would rather not keep buying AA batteries, this is worth doing. Installing it takes a few minutes per robot.

![The battery pack.](images/optional-using-the-battery-pack-b3a67c4f.jpg)

Start by unplugging the AA battery holder from the robot. You will need to unscrew the robot's top board as well, so it is easiest to do that now rather than partway through.

![The top board unscrewed and lifted clear, with the AA battery holder unplugged.](images/optional-using-the-battery-pack-4f020b9a.jpg)

The battery pack attaches to the underside of the top board, clipping into the slots there. Once it is clipped in, plug it into the board using the red and black cables. The plug is shaped so that it only fits one way round.

![The pack clipped into the underside of the top board, with the red and black cables ready to plug in.](images/optional-using-the-battery-pack-db21ceea.jpg)

Screw the board back onto the robot. The AA battery holder is no longer needed.

![The top board screwed back on, with the AA battery holder set aside.](images/optional-using-the-battery-pack-b8f42f1d.jpg)

You can now charge the pack by connecting the robot to a charger or a USB port with the USB cable. While it charges, the robot shows a red light; when charging is complete, the light turns green.

> **Tip**
>
> Please do not attempt to charge the robot while it is running on the 4 x AA batteries.

![Charging. Notice the red LED.](images/optional-using-the-battery-pack-9d9b2d0d.jpg)

![Charging complete. Note the green LED.](images/optional-using-the-battery-pack-b758c100.jpg)

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
