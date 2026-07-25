# Sound Localization


## Required materials

| Item | Description |
| :--- | :--- |
| mBot Robot | The mBot robot |
| Bluetooth Dongle | This is a dongle that allows to connect to the robot from a computer. This is currently the recommended way to work with the robot. |
| Makeblock Sound Sensor | Sensor reading the current sound intensity. Used in the sound localization plan and the intro to programming. |
| Screws | The robot use M4 machine screws. Students should be supplied with an ample supply of extra screws allowing to mount extra sensors. These screws are also used to mount the Robot Pipe Plate onto the PVC pipe. |
| Extra cables (short) | Extra cables for connecting sensors. This allows students to add sensors without removing cables and covers for losing cables.  The cables come in a pack of 4. I suggest supplying 1 extra cable per robot.  This cable is 20 cm long and has the same length as the 2 cables that come with the robot. |
| Lego compatible blocks | These blocks are compatible with the screws and the hole spacing used by the robot. Therefore these blocks allow students freedom in mounting sensors (as an alternative to the brackets we provide) |
| Materials to make robot ears | Students can make ears out of magic clay or craft paper. |
| Gaffers tape | It’s tape. What else can I say. I comes in handy everywhere. |
| Batteries | The robot takes 4 AA batteries. These should last a while. This is a 100 pack of AA batteries Providing more than 8 batteries per robot should allow swapping out the batteries and getting new stock without interruption to the curriculum. |
| Speaker | Speaker for playing the sound during the sound localization activities |
| Measuring Tape | Measuring tape to create the setup during one of the sound localization lesson plans |

> **Note**
>
> The newer versions of the sensor have a potentiometer that allows adjusting its sensitivity. For example, the sensor shown below has a small, round dial beside the microphone.  A screwdriver can be used to very gently rotate the dial to adjust the sensor's sensitivity.  If your sensor has such a dial, turn the dial on both sensors to the same halfway position.

![An image of the sound sensor. This sensor has a dial to change its sensitivity (pointed out by the arrow).](images/sound-localization-lesson-plan-98af73ad.png)

## Prerequisites

Students must be familiar with Microsoft Excel or Google Sheets, be able to enter data, and create and read simple graphs. They should also understand how humans hear sound and have some understanding of algorithmic thinking and the design process.

## Investigating/Essential Questions

- How	do humans localize sound?
- How	does a microphone differ from a human ear?
- How	can we use information from living animals to improve human technology (biomimicry)?
- What is phonotaxis?

## Educational Standards

Please follow the link below to see the educational standards pertaining to this lesson plan:

