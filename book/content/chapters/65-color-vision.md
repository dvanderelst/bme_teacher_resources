# Color Vision

## Materials

| Item | Description |
| :--- | :--- |
| mBot Robot | The mBot robot |
| Bluetooth Dongle | This is a dongle that allows to connect to the robot from a computer. This is currently the recommended way to work with the robot. |
| Makeblock Color Sensor | This is a color sensor, providing a 3 channel readout of the light picked up. It’s used in the color vision lesson plan. |
| Goggles | Each group of three students should have a pair of red, green, and blue goggles. A group of students can have duplicate colors. |
| 3D printed brackets | These are brackets that allow sensors to be mounted on the front of the robot, in different orientations. |
| Screws | The robot use M4 machine screws. Students should be supplied with an ample supply of extra screws allowing to mount extra sensors. These screws are also used to mount the Robot Pipe Plate onto the PVC pipe. |
| Extra motors | Motors seem to be a component that fails from time to time. Students should be provided with replacement motors |
| Extra cables (short) | Extra cables for connecting sensors. This allows students to add sensors without removing cables and covers for losing cables.  The cables come in a pack of 4. I suggest supplying 1 extra cable per robot.  This cable is 20 cm long and has the same length as the 2 cables that come with the robot. |
| Lego compatible blocks | These blocks are compatible with the screws and the hole spacing used by the robot. Therefore these blocks allow students freedom in mounting sensors (as an alternative to the brackets we provide) |
| Colored paper | This paper can be used to build the tracks for the color vision robot activity. |
| Gaffers tape | It’s tape. What else can I say. It comes in handy everywhere. |
| Batteries | The robot takes 4 AA batteries. These should last a while. This is a 100 pack of AA batteries Providing more than 8 batteries per robot should allow swapping out the batteries and getting new stock without interruption to the curriculum. |

## Prerequisites

Basic biology course, some understanding of algorithmic thinking.

## Investigating / Essential Questions

- How does the human eye identify color?
- How can a robot be made to detect color?

## Educational Standards

