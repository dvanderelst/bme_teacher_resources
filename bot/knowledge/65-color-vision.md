---
chapter: "Color Vision"
source: 65-color-vision.md
edition: "27 July 2026"
fingerprint: "677bb65-stale"
---

# Color Vision

## Materials

| Item | Description |
| :--- | :--- |
| mBot Robot | The mBot robot. |
| Bluetooth Dongle | A dongle for connecting the robot to a computer. Currently the recommended connection method. |
| Makeblock Color Sensor | A color sensor providing three-channel RGB readouts. Used in the color vision lesson. |
| Goggles | Each group needs at least one pair of red, green, and blue goggles. Groups may have duplicate colors. |
| 3D printed brackets | Brackets for mounting sensors on the front of the robot in different orientations. |
| Screws | The robot uses M4 machine screws. Provide extra screws for mounting additional sensors and the Robot Pipe Plate onto PVC pipe. |
| Extra motors | Motors occasionally fail. Provide replacement motors for students. |
| Extra cables (short) | Extra cables for connecting sensors. These allow students to add sensors without removing existing connections, preventing lost cables. Cables come in packs of 4; supply 1 extra per robot. Each is 20 cm long, matching the two cables included with the robot. |
| Lego compatible blocks | Blocks compatible with the robot's screw holes. These provide flexibility for mounting sensors as an alternative to the provided brackets. |
| Colored paper | Paper for building tracks for the color vision robot activity. |
| Gaffer's tape | Versatile tape useful throughout the activities. |
| Batteries | The robot requires 4 AA batteries. A 100-pack provides sufficient spares: with more than 8 batteries per robot, you can swap batteries without interrupting the curriculum. |

## Prerequisites

Basic biology course, some understanding of algorithmic thinking.

## Investigating / Essential Questions

- How does the human eye identify color?
- How can a robot be made to detect color?

## Educational Standards

The national and state educational standards applicable to this lesson are listed in the Educational standards chapter.

## Learning Objectives

1. Explain how the human eye discriminates wavelengths of light.
2. Explain how a computer screen can fool you into seeing yellow when all it produces are red, green, and blue wavelengths of light.
3. Develop a computer algorithm based on an analysis of sensor comparisons to guide robot behavior and explain its parallels to human color discrimination.
4. Explain the advantage of using multiple sensors in biological and robotic color discrimination
5. Develop and test a robot that navigates using sensor comparisons.

## Introduction

Sensory biology studies how organisms obtain information from their environment, specifically how sense organs transduce energy from external stimuli into neural electrical signals. This unit focuses on color vision, the ability to discriminate between objects based on the wavelengths of light they emit or reflect. Many animals have evolved this capability, and the mechanisms are well understood. Studies across organisms have revealed how color perception varies among animals and its importance in daily behavior (Cronin et al., 2014). Color is also used to evoke desired behaviors in human applications, from advertisements using color to attract consumer attention to artificial lures designed to attract specific fish species. These same biological principles have been applied to engineering challenges, such as using color sensors in factories to sort and assess products by type or quality.

This challenge-based unit introduces students to the biological principles of color vision and uses engineering design to reinforce those principles. It also demonstrates how color vision principles apply to autonomous robots. Students participate in two activities that build foundational knowledge of color perception in humans and robots:

- **Part 1: Color discrimination game.** Students work in groups, each wearing goggles that transmit distinct wavelengths (red, blue, or green). This setup mimics human cone cells. Each student perceives a different color range, and together they collaborate to identify the colors of objects in a computer game, simulating how the human eye perceives color through combined signals from different cone cells. The goal is for students to collectively determine the color of objects based on their filtered perspectives.
- **Part 2: Robot color discrimination.** Students program a robot to navigate a bicolored paper path using a color sensor. Like the human eye, this sensor has three detectors for red, green, and blue light, enabling the robot to stay centered on the path based on its color readings.

This unit was created collaboratively with faculty from the University of Cincinnati College of Arts and Sciences, College of Engineering, and School of Education. Combining biology with engineering gives students a unique opportunity to understand the parallels between animal and robot behavior, sensory and sensor function, and addresses Next Generation Science Standards (NGSS Lead States, 2013) and International Society for Technology in Education Standards (International Society for Technology in Education, 2022).

## Background: color vision

Light is electromagnetic radiation with a wide spectrum of frequencies and wavelengths. While a broad spectrum may be present in the environment, only a narrow visible range can be detected by most animals. The particular mixture of wavelengths within this range, combined with an animal's ability to analyze them, determines the perceived color.