[Educational Standards](#educational-standards)

## Learning objectives

Students should be able to…

1. Identify three ways that a microphone is different from a human ear.
2. Measure and display the directivity of the microphones on a robot.
3. Design pinnae for a human and a robot.
4. Explore the design and placement of the robot's ears to increase	sensitivity to sound.

## Introduction

In this lesson, students will explore how humans localize sound and how robots can be made to localize sound through phonotaxis.  Sound localization has various applications. For example, in engineering, localizing the noise source in a machine can enhance its design. Engineers typically use arrays of many microphones to pinpoint sound more precisely than when using two microphones or ears. Other applications of sound localization include localizing a speaker. For example, some conference cameras will focus on the person speaking. This not only provides visual information about who is speaking but also improves the quality of the recorded sound. Sound localization is also increasingly used in robots to approach sound sources. Robots that interact with people are often able to localize sound, in particular, speech. As for the conference cameras, this ability allows the robot to fixate on (and identify) the speaker. It also points the microphones in the optimal direction to improve sound quality.

This lesson is divided into two sections. In the first section, students will learn about humans' ability to localize sound, design and test pinnae for human ears, and investigate how a microphone differs from a human ear. Then, in section two, students will use what they have learned to design and test pinnae (ears) for their robots so that the robot can move towards a sound.

This unit was created collaboratively with faculty from the University of Cincinnati College of Arts and Sciences, College of Engineering, and School of Education. Combining biology with engineering activities gives students a unique opportunity to understand the parallels between animal and robot behavior and sensory/sensor function. It addresses the Next Generation Science Standards (NGSS Lead States, 2013) and the International Society for Technology in Education Standards (International Society for Technology in Education, 2022).

## Introduction to Sound Localization

Humans (and many other animals) use several cues to localize sound.  These methods include interaural timing differences (the difference in time that it takes for sound to reach each ear),  interaural level differences (the difference in the loudness of the sound at each ear), and monaural spectral cues (how the shape of the pinna, or outer ear, influences the frequency of the sound).  While interaural timing and level differences help us to locate sounds on the horizontal plane, monaural spectral cues help us to locate sounds on the vertical plane.

### Sound localization cues

[](https://pubs.aip.org/physicstoday/article/52/11/24/410870/How-We-Localize-SoundRelying-on-a-variety-of-cues)

### Motivation

Engage students by asking for a volunteer to sit blindfolded in the middle of the room.  Tell the volunteer that you will make a sound, and they should point to the source as soon as they hear it.  Use a clicker, snap your fingers, or jingle keys for the sound.  Walk quietly around the volunteer, making the noise at ear level to the right or left of the person. The person should be able to identify the sound's location fairly well.  Then, quietly walk behind the volunteer and make the sound directly above their head.  They will likely have a hard time locating the sound.  Humans tend to do much better at localizing sound on the horizontal plane through interaural timing and level differences than on the vertical plane through monaural spectral cues.

## Activity: pinnae design

In this activity, students will create and test their own artificial pinnae (ears) to see whether these can increase the cues available for sound localization. 

[Testing artificial pinnae](#testing-artificial-pinnae)

## Microphones versus the human ear

Before moving on to the robotics section of this lesson, students need to understand how a microphone differs from the human ear.  The robot will use sensors that do not allow precise timing of sound arrival at the microphones. Therefore, only a sound source's loudness (or intensity) can be used to approach it.

### Sensitivity

The lines in the graph below represent the hearing threshold of humans and animals at different sound frequencies. These kinds of graphs are called audiograms. The graph shows the hearing threshold for different animals as a function of frequency. The curve indicates the faintest sound an animal can detect at that frequency. The lower the line, the fainter the sound that can be detected at a given frequency.

![](images/sound-localization-lesson-plan-fd572681.png)

These are average curves. The hearing threshold for individuals (and animals) can vary quite a bit. This graph shows that humans tend to be most sensitive (at the lowest point on the curve) around 3 kHz. Like a mouse, a small animal typically has a higher best frequency. If you want to find similar curves for other animals, Google 'audiogram x,' with x the animal you are interested in. Researchers have measured the audiograms of many different species.

The red line represents the approximate hearing threshold for the microphone, estimated from manufacturer-provided numbers. Two conclusions can be drawn about the differences between our ears and the microphone. First, the microphone's "hearing threshold" is much higher than our ears. This is not surprising. Animal ears are unbelievably sensitive. This implies that many sounds we can detect the microphone cannot. The microphone's hearing threshold is about 36 dB SPL. Students can use the table below to determine which sound intensities correspond with this intensity.  It is estimated that the microphone cannot detect sounds below 36 dB.

![](images/sound-localization-lesson-plan-58c2fb72.png)

### Frequency response

The audiograms and the microphone's sensitivity shown above reveal a second difference between our ears and the microphone: the microphone is almost equally sensitive to frequencies from 20 Hz to 20,000 Hz (and probably even higher frequencies, hence the trailing dots on the right side of the red line). To humans, sounds with the same physical amplitude at 2000 Hz and 10,000 Hz have very different loudness levels.  The 2000 Hz (i.e, 2 kHz) tone will sound louder than the 10,000 Hz (i.e., 10 kHz) tone. Introduce this idea to students using the online tone generator.

The curve that shows a microphone’s sensitivity to different frequencies is called its “frequency response”. Because the red line in the graph above is flat, engineers would say that the microphone has a “flat frequency response.” The drawing in the graph above is not a real frequency response. Below, we have included an actual frequency response of a simple microphone.

![](images/sound-localization-lesson-plan-abed05bc.png)

To demonstrate that our ears are differently sensitive to sounds with different frequencies, you can play tones with different frequencies at the same physical volume.  You can use an online tone generator like the one linked below.

[Online Tone Generator - generate pure tones of any frequency](https://www.szynalski.com/tone-generator/)

Even if you do not change the volume at which the sound is played, people will perceive sounds around 3000 Hz louder than lower- and higher-frequency sounds. For example, start by playing a 2000 Hz sound. Next, stop the sound and move the slider to 10,000 Hz before playing the new tone. Students will notice the difference in frequency, of course. However, they should also note that the 10,000 Hz tone sounds less loud.

### Directionality

The microphone is almost omnidirectional, meaning it is nearly equally sensitive to sounds coming from different directions. Our ears are not equally sensitive to all directions. Our heads and external ears block sound from specific directions and (somewhat) increase (amplify) sounds from other directions. Seeing this is a bit tricky, as the effect depends on the sound's frequency. Use the figure below to convey this idea.

![](images/sound-localization-lesson-plan-d5560ae5.png)

This figure shows the sensitivity of the left ear (for a given frequency) as a function of direction. The sphere is cut in half so that you can see inside. Red colors mean the ear is more sensitive to those directions. From this image, students can see that the ear is less sensitive to sound coming from behind. It is also less sensitive to sounds coming from straight ahead. The left ear is most sensitive to sound coming from the left. This is why humans turn one ear towards a sound source when trying to hear very faint sounds. Human ears are less sensitive to sounds coming from straight ahead. Luckily, that is where our eyes are focusing.

### Temporal response of the Makeblock sound sensor

> **Note**
>
> The take-home message of this section is that the robot does not detect sounds that are longer than about 1 second. The robot detects only the onset (and offset) of sound. This explains why a pulsed sound is provided below for robotic activities. If you were to use a constant sound, the robot would be functionally insensitive to it.

For the technically inclined, there is a fourth way our ears differ from the microphones used by the robot. The electronic components processing the microphone input make the robot sensitive to short bursts of sound. In contrast, the robot cannot detect long sounds, no matter how loud they are. 

When observing the Makeblock sound sensor, it should be evident that the microphone is the round black disk on the sensor board. However, you will notice that the board contains many other (tiny) electronic components. These primarily increase (amplify) the microphone's signal before sending it to the robot. However, these electronic components also do something else: they filter the signal from the microphone so it is high for short, loud bursts of sound. Almost no signal is transmitted to the robot during long bursts of sound.

The image below plots the signal sent to the robot over about 10 seconds. At the position of the first red arrow, a sound started playing.  Notice that, in response, the signal jumps up. This tells the robot the microphone is picking up sound. However, the signal decreases over time. After about a second, the signal returns to baseline, even though the sound is still playing. At the instance of the second arrow, the sound was switched off. The signal responds by becoming negative for a second or so.

![](images/sound-localization-lesson-plan-d9268e13.png)

### Conclusions

Now ask students to list the three (or four) main differences between microphones and human ears.  These three differences affect how we use the microphones to steer the robot to sound. After formatively assessing that students understand the differences, it is time to consider how these aspects would affect robotic sound localization.

### Background: hearing sensitivity

Our ears are very sensitive! Let's express the sensitivity of our ears in some numbers. This will give us intuition about how sensitive we are to sound. The faintest sounds humans can detect (around 2 kHz) have an amplitude of about 20 micropascal. This means the air pressure at the eardrum fluctuates by 20 micropascals around the average pressure. Therefore, the total pressure difference at this sound intensity is 40 micropascal (2 x 20 micropascal). This change in air pressure pushes and pulls the eardrum back and forth. The movement of the eardrum will eventually be perceived as sound.

We can calculate the force a 20 micropascal change in air pressure exerts on the eardrum. Using an online converter to avoid errors, we find that 40 micropascal equals 4.07 × 10⁻⁷ grams per square cm. The surface area of the eardrum is about 0.5 cm2. Therefore, we have to divide this number by 2.

This result shows that our ears can detect (the equivalent of) 0.0000002 grams applied to (and removed from) the eardrum at a frequency of 2000 Hz. These are tiny forces, indeed! Imagine a kitchen scale that could detect something much smaller than a grain of salt!

## Activity: robot phonotaxis

In this robotic activity, students will create a robot that performs phonotaxis. Phonotaxis is defined as the directional movement of an organism with respect to a sound source. The robot will compare the loudness of the sound measured by two sensors to determine whether it should turn left or right to get closer to the sound source. Find the instructions for the activity by following the link below:

[Robot phonotaxis](#robot-phonotaxis)

## Assessment Questions

Below, we list two questions you can use to assess students’ comprehension.

> Question 1: How does creating ‘ears’ on the robot increase the robot’s ability to respond to sound?  Support your reasoning using data from the graph.
> 

Answer: The variability of each ear has increased. For example, for the right ear, the measurements vary from about 400 to 150, a range of 250. In the previous graph, the right ear data range was less than 50. This increased variability is good: it means the microphone's output varies more with the angle to the sound source. This increased directionality should make sound localization easier (or more reliable).

> Question 2: Does angle placement of the ears on the robot increase or decrease the ability to locate sound?  Support your reasoning using data from the graph.
> 

Answer: At angle zero, we would expect the left and right ears to return about the same value. However, this is not the case. The left ear returns a larger value than the right one. This is due to the microphone sensitivity difference we observed earlier – a technical difference between the microphones at the time of manufacture. We will correct this difference.


## Testing artificial pinnae


### Introduction

Before the development of radar, approaching airplanes were often detected and localized acoustically. To increase the range and precision of airplane localization, people built a range of devices to enhance human hearing. Below are some pictures of such devices. The following article provides some further explanation.

[How warplanes were spotted before radar | CNN](https://www.cnn.com/style/article/war-sound-locators-before-radar/index.html)

![](images/testing-artificial-pinnae-affed672.png)

![](images/testing-artificial-pinnae-06410d6c.png)

![](images/testing-artificial-pinnae-6587bd75.jpg)

![](images/testing-artificial-pinnae-f4295f63.png)

All these devices attempted to increase the cues available for sound localization. In the current activity, students are asked to build their own devices to enhance sound localization. The activity is described on the following page.

### Activity

Tell students they will pair up for their sound localization test.  They will also be tasked with building pinnae to enhance their ability to locate sound, and then testing the effectiveness of their design.  For inspiration, show students some pictures of acoustic locators built in the early 20th century. You can also show them pictures of various animal ears. We previously provided students with cardboard paper, pipe cleaners, tape, etc., to build artificial pinnae. Example of some ears built by our students can be seen in the images below.

![](images/testing-artificial-pinnae-fe673636.jpg)

![](images/testing-artificial-pinnae-540a5939.jpg)

![](images/testing-artificial-pinnae-f88f6efd.jpg)

![Picture of students engaged in the experiment, testing their self-made external pinnae. The large sheet of paper on the floor is not part of the current activity.](images/testing-artificial-pinnae-e2beccd3.jpg)

The Google Doc embedded below can be printed and handed out to students as a handout describing how to conduct the experiment and record the data.

After all groups have finished, discuss the pinnae's performance. In their designs, students could have affected the timing (through distance), the loudness (through shape), or both. Ask the class questions to gather information about which were most effective and what they might change with more time.

For this activity, students should download a sound snippet. The link is provided in the linked Google Doc below. However, they can also download it directly here (click the file, then click the 3 dots to download).

[burst_short.wav](files/burst_short.wav)

> **Tip**
>
> You can decrease the number of trials if time is short.

[https://docs.google.com/document/d/1V8dXweQiOUJKbkWrg74FiriQjNVoPsODYCXSUl_M6s8/edit?usp=drive_web](https://docs.google.com/document/d/1V8dXweQiOUJKbkWrg74FiriQjNVoPsODYCXSUl_M6s8/edit?usp=drive_web)


## Robot phonotaxis


This activity aims to create a robot that follows a sound source. Use the sound file provided on a phone or portable speaker. When the sound source is held close (~50 cm) to the robot, the robot should turn towards the sound and approach it. The robot will do this by comparing the sound intensity between the left and right microphones. If the sound strength at the left receiver is greater than at the right, we will turn left, and vice versa. This is a form of phonotaxis.

In principle, the robot should be able to approach a sound source placed somewhere in the environment. However, as discussed earlier, the microphones are not very sensitive, so the robot might not be able to approach distant sound sources. 

> **Note**
>
> This robotic activity works best if the sound source the robot is supposed to approach is the only sound source. This implies that it is difficult to do this activity with different groups in the same room.

> **Note**
>
> Because the robot's sensors are not very sensitive, the volume of the speaker or phone should be turned up quite high. However, care should be taken not to turn the sound up so much that it is uncomfortable or that you need to raise your voice to be understood by someone three feet away. Too loud noise can damage hearing. If in doubt, students could wear hearing protection.

> **Note**
>
> In the programs provided for this activity, we assume the left microphone is plugged into port 3 and the right microphone into port 4.

### Step 1: Measuring the directionality of the microphones

> **Note**
>
> If time is limited, step 1, in which the robot's directionality is measured without external ears, can be skipped. However, we still recommend discussing the lack of directionality of the bare microphones so that students understand why they have to add external ears to the robot.

If we wish to find the sound by comparing the intensities at both receivers, the left microphone must be more sensitive than the right one for sound coming from the left. However, this is not necessarily so. Remember, we discussed the properties of the microphones and compared them with our ears? We said the microphones are almost omnidirectional (but not entirely). Therefore, they pick up sound almost equally well from all directions. In fact, they might be so omnidirectional that a sound at the left of the robot stimulates the left and the right microphones equally. In this case, the robot could not tell whether to turn left or right.

In the first step of this activity, students will measure the microphones' directionality. For this activity, we will provide the robot with two microphone sensors. Sensors can be mounted, as seen in the images below. 

> **Note**
>
> If you mount the sound sensors, as shown below, do not tighten the screws too much. This might damage the sensors.

![](images/robot-phonotaxis-5f001102.jpg)

![](images/robot-phonotaxis-9b19fbad.jpg)

![The sound sensor](images/robot-phonotaxis-e133beed.jpg)

Next, have students build a setup like the one shown below. You can have students put a large sheet of paper or a whiteboard on the floor (as in the example below) and draw several compass directions. Below, angles from -40 to 40 degrees have been drawn in 20-degree steps. Place the sound source at an angle of 0 ° and about 50 cm from the robot. The sound source can be a phone or a speaker. The speaker is not shown in the image below.

![](images/robot-phonotaxis-748fdb0b.jpg)

Have the sound source play the following sound on repeat. The sound consists of bursts of white noise. [The reason why this sound is pulsed is explained here](#sound-localization).  Click the link below, then click the 3 dots in the sound player to download the file.

[pip_exported.mp3](files/pip_exported.mp3)

Students should align the robot with each marked direction. Run the program below. In the program, ensure the block "set left_scale" contains the value 1. You can change this number by clicking on the small oval with the number.

![](images/robot-phonotaxis-35eb8c6f.png)

When they click the green flag, the robot will take 20 measurements of sound intensity from the left and right microphones. Finally, it will calculate the average of the 20 measurements. The robot will beep when it is done. Once the robot beeps, they should write down the number for `left_sound` and `right_sound`.

Next, turn the robot to align it with the next direction and click the green button again to measure the next angle. In this way, the students will determine the loudness of the sound as picked up by the robot's two microphones (or ears) at different positions of the sound source relative to the robot.

> **Tip**
>
> If you use the program below, the mBlock software will load an extension that lets you work with the sound sensor. To start programming from scratch, you must add the extension yourself. Click the following link for instructions:
>
> [Adding the sound sensor extension](#adding-the-sound-sensor-extension)

[sound_localization_directionality](https://planet.mblock.cc/project/3941521) — or [download `sound_localization_directionality.mblock` directly](https://drive.google.com/file/d/1hKiYFX9wSxCGxuLkfC3UYyaonUeW_tbo/view?usp=sharing) if your school blocks the Makeblock site.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
> You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to your computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#running-your-first-program) for an example and more instructions.

After collecting all measurements, students can create a graph of their data. Below, we have included a typical plot resulting from the measurements.

![](images/robot-phonotaxis-d4731c59.png)

From the graph, we can derive two conclusions. First, the intensity of the picked-up sound varies little with the angle. This means that the microphones register about the same sound intensity regardless of the angle relative to the sound source. This is due to the microphones' omnidirectionality. Stated differently, from the sound intensity picked up by the left and right microphones, you cannot tell whether the sound is coming from the left or the right. That is not a good basis for sound localization. Secondly, across (most) directions, the left microphone (in the provided example) registered larger values than the right one. This suggests that the microphones are not equally sensitive. The two microphones on the robot feature the same electronic components. Therefore, one would expect them to be similarly sensitive to sound. However, for various reasons, one is often more sensitive than the other. This makes localizing sound by comparing the intensity at both microphones harder.

In summary, based on the measurements, we conclude that the microphones are not suited for sound localization due to their omnidirectional nature. However, this will be fixed in the next step.

### Step 2: Make the ears directional

Students can make the ears (microphones) directional by constructing artificial pinnae around the microphones. Students can use paper, modeling clay, or other materials. In the example below, we made external ears for the robot by rolling sheets of paper into cones. Notice that the ears are quite large with respect to the robot. Larger ears typically result in higher directionality. We also show images of a student’s robot, which is provided with external ears made out of model magic clay.

![](images/robot-phonotaxis-3b931d59.jpg)

![](images/robot-phonotaxis-3c135ee9.jpg)

![](images/robot-phonotaxis-5b1579be.jpg)

![](images/robot-phonotaxis-caff0520.jpg)

Once students have created ‘ears’ for their robots, have them repeat the measurements above. The graph should now show a clear directionality. If not, they should keep working on the ears until they obtain directional ears. If the ears are not directional, they can not be used to localize sound.

Below, we show an example of data collected with directional ears. These data show that the right ear picks up more sound when the sound source is to the right of the robot (negative x-axis angles), and vice versa.

![](images/robot-phonotaxis-f4124490.png)

One problem with the graph above, which often occurs with students’ external ears, is that the amount of sound picked up by the left and right ears is not the same at zero degrees. Indeed, in the data shown, when the sound source is directly in front of the robot, the left ear picks up more sound than the right. The amount of sound picked up by the left ear seems higher overall. This indicates that the left ear is more sensitive than the right. At angle zero, the right value is about 70% of the value for the left ear:

$$
\frac{right ear value at zero degrees}{left ear value at zero degrees} \approx \frac{250}{340} \approx 0.7
$$

Students’ values will differ. Perhaps their right ear is more sensitive than the left. In this case, the equation above will return a value larger than 1.

We can correct for the differences in microphone sensitivity. The example program provides for this through the `left_scale` block. You can enter the result of the equation into that block to correct for differences in microphone sensitivity. For the example above, we would enter 0.7

![](images/robot-phonotaxis-3f2fd20b.png)

Students could rerun the measurements to check whether this correction results in the left and right ears picking up about the same amount of sound at zero degrees. Below, we have included an example graph.

![](images/robot-phonotaxis-6f33c641.png)

Now, the left and right ear values are approximately equal at angle zero. Moreover, the left ear returns a higher value if the sound source is on the robot's left side (angle > 0). The right ear has a larger response when the sound source is on the robot's right side (angle < 0). These response curves allow us to perform phonotaxis now.

### Step 3: Phonotaxis

We will now have the robot follow a sound source. Students can run the example program. The robot should approach the sound source. They can try moving the sound source while the program is running to see whether the robot notices the change.

[sound_localization_approach](https://planet.mblock.cc/project/3941523) — or [download `sound_localization_approach.mblock` directly](https://drive.google.com/file/d/1-cUC4kOW5Fy2Qy7libpa73puB28lPIS_/view?usp=sharing) if your school blocks the Makeblock site.

When running this program, be sure to fill out the previously determined correction factor in the `left_scale` block:

![](images/robot-phonotaxis-f22ed6ba.png)

The example program does the following:

1. It takes 3 measurements of sound intensity at the left and right ears.
2. Depending on which ear receives the loudest sound, the robot turns slightly left or right.
3. Next, the robot drives a few cm forward. And the cycle repeats.

This approach to sound localization results in a jittery path: the robot stops, measures, rotates, and moves. However, this approach gives the robot enough time to collect data (sound). Moreover, many animals adopt the same stopping-moving strategy when approaching sound sources. Even humans "stop to listen" when looking for their ringing phone. Biology and engineering use similar strategies!


## Adding the sound sensor extension


### Step 1: Add the mBot to mBlock

- Check whether the mBot is showing in the `Devices` window in mBlock. If the mBot is not listed, follow the instructions below to add the mBot.
- Click the `Add` (circular) button at the left side of the window. The button's image is shown below.

![](images/chrome-os-a1ae66d1.png)

- From the window that pops up, select the mBot (**not the mBot2**).

![](images/chrome-os-d52dfcc3.png)

![The mBot is selected in the `Devices` window.](images/chrome-os-86445f6e.png)

- The mBot will be added to the `Devices` section of the mBlock.

### Step 2: Add the sound sensor extension

- Make sure the mBot is selected in the `Devices` window in mBlock.
- Click the `+` button in the blocks menu (see image below)
- This will bring up a screen with extensions for the robot.
- Select and `Add` the `Light Sound` extension.
- This extension will give you access to new blocks for using the sound sensors.

![](images/adding-color-sensor-extension-4c6bddee.png)

![](images/adding-the-sound-sensor-extension-12902c49.png)

![](images/adding-the-sound-sensor-extension-3972f84e.png)
