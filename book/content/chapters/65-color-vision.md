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
| Gaffers tape | It’s tape. What else can I say. I comes in handy everywhere. |
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
> There is a PhET simulation by the University of Colorado, Boulder that could be used to further student understanding. It can be found at this link: [https://phet.colorado.edu/sims/html/color-vision/latest/color-vision_en.html](https://phet.colorado.edu/sims/html/color-vision/latest/color-vision_en.html)

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

### Training game

Students can use the color vision training app to familiarize themselves with how to identify colors collectively. Open the app at the link below; its **TRAIN** button leads to the trainer described here, and its **START** button launches the competitive game described further down.

[NiceGUI](https://colorvisionapp.up.railway.app/)

The trainer shows a large colored rectangle at the top and, below it, three boxes — one beneath an image of each pair of goggles (red, green, and blue) (see screenshot below). Each lower box shows how the top color appears through that pair of goggles. The students can select a different color for the large rectangle using a dropdown box.

![](images/color-vision-lesson-plan-6d594ed2.png)

The bottom rectangle displays the amounts of red, green, and blue light in the top rectangle's current color (as seen through the red, green, and blue goggles). For example, if the students select red for the rectangle color, the left square would be bright red. The two other rectangles would be black. This is because the red color shown does not contain green and blue light. If they choose yellow for the rectangle, the rightmost square would be dark. The left and middle rectangles would be bright red and green, respectively. Another way of thinking about the function of the rectangle at the bottom is to consider it as showing the level of stimulation provided by the top color to the red, green, and blue color cones in the retina. We perceive a yellow color when light stimulates the red and green cones but not the blue cones. Therefore, when selecting yellow, the rightmost (blue) rectangle is darkened.

Students can familiarize themselves with how various colors (in the top rectangle) appear through their colored goggles using this training program. The rectangles at the bottom can be used in two ways. First, with their goggles removed momentarily, the rectangles show how the top color appears through other students’ goggles. For example, yellow (at the top) would look bright red and green to students wearing red and green goggles, respectively, but to a student wearing blue goggles, it would look black (or very dark blue). Therefore, students can use the rectangles at the bottom to explore how the color at the top can be encoded by perceived brightness across three different cone cells (i.e., colored goggles). A second way to use the rectangles is to have students keep their goggles on and explore how the brightness of the three squares varies with color.

They should notice that a single color “channel” is not sufficient to distinguish colors. For example, the leftmost rectangle appears equally bright to a student wearing red goggles, whether it is yellow or red. This means that this student (or an analogous cone) cannot distinguish between these colors on its own. They need multiple color channels for this, especially for secondary colors (cyan, yellow, and magenta).

After students have been allowed to explore how different colors look through their goggles, they can be asked to identify the color in the large rectangle without looking at the label shown. The pull-down menu at the top of the screen (or the up/down arrows on the keyboard) changes the rectangle's color. After the students are proficient at identifying primary colors (red, green, blue), they examine secondary colors (cyan, yellow, and magenta). These are created simply by mixing two of the primary colors. Therefore, they will be seen by two out of the three students as bright, and by the third as dark.

The table below is a key that relates the pattern of what the three students see – bright (+) or dark (-) – to the actual color of the rectangle on the screen.

![](images/color-vision-lesson-plan-f1a76c67.png)

It may be helpful for students to have a blank copy to fill in as they work through this training program. A blank copy is provided below:

https://docs.google.com/document/d/13XWyNWr7AakKWV4G2NTxmmAAdFU6aDXkLBcIz2Qe-0c/edit?usp=drive_web

### Competitive Game

After student groups practice identifying colors in the training program, they are asked to run a competitive version of the color discrimination game to reinforce the concepts learned and foster collaborative interaction. While wearing their goggles, groups open the software. They then see nine boxes of different primary or secondary colors. Above those boxes is a word indicating the color of the corresponding box. All boxes of that color must be selected, and the group’s score is determined by the time needed to identify all appropriately colored boxes.

The game offers three difficulty levels: Easy, Medium, and Hard. Each level determines the time limit for correctly identifying colors on each screen. As the difficulty increases, the time allowed decreases, challenging players to make faster decisions. Players earn points based on their speed and accuracy.

The game has ten rounds. Each round starts at 100 points, and the points tick down as an audible clock counts off — so the faster the group selects all the correct boxes, the more of the 100 points it keeps for that round. Selecting an incorrectly colored box costs 10 points and speeds up the clock, so mistakes are penalized twice over. The total across the ten rounds is then multiplied by a difficulty factor (Easy ×1.0, Medium ×1.5, Hard ×2.0) to give the final score.

The link to the game is provided below:

[NiceGUI](https://colorvisionapp.up.railway.app/)

Have student groups share their score after finishing the game. At the end of the game, they enter a team name and submit their score. You can encourage students to play the game a few times and try to improve their scores. Submitted scores are collected on a leaderboard that the teacher can view on a password-protected instructor dashboard, reached from the link at the bottom of the app's start page; the dashboard lists each team's score for a chosen date. If you would like to use the dashboard in your classroom, email [vanderdt@ucmail.uc.edu](mailto:vanderdt@ucmail.uc.edu) for access.

The image below shows the game's final screen, where students enter a team name and submit their score.

![](images/color-vision-lesson-plan-67265ec6.png)

## Activity: robot color discrimination

### Introduction

Explain to students that their task is to program a robot to follow a bicolored path constructed of paper, using a color sensor to keep the robot in the middle of the path. The task is illustrated in the figure below.

Students will create a path of two different colors of paper (red and green in the example below). Next, they will program the robot to stay in the middle of the path. This can be done by programming the robot to turn left or right, depending on which color the color sensor detects. In the example below, the robot should turn right if the sensor detects green and left if the sensor detects the red paper.

![](images/color-vision-lesson-plan-998025db.png)

### Operation of the color sensor

Students can find detailed [information on the operation of the color sensor](https://www.mouser.co.uk/datasheet/2/348/bh1745nuc-e-519994.pdf) online. However, in brief, the Me color sensor consists of three different light detectors registering the amount of red, green, and blue light. As we know, this information can be used to discriminate colors and recognize which color the paper under the robot is.

Give students time to install the color sensor instead of the Line follower sensor depicted in the generic instructions. Students should not over-tighten the screws when installing the color sensor because the caster wheel rests on some of the electronic components on the sensor board. This may cause the wheel not to move or the electronic component to get damaged. See below for images of the color sensor installed on the robot.

![](images/color-vision-lesson-plan-a15b7f94.jpg)

![](images/color-vision-lesson-plan-bf6d4571.jpg)

Students also construct a bicolored path using colored paper and tape so that each side of the path is a different color. This is illustrated in the drawing above. [An example is also shown in the video at the end of this guide](#color-vision).

### Procedure

The color sensor can only be used in the so-called `Upload` mode. This means programs must be uploaded to the robot using a USB cable. We can then disconnect the cable, and the robot is entirely autonomous. From then on, every time we switch on the robot, it will run the uploaded program without communication with your computer. More information about the different modes the robot can operate in is [available here](#getting-started-with-the-robot).

The fact that the sensor can only be used in `Upload` mode makes programming the robot harder. The main issue is that one cannot observe sensor values while our program runs and the robot is not connected using a USB cable. This makes it challenging to pick the correct sensor values to respond to.

To solve this issue, we will proceed in three steps. First, students will run a program that displays the sensor's current values while the robot is connected to the computer via a USB cable. This allows them to pick values for the program. Second, they can use these values to construct a program that follows the track. Next, they can program the robot using the derived rule. At this point, the robot is no longer connected to the computer using a USB cable.

> **Tip**
>
> If you use the programs below, the mBlock software will load an extension that allows you to work with the color sensor. To start programming from scratch, you must add the extension yourself. Click the following link for instructions:
>
> [Adding color sensor extension](#adding-color-sensor-extension)

#### Step 1: Inspecting the color sensor values

> **Note**
>
> Ensure the color sensor is connected to port 2 on the robot.

1. Open the program in mBlock on your computer or online.

    [Open the mBlock project](https://planet.mblock.cc/project/3954097) — or [download `color_vision_communication.mblock` directly](https://drive.google.com/file/d/1HsO5T4I7fSO7VC-iYbI_eH1SbMnlvQkI/view?usp=sharing) if your school blocks the Makeblock site.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
>     You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to your computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#step-1-open-the-example-program) for an example and more instructions.

2. In mBlock, select mBot under the Devices tab on the left side of the screen. This will show the robot's code. Do not unplug the cable during this part of the activity.

    ![Make sure you select the mBot under the Devices tab to see the code for the robot.](images/color-vision-lesson-plan-a5e7ceb3.png)

    Make sure you select the mBot under the Devices tab to see the code for the robot.

3. Connect to the robot using the USB cable. see [Getting started with the robot](#getting-started-with-the-robot) for instructions on connecting over the USB cable.
4. Upload the code to the robot by selecting the `Upload` mode and clicking `Upload code`.

![](images/color-vision-lesson-plan-4d4b0a0b.png)

![](images/color-vision-lesson-plan-41a422cc.png)

Once the code has been uploaded to the robot, you should see the robot’s white light coming on every second. This indicates that the robot is collecting data using the color sensor. Keep the USB cable plugged in. Also, mBlock should show a graph view that visualizes the amount of red, green, and blue light the color sensor picks up. The values are also shown in the panda window. Below, we show an image of the bar graph and the values as shown in the panda window.

![](images/color-vision-lesson-plan-8d5aeda8.png)

![](images/color-vision-lesson-plan-d29948b8.png)

With the robot connected to the computer through the USB cable, we can now collect data to check how the color sensor sees the two different colors of paper. Ask students to draw a few lines spanning the border between the two colors of paper spaced by about 1 cm. For example, in the figure below, we have drawn 7 marks spaced by 1 cm.

![](images/color-vision-lesson-plan-9e9eb54f.png)

Students can now observe how the values for the red, green, and blue light change as the robot is placed and aligned with each mark. For example, in the image below, the robot is aligned with the left most marker.

![](images/color-vision-lesson-plan-c1d3a88e.jpg)

The aim is to observe how the sensor readings change as the robot moves from one color of paper to the other color (here, green to red). Below, we include some measurements collected using the setup depicted in the images above. We have also included a column that shows the difference between the red and green values.

Here is a link to a [Google Sheets document](https://docs.google.com/spreadsheets/d/1frBjPa5mE7UsAW0t1LLKr9oEFSrDW9Je9eHolUvAf_I/edit?usp=sharing) to simplify recording and graphing the data.

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

![](images/color-vision-lesson-plan-44ef58b4.png)

Now that students have some baseline data, they must develop their algorithm and program the robot to follow the midline. Give students time to write a rule that would direct the robot when to turn right or left based on their data. Check student work before moving on. Students should have something similar to the example explanation below.

#### Step 2: Interpreting the data

In the above example, the set-up consisted of green paper on the left and red on the right. Here, we will derive a rule that keeps the robot on the centerline between the papers using the difference between the Red and Green channels.

> **Note**
>
> In principle, the current challenge can also be solved by only looking at the amount of red light. Indeed, as can be seen from the graph, if the robot picks up a lot of red light, it is on the red paper. If the intensity of the red light is lower, it is on the green paper. However, when students use paper in colors other than the primary colors (red, green, and blue), a single color channel might not be sufficient to discriminate the colors, and different channels must be compared. Moreover, true color vision relies on comparing different color channels (refer to the discussion of color vision in animals and the rationale of the color vision games) Therefore, the example here also uses a comparison between color channels.

Below, we have plotted the difference between Red and Green as a function of the robot's position. From this graph, we can derive a rule to keep the robot on the center line.

![](images/color-vision-lesson-plan-2a426533.png)

This is a potential rule:

```jsx
If Red - Green < -10: turn right
If Red - Green > 40: turn left
```

This rule turns the robot right if it detects more green light than red and vice versa. Once students have devised a rule like this, they can implement it in the robot.

#### Step 3: Programming the robot

Below, we link a program that implements the rule we have derived above. Students’ programs could look similar but should be changed to reflect the rules they derived.

If students start writing their program from scratch instead of starting from the example program. They should load the extension that loads the blocks that allow reading the color sensor.

![Click this button to open the extension menu.](images/color-vision-lesson-plan-721cd583.png)

![Add the color sensor extension to enable the blocks required to read the color sensor.](images/color-vision-lesson-plan-d48c279e.png)

![Adding a new category of blocks.](images/color-vision-lesson-plan-c06b5690.png)

[Open the mBlock project](https://planet.mblock.cc/project/3954308) — or [download `color_vision_motion.mblock` directly](https://drive.google.com/file/d/1kIi6T0hHREPmvZpEvC-I0OGfBcrrUTfW/view?usp=sharing) if your school blocks the Makeblock site.

The program is shown below. The first blocks read the red, green, and blue values detected by the color sensor. The purple block sets the onboard lights to a color that mimics the color seen by the color sensor, which should help debug the program. Next, the robot is set to move forward at a slow speed. Immediately after this, we check the value of red-green. Depending on this result, the robot is turned left or right. See below for a video demonstrating the behavior of the robot.

> **Note**
>
> It helps to keep the robot's speed low. This gives it more time to measure and respond to the color. For example, in the example, we set the power to 25%. This might make it difficult for the robot to get started. To help it start moving, you could give it a small push.

To run the example program (or the students’ program), upload the program to the robot. Once the program is uploaded, the USB cable can be disconnected. To change the program, connect the USB cable to the robot and upload the new program.

![](images/color-vision-lesson-plan-8649dc81.png)

[output.mp4](files/output.mp4)

### Extensions

Several extensions to the lesson plan can be made:

1. The track's end and start can be constructed of a third color. When the robot detects this color, it can be programmed to turn 180 degrees to return to the other end of the path.
2. The white LEDs on the me color sensor can be switched off. Remember, the LEDs deliver a uniform fixed and broad-spectrum light onto the floor, making the sensor’s ability to color discriminate easier. But, consider a real-life scenario where a robot tries to detect whether the floor underneath it is red or yellow, but the light in the environment is variable or suboptimal. If the lighting is poor, the overhead lamps might not emit sufficient yellow light, so the light reflecting from the floor will contain little yellow light. The sensor will have difficulty discriminating yellow from red. The following block can be used to switch off the white LEDs.

    ![](images/color-vision-lesson-plan-5972c66e.png)

3. Altering the colors in the path to include secondary colors such as cyan, yellow, and/or magenta.

## Adding color sensor extension

### Step 1: Add the mBot to mBlock

- Check whether the mBot is showing in the `Devices` window in mBlock. If the mBot is not listed, follow the instructions below to add the mBot.
- Click the `Add` (circular) button at the left side of the window. The button's image is shown below.

![](images/chrome-os-a1ae66d1.png)

- From the window that pops up, select the mBot (**not the mBot2**).

![](images/chrome-os-d52dfcc3.png)

![The mBot is selected in the `Devices` window.](images/chrome-os-86445f6e.png)

- The mBot will be added to the `Devices` section of the mBlock.

### Step 2: Add the color sensor extension

- Make sure the mBot is selected in the `Devices` window in mBlock.
- Click the `+` button in the blocks menu (see image below)
- This will bring up a screen with extensions for the robot.
- Select and `Add` the  `color sensor` extension.
- This extension will give you access to new blocks for using the color sensor.

> **Tip**
>
> Note that the color sensor can only be used in the `Upload` mode. Not in `Live mode`. Follow this link for more information about these modes: [Getting started with the robot](#getting-started-with-the-robot).

![](images/adding-color-sensor-extension-4c6bddee.png)

![](images/adding-color-sensor-extension-2578cd3c.png)

![](images/adding-color-sensor-extension-7d2f1d27.png)