In humans, light enters the eye through the cornea, passes through the pupil, and is focused by the lens onto the retina. The retina contains rod and cone photoreceptor cells. Rod cells enable peripheral vision and low-light sensitivity, while three types of cone cells enable detailed vision and color perception. These cone types are commonly referred to as red, green, and blue cones, names that indicate the wavelengths to which each is most sensitive. This difference in sensitivity arises from the expression of different proteins called opsins. Each opsin forms a complex with retinal, creating the pigment rhodopsin, which absorbs incoming light. Differences in the amino acid sequences of opsin proteins among cell types create distinct wavelength sensitivities: short wavelengths for blue, medium for green, and long for red.

However, for an organism to have color vision, it is not enough to be sensitive to certain wavelengths. Rather, it means the organism can distinguish between different wavelengths. To do this, light absorbed by rhodopsin in each cone cell is converted into electrical energy, and the resulting excitation levels are compared by the eye and brain to determine the color of incoming light. For example, a red object absorbs most visible wavelengths but reflects long wavelengths around 600-750 nanometers. This reflected light stimulates the red cone cell because its rhodopsin absorbs those wavelengths, but not the green or blue cone cells because their rhodopsins do not. The brain interprets this activation pattern as red. Similarly, light reflecting off a yellow object stimulates the red and green cones but not the blue, creating a different pattern that the brain perceives as yellow. If all three cones are equally stimulated, the object appears white (or gray in low light).

**Note:** There is a PhET simulation by the University of Colorado, Boulder that could be used to further student understanding. It can be found here: [PhET Color Vision simulation](https://phet.colorado.edu/sims/html/color-vision/latest/color-vision_en.html)

**Note:** Here is another easily accessible intro to color vision:

[How color vision happens in the eye (Medium)](https://medium.com/age-of-awareness/red-light-green-light-yellow-light-heres-how-it-happens-in-the-eye-and-how-to-teach-it-4e0c4bb96b8)

## Activity: color discrimination game

Students work in groups of at least three, with each group member wearing goggles with a different filter: red, blue, or green. Multiple students can wear the same color filter. The filters are critical to this activity. At the time of writing, the goggles use these three Rosco E-Colour+ filters:

- Rosco E-Colour+ #736 Twickenham Green
- Rosco E-Colour+ #106 Primary Red
- Rosco E-Colour+ #071 Tokyo Blue

Figure: Examples of goggles prepared with red, blue, and green filters. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-4b0d8cdb.jpg))

Each student wearing a particular filter acts as a proxy for one cone type in the human retina. The goggles make them sensitive to a specific wavelength band, mimicking how different cone types have different preferred wavelengths.

The goggles prevent a single student from discriminating colors, analogous to how a single cone cell cannot discriminate colors. A cone cell only detects the amount of light in its specific wavelength band. The retina compares activity across differently tuned cone cells to determine color. Students can do the same: by comparing how much light they see (the brightness of a color), they can collectively identify which color they are viewing.
### The app
### The app

Both halves of this activity run in a single app: [colorvisionapp.up.railway.app](https://colorvisionapp.up.railway.app/). It requires no installation — any browser works — and opens to the screen below.

Figure: The app's opening screen. `TRAIN` opens the trainer, `START` begins the competitive game, and the difficulty setting determines how long each round allows. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-app-start.png))

`TRAIN` opens the trainer described next. `START` begins the competitive game described after it. Set the difficulty before starting: it determines how many seconds each round allows and multiplies the final score.

### Training game

Students use the trainer to practice identifying colors together before being timed.

Figure: The trainer. The dropdown selects the color of the large rectangle; beneath each pair of goggles is a box showing how that color appears through them. With RED selected, only the red goggles see anything. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-trainer.png))

The trainer displays a large colored rectangle with three boxes below it, one under each pair of goggles. Each box shows how the top color appears through those goggles. Students select the rectangle's color from the dropdown.

These three boxes display the red, green, and blue light content of the top color, which corresponds to how strongly it would stimulate red, green, and blue cones in a retina. Select red, and the box under the red goggles is bright while the other two are black, because red light contains no green or blue. Select yellow, and the red and green boxes are bright while the blue one is dark — which is exactly why we see yellow when light stimulates the red and green cones but not the blue.

There are two ways to use this. Without goggles, students can see how a color appears to each group member. With goggles on, they can watch how the brightness of their own box changes as the color changes.