The national and state educational standards applicable to this lesson are listed in the [Educational standards](#educational-standards) chapter.

## Learning Objectives

1. Explain how the human eye discriminates wavelengths of light.
2. Explain how a computer screen can fool you into seeing yellow when all it produces are red, green, and blue wavelengths of light.
3. Develop a computer algorithm based on an analysis of sensor comparisons to guide robot behavior and explain its parallels to human color discrimination.
4. Explain the advantage of using multiple sensors in biological and robotic color discrimination
5. Develop and test a robot that navigates using sensor comparisons.

## Introduction

Sensory biology as a field of study is concerned with how organisms obtain information about their environment. Specifically, how sense organs transduce energy from external stimuli to neural electrical signals. This unit examines the sense of color vision. Many animals have evolved color vision, which is the ability to discriminate between things based solely on the wavelengths of light they either emit or reflect. The mechanisms underlying color vision are well understood. Studies across organisms have led to a rich understanding of how animals vary in color perception ability and its importance in their daily behavior (Cronin et al., 2014). There are many examples of color used to evoke desired behaviors, such as human-made media advertisements that use color to get consumer attention and the development of artificial lures colored to attract different species of fish. The biological principles behind the detection of color have also been applied to engineering problems. For example, color sensors are used to check the colors of products in factories, allowing products to be automatically sorted and assessed for their type or quality.

This challenge-based unit aims to introduce students to the biological principles underlying color vision in animals and use engineering design to reinforce the principles learned. The unit also demonstrates to students how the working principles of color vision can be applied to autonomous robots. Groups of students participate in two activities that build foundational knowledge of how humans perceive color and how robots discriminate color to meet their engineering challenges.

- Part 1: Color discrimination game. In this activity, student groups participate in a computer game where each member wears goggles transmitting distinct wavelengths of light (red, blue, or green). This setup mimics the functioning of human cone cells. By wearing these goggles, students act as proxies for the cone cells of the human eye, each perceiving a different color range. Together, they collaborate to discern the color of objects in the game, simulating how the human eye perceives color through combined signals from different cone cells. The goal is for the students to collectively determine and agree upon the color of the objects they see based on their filtered perspectives.
- Part 2: Robot color discrimination. In this activity, student groups learn to program a robot that navigates a colored path using light sensors. The light sensor operates similarly to the human eye, with different detectors registering varying amounts of light wavelengths to determine color. The task involves programming the robot to follow a bicolored paper path using a color sensor. **This sensor, resembling the human eye, includes three light detectors for red, green, and blue light**, enabling the robot to stay centered on the path based on the color readings it receives.

This unit was created collaboratively with faculty from the University of Cincinnati College of Arts and Sciences, College of Engineering, and School of Education. Combining biology with engineering activities provides students with a unique opportunity to understand the parallels between animal and robot behavior and sensory/sensor function and addresses broad Next Generation Science Standards (NGSS Lead States, 2013) and International Society for Technology in Education Standards (International Society for Technology in Education, 2022).

## Background: color vision

Light is electromagnetic radiation with a wide range of frequencies/wavelengths, i.e., a wide spectrum. While a broad spectrum of wavelengths may be present in the environment, only a narrow range is visible to most animals. It is the particular mixture of wavelengths present within this range and animals’ ability to analyze them that determines the perceived color.

In humans, light enters the eye through the cornea, passes through the pupil, and finally is focused by the lens onto the retina. The retina contains rod and cone photoreceptor cells. The rod photoreceptor cells are important for peripheral vision and low light sensitivity, while three types of cone photoreceptor cells are used to perceive detail and color. The three types of cone cells are referred to as red, green, and blue cone cells. These color names refer to different wavelengths of light to which each of them is most sensitive. This difference in color sensitivity of the cone cells is due to their expression of different proteins called opsins. These opsins form a complex with another molecule called retinal, which forms the pigment called rhodopsin, which absorbs the light entering the eye. Differences in the amino acid sequence of the opsin proteins in the different cell types result in the cells' distinct sensitivities to wavelengths or colors of light; that is, it makes them more or less likely to absorb short (blue), medium (green) or long (red) wavelengths.

However, for an organism to have color vision, it is not sufficient to be sensitive to certain wavelengths of light. Rather, it means that the organism can tell the difference between the different wavelengths. To do this, the light absorbed by the rhodopsin in each cone cell is converted into electrical energy, and the amount of electrical excitation produced is compared by the eye and brain such that the color of the incoming light is determined. For example, consider a red object. That object looks red because it absorbs most wavelengths of visible light but reflects long wavelengths around 600-750 nanometers. This reflected light would stimulate the 'Red' cone cell (i.e., the longest wavelength sensitive cone in the human eye) because its rhodopsin absorbs those wavelengths, but not the 'Green' or 'Blue' cone cells because their rhodopsins do not. The brain interprets this activation pattern of the three cone cells as red. Using the same logic, light reflecting off a yellow object will stimulate the 'Red' and 'Green’ cones, but not the ‘Blue’ and forms a different pattern in the brain, resulting in the object being perceived as yellow. If all three cells are equally stimulated, the object is perceived as white (or if the light is low, gray).

> **Note**
>
> There is a PhET simulation by the University of Colorado, Boulder that could be used to further student understanding. It can be found here: [PhET Color Vision simulation](https://phet.colorado.edu/sims/html/color-vision/latest/color-vision_en.html)

> **Note**
>
> Here is another easily accessible intro to color vision:
>
> [How color vision happens in the eye (Medium)](https://medium.com/age-of-awareness/red-light-green-light-yellow-light-heres-how-it-happens-in-the-eye-and-how-to-teach-it-4e0c4bb96b8)

## Activity: color discrimination game

For this game, students work in groups of at least three. At least one person in a group should wear goggles with red filters, another with blue filters, and another with green filters. It is okay for more than one person to wear filters of a particular color. The filters in the goggles are important to the success of this activity. At the time of writing, the following three filters are used to create the goggles:

- Rosco E-Colour+ #736 Twickenham Green
- Rosco E-Colour+ #106 Primary Red
- Rosco E-Colour+ #071 Tokyo Blue

![Examples of goggles prepared with red, blue, and green filters.](images/color-vision-lesson-plan-4b0d8cdb.jpg)

By wearing goggles with a particular filter, a student acts as a proxy for one type of cone in the retina of humans and other animals. The goggles make them sensitive to a specific band of wavelengths, just like the different types of cones in the retina have different preferred wavelengths.

The goggles prevent a single student from discriminating various colors. Again, this is analogous to the cones in the retina: a single cone cell can not discriminate colors. It can only tell how much light in a specific wavelength band reaches it. As mentioned, the retina compares the activity across differently tuned cone cells to discriminate colors. Students can do something similar: by comparing how much light they see (how bright a color looks), they can collectively work out which color they are looking at.

### The app

Both halves of this activity live in one app: [colorvisionapp.up.railway.app](https://colorvisionapp.up.railway.app/). It needs nothing installed — any browser will do — and it opens on the screen below.

![The app's opening screen. `TRAIN` opens the trainer, `START` begins the competitive game, and the difficulty setting fixes how long each round allows.](images/color-vision-app-start.png)

`TRAIN` opens the trainer described next. `START` begins the competitive game described after it. Set the difficulty before starting: it decides how many seconds each round allows, and it multiplies the final score.

### Training game

Students use the trainer to get used to identifying colors together before they are timed on it.

![The trainer. The dropdown chooses the color of the large rectangle; beneath each pair of goggles is a box showing how that color looks through them. With RED selected, only the red goggles see anything.](images/color-vision-trainer.png)

The trainer shows a large colored rectangle, and below it three boxes, one under an image of each pair of goggles. Each box shows how the top color appears through those goggles. Students choose the color of the large rectangle from the dropdown.

Those three boxes show how much red, green and blue light the top color contains, which is the same thing as how strongly it would stimulate the red, green and blue cones in a retina. Select red, and the box under the red goggles is bright while the other two are black, because red light contains no green or blue. Select yellow, and the red and green boxes are bright while the blue one is dark — which is exactly why we see yellow when light stimulates the red and green cones but not the blue.

There are two ways to use this. With goggles off, students can see how a color looks to each of the others in the group. With goggles on, they can watch how the brightness of their own box changes as the color changes.

They should notice that one channel alone is not enough. The box under the red goggles looks equally bright for yellow and for red, so a student wearing red goggles — like a single cone cell — cannot tell those two apart. Distinguishing them takes more than one channel, and that is most obvious for the secondary colors: cyan, yellow and magenta.

Once students have explored, ask them to identify the color of the large rectangle without reading the label. The dropdown, or the up and down arrow keys, changes it. Start with the primaries — red, green, blue — and move on to the secondaries, each of which is a mixture of two primaries and so looks bright to two students and dark to the third.

The table below relates what the three students see, bright (+) or dark (-), to the actual color on screen.

![The key relating what each pair of goggles sees to the color on screen.](images/color-vision-lesson-plan-f1a76c67.png)

It helps to give students a blank copy to fill in as they work through the trainer:

[Color discrimination chart (.docx)](files/Color_Discrimination_Chart.docx)

### Competitive Game

After practising in the trainer, groups play the timed version to reinforce what they have learnt and to give them a reason to work quickly together. Wearing their goggles, they press `START`. Each round shows nine boxes of primary and secondary colors with a color named above them, and the group must select every box of that color.

![A round in progress. The named color is at the top, the ring above it shows the time left, and the group selects every box of that color.](images/color-vision-game.png)

The game runs ten rounds. Each round starts at 100 points and ticks down as an audible clock counts off, so the faster a group finds all the right boxes, the more of the 100 it keeps. Selecting a wrongly colored box costs 10 points and speeds the clock up, so a mistake is penalised twice. The ten rounds therefore total at most 1000, and that total is multiplied by the difficulty — Easy x1.0, Medium x1.5, Hard x2.0 — for a maximum of 2000 on Hard.

At the end, groups enter a team name and submit their score. Encourage them to play more than once and try to beat it.

![The final screen. The score is shown out of 1000 before the difficulty multiplier is applied.](images/color-vision-lesson-plan-67265ec6.png)

### Watching the scores come in

Submitted scores go to an instructor dashboard, reached from the `Instructor Dashboard` link at the foot of the app's opening screen.

![The `Instructor Dashboard` link sits at the bottom of the opening screen.](images/color-vision-dashboard-link.png)

![The dashboard asks for a password.](images/color-vision-dashboard-login.png)

Write to **Dieter Vanderelst** at [vanderdt@ucmail.uc.edu](mailto:vanderdt@ucmail.uc.edu) for the password. Once you are in, pick the date or dates your class is playing, and the dashboard lists every team's score for those days, refreshing every ten seconds or so. Left on a projector, it becomes a live leaderboard, which is worth doing: groups play again to climb it.

![The dashboard, with team names blurred here. Choose one or more dates on the left, and the scores appear on the right, highest first.](images/color-vision-dashboard-scores.png)

> **Note**
>
> Every teacher using the dashboard shares the same one, so you will see other schools' scores alongside your own — picking your dates is what filters it down to your class. Ask groups to invent a team name rather than use their own names, which keeps the board readable and is more fun anyway.

## Activity: robot color discrimination

### Introduction

Explain to students that their task is to program a robot to follow a bicolored path constructed of paper, using a color sensor to keep the robot in the middle of the path. The task is illustrated in the figure below.

Students will create a path of two different colors of paper (red and green in the example below). Next, they will program the robot to stay in the middle of the path. This can be done by programming the robot to turn left or right, depending on which color the color sensor detects. In the example below, the robot should turn right if the sensor detects green and left if the sensor detects the red paper.

![The task. The color sensor points down at the boundary between the two colors, and the robot steers to keep it there.](images/color-vision-lesson-plan-998025db.png)

### Operation of the color sensor

Students can find detailed [information on the operation of the color sensor](https://www.mouser.co.uk/datasheet/2/348/bh1745nuc-e-519994.pdf) online. However, in brief, the Me color sensor consists of three different light detectors registering the amount of red, green, and blue light. As we know, this information can be used to discriminate colors and recognize which color the paper under the robot is.

Give students time to install the color sensor instead of the Line follower sensor depicted in the generic instructions. Students should not over-tighten the screws when installing the color sensor because the caster wheel rests on some of the electronic components on the sensor board. This may cause the wheel not to move or the electronic component to get damaged. See below for images of the color sensor installed on the robot.

![The color sensor mounted at the front of the robot, facing down.](images/color-vision-lesson-plan-a15b7f94.jpg)

![The same sensor seen from underneath, between the two motors. Its two white LEDs light the paper so the reading does not depend on the room.](images/color-vision-lesson-plan-bf6d4571.jpg)

Students also construct a bicolored path using colored paper and tape so that each side of the path is a different color. This is illustrated in the drawing above. [An example is also shown in the video at the end of this guide](#color-vision).

### Procedure

The color sensor can only be used in the so-called `Upload` mode. This means programs must be uploaded to the robot using a USB cable. We can then disconnect the cable, and the robot is entirely autonomous. From then on, every time we switch on the robot, it will run the uploaded program without communication with your computer. More information about the different modes the robot can operate in is [available here](#getting-started-with-the-robot).

The fact that the sensor can only be used in `Upload` mode makes programming the robot harder. The main issue is that one cannot observe sensor values while our program runs and the robot is not connected using a USB cable. This makes it challenging to pick the correct sensor values to respond to.

To solve this issue, we will proceed in three steps, which are the three sections that follow. First, students run a program that displays the sensor's current values while the robot is connected to the computer via a USB cable. Second, they interpret those readings to work out a rule that tells the two colors apart. Third, they program the robot using that rule and disconnect the cable, so that from then on the robot follows the track on its own.

> **Tip**
>
> If you use the programs below, the mBlock software will load an extension that allows you to work with the color sensor. To start programming from scratch, you must add the extension yourself. Click the following link for instructions:
>
> [Adding color sensor extension](#adding-color-sensor-extension)

#### Step 1: Inspecting the color sensor values

> **Note**
>
> Ensure the color sensor is connected to port 2 on the robot.

1. Open the program in mBlock, in the browser or installed. Either link works, and [Step 1: Open the example program](#step-1-open-the-example-program) explains what to do with each.

    [Open the mBlock project](https://planet.mblock.cc/project/3954097). If your school blocks the Makeblock site, [download `color_vision_communication.mblock`](files/programs/color_vision_communication.mblock) instead.

2. In mBlock, select mBot under the Devices tab on the left side of the screen. This will show the robot's code. Do not unplug the cable during this part of the activity.

    ![Make sure you select the mBot under the Devices tab to see the code for the robot.](images/color-vision-lesson-plan-a5e7ceb3.png)

3. Connect to the robot using the USB cable. see [Getting started with the robot](#getting-started-with-the-robot) for instructions on connecting over the USB cable.
4. Upload the code to the robot by selecting the `Upload` mode and clicking `Upload code`.

![Select the mBot in `Devices`, switch to `Upload`, then click `Upload Code`.](images/color-vision-lesson-plan-4d4b0a0b.png)

![The upload in progress. It takes a few moments, and the robot cannot be used until it finishes.](images/color-vision-lesson-plan-41a422cc.png)

Once the code has been uploaded to the robot, you should see the robot’s white light coming on every second. This indicates that the robot is collecting data using the color sensor. Keep the USB cable plugged in. Also, mBlock should show a graph view that visualizes the amount of red, green, and blue light the color sensor picks up. The same values also appear on the stage, at the top left of the mBlock window. Both are shown below.

![mBlock's chart view, showing how much red, green and blue light the sensor is picking up.](images/color-vision-lesson-plan-8d5aeda8.png)

![The same three readings on the stage. They are labelled `Panda:` because the variables belong to the panda sprite.](images/color-vision-lesson-plan-d29948b8.png)

With the robot connected to the computer through the USB cable, we can now collect data to check how the color sensor sees the two different colors of paper. Ask students to draw a few lines spanning the border between the two colors of paper spaced by about 1 cm. For example, in the figure below, we have drawn 7 marks spaced by 1 cm.

![Marks drawn across the boundary about 1 cm apart. Here there are seven, from 3 cm into the green to 3 cm into the red.](images/color-vision-lesson-plan-9e9eb54f.png)

Students can now observe how the values for the red, green, and blue light change as the robot is placed and aligned with each mark. For example, in the image below, the robot is aligned with the left most marker.

![The robot lined up with one of the marks. The sensor's own lights show which patch of paper it is reading.](images/color-vision-lesson-plan-c1d3a88e.jpg)

The aim is to observe how the sensor readings change as the robot moves from one color of paper to the other color (here, green to red). Below, we include some measurements collected using the setup depicted in the images above. We have also included a column that shows the difference between the red and green values.

Students can record this on paper or in whatever spreadsheet software the school already uses — the table is six columns and a handful of rows, and a spreadsheet has the advantage of plotting the last column for them, which is what the next step needs.

| Marker | Position | Red | Green | Blue | Red – Green |
| --- | --- | --- | --- | --- | --- |
| 1 | -3 cm | 17 | 33 | 19 | -16 |
| 2 | -2 cm | 18 | 33 | 19 | -15 |
| 3 | -1 cm | 22 | 32 | 19 | -10 |
| 4 | 0 cm | 35 | 26 | 15 | 9 |
| 5 | 1 cm | 58 | 17 | 9 | 41 |
| 6 | 2 cm | 64 | 14 | 8 | 50 |
| 7 | 3 cm | 64 | 14 | 7 | 50 |

There are a few things to observe. The students’ values might differ depending on the paper's color. Notice that for each paper, all channels have a value larger than 0, indicating that each paper also reflects some amount of other wavelengths of light.

![The three channels as the sensor crosses the boundary. Red rises and green falls, while blue changes comparatively little.](images/color-vision-lesson-plan-44ef58b4.png)

Now that students have some baseline data, they must develop their algorithm and program the robot to follow the midline. Give students time to write a rule that would direct the robot when to turn right or left based on their data. Check student work before moving on. Students should have something similar to the example explanation below.

#### Step 2: Interpreting the data

In the above example, the set-up consisted of green paper on the left and red on the right. Here, we will derive a rule that keeps the robot on the centerline between the papers using the difference between the Red and Green channels.

> **Note**
>
> In principle, the current challenge can also be solved by only looking at the amount of red light. Indeed, as can be seen from the graph, if the robot picks up a lot of red light, it is on the red paper. If the intensity of the red light is lower, it is on the green paper. However, when students use paper in colors other than the primary colors (red, green, and blue), a single color channel might not be sufficient to discriminate the colors, and different channels must be compared. Moreover, true color vision relies on comparing different color channels (refer to the discussion of color vision in animals and the rationale of the color vision games) Therefore, the example here also uses a comparison between color channels.

Below, we have plotted the difference between Red and Green as a function of the robot's position. From this graph, we can derive a rule to keep the robot on the center line.

![The difference between red and green across the same positions. This is the curve the steering rule is read off: strongly negative on the green, strongly positive on the red, crossing zero near the middle.](images/color-vision-lesson-plan-2a426533.png)

This is a potential rule:

```text
If Red - Green < -10: turn right
If Red - Green > 40: turn left
```

This rule turns the robot right if it detects more green light than red and vice versa. Once students have devised a rule like this, they can implement it in the robot.

#### Step 3: Programming the robot

Below, we link a program that implements the rule we have derived above. Students’ programs could look similar but should be changed to reflect the rules they derived.

Students starting from scratch rather than from the example program will need to add the color sensor extension first, which is described in [Adding color sensor extension](#adding-color-sensor-extension) at the end of this chapter.

[Open the mBlock project](https://planet.mblock.cc/project/3954308). If your school blocks the Makeblock site, [download `color_vision_motion.mblock`](files/programs/color_vision_motion.mblock) instead.

The program is shown below. The first blocks read the red, green, and blue values detected by the color sensor. The purple block sets the onboard lights to a color that mimics the color seen by the color sensor, which should help debug the program. Next, the robot is set to move forward at a slow speed. Immediately after this, we check the value of red-green. Depending on this result, the robot is turned left or right. See below for a video demonstrating the behavior of the robot.

> **Note**
>
> It helps to keep the robot's speed low. This gives it more time to measure and respond to the color. For example, in the example, we set the power to 25%. This might make it difficult for the robot to get started. To help it start moving, you could give it a small push.

To run the example program (or the students’ program), upload the program to the robot. Once the program is uploaded, the USB cable can be disconnected. To change the program, connect the USB cable to the robot and upload the new program.

![One solution. The three channels are read into variables, the LEDs are set to the color the sensor reports, and the robot turns right or left when the red-minus-green difference passes the thresholds taken from the graph.](images/color-vision-lesson-plan-8649dc81.png)

![The robot following the boundary between the two colors. The onboard LEDs are set to the color the sensor is reporting, which makes it possible to see what the robot thinks it is looking at.](images/color-vision-path-following.png)

[Video: the robot following the path (.mp4)](files/color_vision_path_following.mp4)

### Taking it further

Several extensions to the lesson plan can be made:

1. The track's end and start can be constructed of a third color. When the robot detects this color, it can be programmed to turn 180 degrees to return to the other end of the path.
2. The white LEDs on the me color sensor can be switched off. Remember, the LEDs deliver a uniform fixed and broad-spectrum light onto the floor, making the sensor’s ability to color discriminate easier. But, consider a real-life scenario where a robot tries to detect whether the floor underneath it is red or yellow, but the light in the environment is variable or suboptimal. If the lighting is poor, the overhead lamps might not emit sufficient yellow light, so the light reflecting from the floor will contain little yellow light. The sensor will have difficulty discriminating yellow from red. The following block can be used to switch off the white LEDs.

    ![The block that switches the sensor's white fill LEDs off. Note that the port dropdown reads `port1` in this screenshot; set it to the port the color sensor is actually plugged into, which is port 2 everywhere else in this chapter.](images/color-vision-lesson-plan-5972c66e.png)

3. Altering the colors in the path to include secondary colors such as cyan, yellow, and/or magenta.

## Adding color sensor extension

The blocks that read the color sensor are not in mBlock to begin with; they arrive as an extension. Opening one of our programs loads it for you, so this is only needed when starting a program from scratch.

First make sure the mBot has been added to mBlock — see [Adding the mBot to mBlock](#adding-the-mbot-to-mblock) — and that it is the device selected in the `Devices` panel, because extensions are added to a particular device.

Then click the `+` button at the bottom of the block palette, find `color sensor` in the list that appears, and click `Add`.

![The `+` button at the foot of the block palette opens the extension list.](images/adding-color-sensor-extension-4c6bddee.png)

![Find the color sensor extension and click `Add`.](images/adding-color-sensor-extension-2578cd3c.png)

![A new category appears in the palette, holding the blocks that read the color sensor.](images/adding-color-sensor-extension-7d2f1d27.png)

> **Tip**
>
> The color sensor works only in `Upload` mode, not in `Live` mode. See [Live versus Upload mode](#live-versus-upload-mode).
