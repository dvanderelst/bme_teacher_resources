---
chapter: "Introduction to the robot"
source: 10-robot.md
edition: "27 July 2026"
fingerprint: "6a5b178-stale"
---

# Introduction to the robot

Our lesson plans use the mBot, an educational robot made by [Makeblock](https://www.makeblock.com). We selected this robot because it easily connects various sensors and is programmed using mBlock, a Scratch-like language.

If your robots still need assembly, follow Makeblock's instructions: [Assemble mBot](https://support.makeblock.com/hc/en-us/articles/12822859943959-A-Beginner-s-Guide-to-mBot#Assemble%20mBot). The rest of this chapter covers the parts and connections you need to know for the lessons.

Figure: The robot is equipped with a sonar sensor on the front and a line follower sensor on the bottom, which is its default configuration. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-the-robot-15c3c66e.jpg))

Figure: A program for the robot. The software we use to write these programs is called mBlock. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-the-robot-1979a40e.png))

## Ports and sensor compatibility

The robot has four RJ25 ports (Makeblock's name for these connectors).

Each port has several color labels. Port 1, for example, is labeled yellow, blue, and white. Pay attention to these labels, as they indicate which sensors each port accepts. The sound sensor has a black label; only ports 3 and 4 include black, so it must be plugged into one of those. These are the only ports with analog inputs, which sound sensors require. The sonar sensor has a yellow label, and all four ports have yellow, so a sonar will work in any of them.

Importantly, the ports are not interchangeable, so check which one you are using. When a lesson specifies a port, use that port; our programs expect sensors on the specified ports. mBlock also enforces these restrictions. If you add a sound sensor block, its port dropdown only offers ports 3 and 4, preventing serious errors even if you forget. The Block reference notes, for each block, which ports its dropdown offers.

Figure: The four RJ25 ports on top of the robot, where sensors plug in. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-the-robot-0c87735b.jpg))

Figure: Left: a sound sensor (with black label). Right: a sonar sensor (with yellow label). ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-the-robot-c0775633.jpg))

Figure: Cable for connecting sensors to the robot's ports. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-the-robot-676c1e4d.png))

The sound and color sensors require an mBlock extension before their blocks appear. Our example programs load the extension automatically. If you start from scratch, you must add it yourself. See Adding the sound sensor extension and Adding the color sensor extension.

## Switches and onboard sensors

The robot runs on four AA batteries. If you prefer not to replace batteries constantly, a rechargeable battery pack is also available; see the rechargeable battery pack below.

The on/off switch appears in the image below. The robot also has a USB port. As described later, you can also program via USB. However, the recommended method is wireless connection (see Getting started with the robot).

Figure: The location of the on/off switch and the USB port. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-the-robot-b3cee238.jpg))

Even without external sensors, the robot has several built-in inputs and outputs:

1. A light sensor that measures the amount of ambient light.
2. A small speaker that can play tones.
3. Two RGB LEDs, whose brightness and color you can set.
4. A button that your programs can read.

The image below shows where these components sit on the robot's main board. The board also includes an infrared receiver and transmitter, though our lessons do not use these.

Figure: The mBot's main board, the mCore, with its connectors and onboard devices labeled. Diagram by Makeblock. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/introduction-to-the-robot-51abd850.png))

## Optional: the rechargeable battery pack

By default, the robot runs on four AA batteries, but you can replace them with a rechargeable battery pack that charges via USB. This avoids repeatedly purchasing disposable batteries and takes only a few minutes per robot to install.

Figure: The battery pack. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/optional-using-the-battery-pack-b3a67c4f.jpg))

Begin by unplugging the AA battery holder from the robot. You must also unscrew the top board, so remove it now rather than later in the process.

Figure: The top board unscrewed and lifted clear, with the AA battery holder unplugged. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/optional-using-the-battery-pack-4f020b9a.jpg))

Clip the battery pack to the underside of the top board. Then connect it to the board using the red and black cables. The connector only fits in one orientation.

Figure: The pack clipped into the underside of the top board, with the red and black cables ready to plug in. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/optional-using-the-battery-pack-db21ceea.jpg))

Reattach the top board to the robot. The AA battery holder is no longer required.

Figure: The top board screwed back on, with the AA battery holder set aside. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/optional-using-the-battery-pack-b8f42f1d.jpg))

Charge the pack by connecting the robot to a USB power source. A red LED indicates charging in progress; it turns green when complete.

**Tip:** Do not charge the robot while it runs on the 4 x AA batteries.

Figure: Charging. Notice the red LED. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/optional-using-the-battery-pack-9d9b2d0d.jpg))

Figure: Charging complete. Note the green LED. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/optional-using-the-battery-pack-b758c100.jpg))

## Robot moving in the wrong direction?

If the robot moves backward when it should move forward, or turns left when it should turn right, the motor cables may be connected to the wrong ports.

To correct this:

1. Turn off the robot and disconnect the power source.
2. Locate the two motor connections on the main board, labeled `M1` and `M2`.
3. Verify the motor cable connections:
    - Left motor to `M1`
    - Right motor to `M2`
4. If reversed, unplug the cables and swap them.
5. Ensure both cables are securely seated.
6. Reconnect power and turn on the robot.
7. Test movement to confirm the correction.