They should notice that one channel alone is insufficient. The box under the red goggles looks equally bright for yellow and red, so a student wearing red goggles — like a single cone cell — cannot distinguish between them. This is most obvious for secondary colors: cyan, yellow, and magenta.

Once students have explored, ask them to identify the color of the large rectangle without reading the label. The dropdown, or the up and down arrow keys, changes it. Start with the primaries (red, green, blue) and move on to the secondaries. Each secondary color is a mixture of two primaries, appearing bright to two students and dark to the third.

The table below relates what the three students see, bright (+) or dark (-), to the actual color on screen.

Figure: The key relating what each pair of goggles sees to the color on screen. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-f1a76c67.png))

It helps to give students a blank copy to fill in as they work through the trainer:

[Color discrimination chart (.docx)](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/files/Color_Discrimination_Chart.docx)

### Competitive Game

After practicing in the trainer, groups play the timed version to reinforce what they have learned and to encourage quick teamwork. Wearing their goggles, they press `START`. Each round displays nine boxes of primary and secondary colors with a color name above them, and the group must select every box of that color.

Figure: A round in progress. The named color is at the top, the ring above it shows the time left, and the group selects every box of that color. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-game.png))

The game runs ten rounds. Each round starts at 100 points and ticks down as an audible clock counts off, so the faster a group finds all the correct boxes, the more points it retains. Selecting a wrong color costs 10 points and speeds up the clock, penalizing mistakes twice. The ten rounds therefore total at most 1000 points, and this total is multiplied by the difficulty setting — Easy ×1.0, Medium ×1.5, Hard ×2.0 — for a maximum of 2000 on Hard.

At the end, groups enter a team name and submit their score. Encourage them to play more than once and try to beat their previous score.

Figure: The final screen. The score is shown out of 1000 before the difficulty multiplier is applied. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-67265ec6.png))

### Watching the scores come in

Submitted scores appear on an instructor dashboard, accessed via the `Instructor Dashboard` link at the bottom of the app's opening screen.

Figure: The `Instructor Dashboard` link sits at the bottom of the opening screen. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-dashboard-link.png))

Figure: The dashboard asks for a password. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-dashboard-login.png))

Write to **Dieter Vanderelst** at vanderdt@ucmail.uc.edu for the password. Once logged in, select the date or dates your class is playing, and the dashboard lists every team's score for those days, refreshing every ten seconds or so. Left on a projector, it becomes a live leaderboard, encouraging groups to play again to climb the rankings.

Figure: The dashboard, with team names blurred here. Choose one or more dates on the left, and the scores appear on the right, highest first. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-dashboard-scores.png))

**Note:** Every teacher using the dashboard shares the same one, so you will see other schools' scores alongside your own. Picking your dates filters it to show only your class. Ask groups to invent a team name rather than use their own names, which keeps the board readable and is more fun.
## Activity: robot color discrimination

### Introduction

Students program a robot to follow a bicolored paper path using a color sensor to keep the robot centered. The task is illustrated below.

Students create a path using two different colors of paper (red and green in the example). They then program the robot to stay in the middle by turning left or right based on the color sensor's readings. In the example, the robot turns right when the sensor detects green and left when it detects red.

Figure: The task. The color sensor points down at the boundary between the two colors, and the robot steers to keep it there. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-998025db.png))

### Operation of the color sensor

Students can find detailed [information on the color sensor's operation](https://www.mouser.co.uk/datasheet/2/348/bh1745nuc-e-519994.pdf) online. In brief, the Me color sensor has three light detectors that register the amount of red, green, and blue light. This information can be used to discriminate colors and identify the color of the paper under the robot.

Give students time to install the color sensor instead of the line follower sensor shown in the generic instructions. Caution students not to over-tighten the screws, as the caster wheel rests on some of the electronic components on the sensor board. This can prevent the wheel from moving or damage the components. See below for images of the color sensor installed on the robot.

Figure: The color sensor mounted at the front of the robot, facing down. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-a15b7f94.jpg))

Figure: The same sensor seen from underneath, between the two motors. Its two white LEDs light the paper so the reading does not depend on the room lighting. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-bf6d4571.jpg))

Students also construct a bicolored path using colored paper and tape, with each side a different color as illustrated above. An example is also shown in the video at the end of this guide.

### Procedure

The color sensor only works in `Upload` mode. Programs must be uploaded to the robot using a USB cable, which can then be disconnected. The robot then runs the uploaded program autonomously. Every time the robot is switched on, it will run this program without needing computer communication. More information about the robot's operational modes is available here.

The fact that the sensor only works in `Upload` mode makes programming more challenging. The main issue is that sensor values cannot be observed while the program runs without a USB connection. This makes it difficult to identify the correct sensor values to respond to.

To solve this issue, we will proceed in three steps, which are the three sections that follow. First, students run a program that displays the sensor's current values while the robot is connected to the computer via a USB cable. Second, they interpret those readings to work out a rule that tells the two colors apart. Third, they program the robot using that rule and disconnect the cable, so that from then on the robot follows the track on its own.

**Tip:** If you use the programs below, the mBlock software will load an extension that allows you to work with the color sensor. To start programming from scratch, you must add the extension yourself. Click the following link for instructions:

Adding color sensor extension

**Tip:** If you use the programs below, the mBlock software will automatically load an extension that allows you to work with the color sensor. To start programming from scratch, you must add the extension yourself. Click the following link for instructions:

Adding color sensor extension

#### Step 1: Inspecting the color sensor values

**Note:** Ensure the color sensor is connected to port 2 on the robot.

1. Open the program in mBlock, either in the browser or installed version. Either link works, and Step 1: Open the example program explains what to do with each.

    [Open the mBlock project](https://planet.mblock.cc/project/3954097). If your school blocks the Makeblock site, [download `color_vision_communication.mblock`](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/files/programs/color_vision_communication.mblock) instead.

2. In mBlock, select mBot under the Devices tab on the left side of the screen. This displays the robot's code. Do not unplug the cable during this part of the activity.

    Figure: Make sure you select the mBot under the Devices tab to see the code for the robot. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-a5e7ceb3.png))

3. Connect to the robot using the USB cable. See Getting started with the robot for USB connection instructions.
4. Upload the code to the robot by selecting `Upload` mode and clicking `Upload code`.

Figure: Select the mBot in `Devices`, switch to `Upload`, then click `Upload Code`. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-4d4b0a0b.png))

Figure: The upload in progress. It takes a few moments, and the robot cannot be used until it finishes. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-41a422cc.png))

Once uploaded, the robot's white light should flash every second, indicating it is collecting data using the color sensor. Keep the USB cable plugged in. mBlock will display a graph view showing the red, green, and blue light readings from the color sensor. These values also appear on the stage, at the top left of the mBlock window.

Figure: mBlock's chart view, showing how much red, green and blue light the sensor is picking up. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-8d5aeda8.png))

Figure: The same three readings on the stage. They are labelled `Panda:` because the variables belong to the panda sprite. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-d29948b8.png))

With the robot connected to the computer via USB cable, students can now collect data on how the color sensor perceives the two different paper colors. Ask students to draw a few lines spanning the border between the two colors, spaced about 1 cm apart. For example, the figure below shows 7 marks spaced by 1 cm.

Figure: Marks drawn across the boundary about 1 cm apart. Here there are seven, from 3 cm into the green to 3 cm into the red. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-9e9eb54f.png))

Students can now observe how the red, green, and blue values change as the robot is placed and aligned with each mark. For example, in the image below, the robot is aligned with the leftmost marker.

Figure: The robot lined up with one of the marks. The sensor's own lights show which patch of paper it is reading. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-c1d3a88e.jpg))

The goal is to observe how sensor readings change as the robot moves from one color to the other (here, green to red). Below are example measurements using the setup shown above, including a column showing the difference between red and green values.

Students can record this in a spreadsheet (the table has six columns and a handful of rows). A spreadsheet has the advantage of automatically plotting the last column, which is what the next step requires.

| Marker | Position | Red | Green | Blue | Red – Green |
| --- | --- | --- | --- | --- | --- |
| 1 | -3 cm | 17 | 33 | 19 | -16 |
| 2 | -2 cm | 18 | 33 | 19 | -15 |
| 3 | -1 cm | 22 | 32 | 19 | -10 |
| 4 | 0 cm | 35 | 26 | 15 | 9 |
| 5 | 1 cm | 58 | 17 | 9 | 41 |
| 6 | 2 cm | 64 | 14 | 8 | 50 |
| 7 | 3 cm | 64 | 14 | 7 | 50 |

Note that student values might differ depending on the paper colors used. For each paper, all channels have values greater than 0, indicating that each paper reflects some light from other wavelengths as well.

Figure: The three channels as the sensor crosses the boundary. Red rises and green falls, while blue changes comparatively little. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-44ef58b4.png))

Now that students have baseline data, they must develop an algorithm to program the robot to follow the midline. Give students time to write a rule for when the robot should turn right or left based on their data. Check student work before moving on. Students should have something similar to the example below.

#### Step 2: Interpreting the data

In the example above, the setup uses green paper on the left and red on the right. Here, we derive a rule that keeps the robot on the centerline using the difference between the Red and Green channels.

**Note:** In principle, this challenge can also be solved by looking only at the red light amount. As the graph shows, if the robot detects much red light, it is on the red paper; if less, it is on the green paper. However, when students use non-primary paper colors, a single channel may not be sufficient. Moreover, true color vision relies on comparing different color channels (refer to the animal color vision discussion and the color vision games). Therefore, this example uses a comparison between color channels.

Below, we plot the difference between Red and Green as a function of robot position. From this graph, we can derive a rule to keep the robot on the center line.

Figure: The difference between red and green across the same positions. This is the curve the steering rule is read off: strongly negative on the green, strongly positive on the red, crossing zero near the middle. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-2a426533.png))

A potential rule:

```text
If Red - Green < -10: turn right
If Red - Green > 40: turn left
```

This rule turns the robot right if it detects more green light than red, and vice versa. Once students have devised a similar rule, they can implement it in the robot.

#### Step 3: Programming the robot

Below is a link to a program that implements the rule derived above. Student programs could look similar but should reflect the rules they created.

Students starting from scratch rather than from the example program will need to add the color sensor extension first, described in Adding color sensor extension at the end of this chapter.

[Open the mBlock project](https://planet.mblock.cc/project/3954308). If your school blocks the Makeblock site, [download `color_vision_motion.mblock`](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/files/programs/color_vision_motion.mblock) instead.

The program works as follows. The first blocks read the red, green, and blue values detected by the color sensor. The purple block sets the onboard lights to a color that mimics the color seen by the color sensor, which helps debug the program. Next, the robot is set to move forward at a slow speed. Immediately after this, the red-minus-green value is checked. Based on this result, the robot turns left or right. See the video below for a demonstration.

**Note:** Keeping the robot's speed low helps. This gives it more time to measure and respond to color. For example, the sample uses 25% power. This might make it difficult for the robot to start moving. To help, you could give it a small push.

To run the example program (or a student's program), upload it to the robot. Once uploaded, the USB cable can be disconnected. To change the program, reconnect the USB cable and upload the new version.

Figure: One solution. The three channels are read into variables, the LEDs are set to the color the sensor reports, and the robot turns right or left when the red-minus-green difference passes the thresholds taken from the graph. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-8649dc81.png))

Figure: The robot following the boundary between the two colors. The onboard LEDs are set to the color the sensor is reporting, making it possible to see what the robot thinks it is looking at. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-path-following.png))

[Video: the robot following the path (.mp4)](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/files/color_vision_path_following.mp4)

### Taking it further

The lesson can be extended in several ways:

1. Construct the track's end and start with a third color. Program the robot to turn 180 degrees when it detects this color to return to the other end of the path.
2. Switch off the white LEDs on the color sensor. Normally, these LEDs provide uniform, broad-spectrum light, making color discrimination easier. However, consider a real-world scenario where a robot must detect whether the floor is red or yellow under variable or suboptimal lighting. With poor lighting, overhead lamps may not emit sufficient yellow light, so reflected light from the floor will contain little yellow. The sensor will then struggle to distinguish yellow from red. Use the following block to switch off the white LEDs:

    Figure: The block that switches the sensor's white fill LEDs off. Note that the port dropdown reads `port1` in this screenshot; set it to the port the color sensor is actually plugged into, which is port 2 everywhere else in this chapter. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/color-vision-lesson-plan-5972c66e.png))

3. Use secondary colors such as cyan, yellow, and/or magenta in the path.

## Adding color sensor extension

The blocks for the color sensor are not in mBlock by default; they are added via an extension. Opening one of our programs loads this extension automatically, so this step is only needed when starting a program from scratch.

First, ensure the mBot has been added to mBlock — see Adding the mBot to mBlock — and that it is selected in the `Devices` panel, as extensions are added to a specific device.

Then, click the `+` button at the bottom of the block palette, find `color sensor` in the list, and click `Add`.

Figure: The `+` button at the foot of the block palette opens the extension list. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/adding-color-sensor-extension-4c6bddee.png))

Figure: Find the color sensor extension and click `Add`. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/adding-color-sensor-extension-2578cd3c.png))

Figure: A new category appears in the palette, holding the blocks that read the color sensor. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/adding-color-sensor-extension-7d2f1d27.png))

**Tip:** The color sensor only works in `Upload` mode, not in `Live` mode. See Live versus Upload mode.
