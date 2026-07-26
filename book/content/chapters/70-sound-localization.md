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
| Gaffers tape | It’s tape. What else can I say. It comes in handy everywhere. |
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

- How do humans localize sound?
- How does a microphone differ from a human ear?
- How can we use information from living animals to improve human technology (biomimicry)?
- What is phonotaxis?

## Educational Standards

The educational standards applicable to this lesson are listed in the [Educational standards](#educational-standards) chapter.

## Learning objectives

Students should be able to…

1. Identify three ways that a microphone is different from a human ear.
2. Measure and display the directivity of the microphones on a robot.
3. Design pinnae for a human and a robot.
4. Explore the design and placement of the robot's ears to increase sensitivity to sound.

## Introduction

In this lesson, students will explore how humans localize sound and how robots can be made to localize sound through phonotaxis.  Sound localization has various applications. For example, in engineering, localizing the noise source in a machine can enhance its design. Engineers typically use arrays of many microphones to pinpoint sound more precisely than when using two microphones or ears. Other applications of sound localization include localizing a speaker. For example, some conference cameras will focus on the person speaking. This not only provides visual information about who is speaking but also improves the quality of the recorded sound. Sound localization is also increasingly used in robots to approach sound sources. Robots that interact with people are often able to localize sound, in particular, speech. As for the conference cameras, this ability allows the robot to fixate on (and identify) the speaker. It also points the microphones in the optimal direction to improve sound quality.

This lesson is divided into two sections. In the first section, students will learn about humans' ability to localize sound, design and test pinnae for human ears, and investigate how a microphone differs from a human ear. Then, in section two, students will use what they have learned to design and test pinnae (ears) for their robots so that the robot can move toward a sound.

This unit was created collaboratively with faculty from the University of Cincinnati College of Arts and Sciences, College of Engineering, and School of Education. Combining biology with engineering activities gives students a unique opportunity to understand the parallels between animal and robot behavior and sensory/sensor function. It addresses the Next Generation Science Standards (NGSS Lead States, 2013) and the International Society for Technology in Education Standards (International Society for Technology in Education, 2022).

## Introduction to Sound Localization

Humans (and many other animals) use several cues to localize sound.  These methods include interaural timing differences (the difference in time that it takes for sound to reach each ear),  interaural level differences (the difference in the loudness of the sound at each ear), and monaural spectral cues (how the shape of the pinna, or outer ear, influences the frequency of the sound).  While interaural timing and level differences help us to locate sounds on the horizontal plane, monaural spectral cues help us to locate sounds on the vertical plane.

### Sound localization cues

Humans locate sound using several cues at once: the difference in arrival time between the two ears, the difference in level, and the way the outer ear colours sounds arriving from different directions. The article below is a readable survey.

[How We Localize Sound — *Physics Today*](https://pubs.aip.org/physicstoday/article/52/11/24/410870/How-We-Localize-SoundRelying-on-a-variety-of-cues)

### Motivation

Engage students by asking for a volunteer to sit blindfolded in the middle of the room.  Tell the volunteer that you will make a sound, and they should point to the source as soon as they hear it.  Use a clicker, snap your fingers, or jingle keys for the sound.  Walk quietly around the volunteer, making the noise at ear level to the right or left of the person. The person should be able to identify the sound's location fairly well.  Then, quietly walk behind the volunteer and make the sound directly above their head.  They will likely have a hard time locating the sound.  Humans tend to do much better at localizing sound on the horizontal plane through interaural timing and level differences than on the vertical plane through monaural spectral cues.

## Activity: pinnae design

In this activity, students will create and test their own artificial pinnae (ears) to see whether these can increase the cues available for sound localization.

[Testing artificial pinnae](#testing-artificial-pinnae)

## Microphones versus the human ear

Before moving on to the robotics section of this lesson, students need to understand how a microphone differs from the human ear.  The robot will use sensors that do not allow precise timing of sound arrival at the microphones. Therefore, only a sound source's loudness (or intensity) can be used to approach it.

### Sensitivity

The graph below is an **audiogram**. It is worth spending a moment on how to read one, because the shape is the opposite way up from what people expect.

Every point on a curve is a **threshold**: the faintest sound the animal can just detect at that frequency. So a curve that dips low means *good* hearing, not a quiet sound — it means the animal can hear sounds as faint as that. A curve that rises means hearing is *worse* there, because a sound has to be louder before it registers at all. The lowest point on a curve is the frequency the animal hears best. Nothing on this graph says anything about how loud a sound is; it is entirely about how quiet a sound can get before it becomes inaudible.

![Audiograms for four species, with the sound sensor's threshold in red. Each curve gives the faintest sound that animal can detect at each frequency, so **lower on the graph means more sensitive**. Humans hear best at around 3 kHz, where the threshold dips below 0 dB SPL. The red line is flat because the sensor is about equally sensitive at every frequency, and it lies above all four curves because it is far less sensitive than any of these ears.](images/sound-localization-lesson-plan-fd572681.png){#fig:audiogram}

These are average curves. The hearing threshold for individuals (and animals) can vary quite a bit. The graph shows that humans tend to be most sensitive around 3 kHz. Like a mouse, a small animal typically has a higher best frequency. If you want to find similar curves for other animals, search for 'audiogram x', with x the animal you are interested in. Researchers have measured the audiograms of many different species.

The red line is the approximate threshold of the robot's sound sensor, estimated from manufacturer-provided numbers, and it gives the first of our differences. It sits at about 36 dB SPL — above every animal curve on the graph. The sensor is much less sensitive than any of these ears, which is not surprising, because animal ears are extraordinarily sensitive. A great many sounds that we can hear easily are simply not there as far as the robot is concerned. The [table of everyday sound levels](#fig:levels) gives a feel for what 36 dB SPL means.

![Everyday sounds and their approximate levels. The sensor's threshold of about 36 dB SPL falls between a quiet whisper and a quiet auditorium, so anything fainter than a quiet room will not register at all.](images/sound-localization-lesson-plan-58c2fb72.png){#fig:levels}

### Frequency response

The [audiogram](#fig:audiogram) reveals a second difference. The sensor is almost equally sensitive from 20 Hz to 20,000 Hz and probably beyond, which is why its line is flat and why it trails off in dots at the right-hand edge. Our ears are not like that at all. Two sounds with the same physical amplitude, one at 2 kHz and one at 10 kHz, do not sound equally loud to us: the 2 kHz tone sounds louder.

The curve describing how sensitive a microphone is at each frequency is called its **frequency response**, and because the red line is flat, an engineer would say this microphone has a *flat frequency response*. That red line is a schematic rather than a measurement. A [real one, measured from a simple microphone](#fig:freqresp), is flat within a decibel or two across most of the range, with small ripples at the top end.

![A measured frequency response for a simple microphone. Unlike the schematic red line in the audiogram, this one is real data, but the story is the same: within a decibel or two, the microphone treats every frequency alike.](images/sound-localization-lesson-plan-abed05bc.png){#fig:freqresp}

You can demonstrate the contrast with your own ears using an online tone generator, playing tones of different frequencies without touching the volume control.

[Online Tone Generator - generate pure tones of any frequency](https://www.szynalski.com/tone-generator/)

Even with the volume fixed, sounds around 3000 Hz are perceived as louder than lower- and higher-frequency ones. Play a 2000 Hz tone, then stop it, move the slider to 10,000 Hz, and play again. Students will hear the change in pitch, of course, but they should also notice the 10,000 Hz tone sounds quieter, even though nothing about the volume has changed.

This has a practical consequence that is easy to miss, and it matters for the robot activities later in this chapter. Because our sensitivity falls away at both ends of the range and the sensor's does not, **your own ears are a poor guide to what the robot can hear.** A 10 kHz tone that sounds faint to you is no harder for the sensor than a 2 kHz tone that sounds loud, and a low rumble you can barely hear may be perfectly detectable to it. So when you are setting up a sound for the robot, judge it by what the robot reports rather than by how loud it seems in the room — and resist turning the volume up because a tone sounds quiet to you, since the sensor may be well above its threshold already.

### Directionality

The microphone is almost omnidirectional, meaning it is nearly equally sensitive to sounds coming from different directions. Our ears are not equally sensitive to all directions. Our heads and external ears block sound from specific directions and (somewhat) increase (amplify) sounds from other directions. Seeing this is a bit tricky, as the effect depends on the sound's frequency. Use the [directivity figure](#fig:hrtf) to convey this idea.

![How sensitivity varies with the direction a sound comes from, for one ear and one frequency. The sphere is cut away so the inside is visible, and warmer colors mark the directions the ear picks up best. Figure from [LmK Music Production, *What is HRTF?*](https://lmkprod.com/what-is-hrtf-brief-explanation/).](images/sound-localization-lesson-plan-d5560ae5.png){#fig:hrtf}

It shows the sensitivity of the left ear, at one frequency, as a function of the direction a sound arrives from. The sphere is cut in half so that you can see inside, and warmer colors mark the directions the ear picks up best.

Each ear is most sensitive to sounds arriving from its own side — for the left ear, from roughly 90 degrees to the left. Sensitivity falls away from there in both directions: towards the back, where the head and the pinna shadow the ear, and towards the front, so that a sound directly ahead reaches the ear less efficiently than the same sound off to one side. This is why we turn one ear towards a sound we are straining to hear, and it is no great loss that straight ahead is a weak direction for the ears, because that is the direction the eyes already cover.

The pattern is easier to state than to read off this particular figure, so use it as an illustration of the idea rather than something to measure.

### Temporal response of the Makeblock sound sensor

> **Note**
>
> The take-home message of this section is that the robot does not detect sounds that are longer than about 1 second. The robot detects only the onset (and offset) of sound. This explains why a pulsed sound is provided below for robotic activities. If you were to use a constant sound, the robot would be functionally insensitive to it.

For the technically inclined, there is a fourth way our ears differ from the sound sensor the robot uses. The electronics on the sensor board make it responsive to short bursts of sound, while a long sound goes undetected no matter how loud it is.

> **Important**
>
> This is a quirk of the Makeblock sound sensor, not something microphones do in general. The microphone itself follows a continuous sound perfectly well. It is the amplifier circuit on the sensor board that removes the steady part of the signal and passes on only the changes. A different sound sensor would behave differently, and the microphone in a phone or a laptop certainly does. It is worth being explicit about this with students, because "microphones cannot hear continuous sounds" is both memorable and wrong.

When observing the Makeblock sound sensor, it should be evident that the microphone is the round black disk on the sensor board. However, you will notice that the board contains many other (tiny) electronic components. These primarily increase (amplify) the microphone's signal before sending it to the robot. However, these electronic components also do something else: they filter the signal from the microphone so it is high for short, loud bursts of sound. Almost no signal is transmitted to the robot during long bursts of sound.

The [oscilloscope trace](#fig:temporal) plots the signal reaching the robot over about ten seconds. At the first red arrow a sound starts playing, and the signal jumps up: the sensor has noticed. But it then falls away, and after about a second it is back at baseline even though the sound is still playing. At the second arrow the sound stops, and the signal dips below baseline for a second or so before recovering. What the sensor reports is not the sound but the *changes* in it.

![The sensor's output on an oscilloscope, over about ten seconds. The sound starts at the first arrow and stops at the second. Both edges produce a response that decays back to baseline within about a second; the steady sound in between produces nothing at all.](images/sound-localization-lesson-plan-d9268e13.png){#fig:temporal}

### Conclusions

Now ask students to list the three (or four) main differences between microphones and human ears.  These three differences affect how we use the microphones to steer the robot to sound. After formatively assessing that students understand the differences, it is time to consider how these aspects would affect robotic sound localization.

### Background: hearing sensitivity

Our ears are very sensitive, and it is worth putting a number on it. The faintest sound a person can hear at around 2 kHz corresponds to a sound pressure of about **20 micropascal** — the figure that defines 0 dB SPL, and the bottom row of the table of sound levels earlier in this chapter.

That 20 micropascal is an RMS value: a kind of average taken over the cycle, not the largest pressure reached. For a pure tone the peak is √2 times the RMS value, so at the eardrum the pressure rises about 28 micropascal above the surrounding air pressure and falls about 28 micropascal below it. The full swing, from the top of the cycle to the bottom, is about **57 micropascal**. It is this rising and falling pressure that pushes and pulls the eardrum, and that movement is eventually perceived as sound.

We can turn that pressure into a force. A pressure of 57 micropascal is 5.8 × 10⁻⁷ grams-force per square centimetre — the weight of just under six ten-millionths of a gram resting on each square centimetre. Force is pressure times area, and the eardrum is about 0.5 cm², so the force on it is about **2.9 × 10⁻⁷ grams-force**, or 0.0000003 grams.

So our ears detect the equivalent of three ten-millionths of a gram being laid on the eardrum and lifted off again, two thousand times a second. A grain of salt weighs something like 0.00006 grams — two hundred times more. Imagine a kitchen scale that could weigh a two-hundredth of a grain of salt, and read it two thousand times a second.

## Activity: robot phonotaxis

In this robotic activity, students will create a robot that performs phonotaxis. Phonotaxis is defined as the directional movement of an organism with respect to a sound source. The robot will compare the loudness of the sound measured by two sensors to determine whether it should turn left or right to get closer to the sound source. Find the instructions for the activity by following the link below:

[Robot phonotaxis](#robot-phonotaxis)

## Assessment Questions

Below, we list two questions you can use to assess students’ comprehension.

> Question 1: How does creating ‘ears’ on the robot increase the robot’s ability to respond to sound?  Support your reasoning using data from the graph.
>

Answer: The variability of each ear has increased. With ears fitted, the right ear ranges from about 380 at -40 degrees down to about 170 at +40, a spread of roughly 210. Without ears it stayed between about 310 and 380, a spread of roughly 70. This increased variability is good: it means the microphone's output varies more with the angle to the sound source. This increased directionality should make sound localization easier (or more reliable).

> Question 2: Does angle placement of the ears on the robot increase or decrease the ability to locate sound?  Support your reasoning using data from the graph.
>

Answer: At angle zero, we would expect the left and right ears to return about the same value. However, this is not the case. The left ear returns a larger value than the right one. This is due to the microphone sensitivity difference we observed earlier – a technical difference between the microphones at the time of manufacture. We will correct this difference.

## Testing artificial pinnae

### Introduction

Before the development of radar, approaching airplanes were often detected and localized acoustically. To increase the range and precision of airplane localization, people built a range of devices to enhance human hearing. Below are some pictures of such devices. The following article provides some further explanation.

[How warplanes were spotted before radar | CNN](https://www.cnn.com/style/article/war-sound-locators-before-radar/index.html)

![Two Dutch personal sound locators. Each funnels sound from a wide area into the operator's ears, and each turns on its base so the operator can sweep for the direction the sound is loudest.](images/testing-artificial-pinnae-affed672.png)

![Four more locators. Note how many use pairs or quads of horns rather than one: separating the collectors widens the difference between what each ear receives, which is exactly what students are trying to achieve with their own pinnae.](images/testing-artificial-pinnae-06410d6c.png)

![Left, a locator using honeycomb collectors rather than horns. Right, a row of them on wheeled carriages, ready to be moved into position.](images/testing-artificial-pinnae-6587bd75.jpg)

![Left, a head-mounted locator, which is the closest of these to the pinnae students will build. Right, a large locator worked by three operators at once.](images/testing-artificial-pinnae-f4295f63.png)

All these devices attempted to increase the cues available for sound localization. In the current activity, students are asked to build their own devices to enhance sound localization. The activity is described below.

### Activity

Tell students they will pair up for their sound localization test.  They will also be tasked with building pinnae to enhance their ability to locate sound, and then testing the effectiveness of their design.  For inspiration, show students some pictures of acoustic locators built in the early 20th century. You can also show them pictures of various animal ears. We previously provided students with cardboard paper, pipe cleaners, tape, etc., to build artificial pinnae. Example of some ears built by our students can be seen in the images below.

![Pinnae made from card cones on a headband. The shape gathers sound from in front of the ear and shields it from behind.](images/testing-artificial-pinnae-fe673636.jpg)

![A flatter design, taped to the side of the head. Reflecting surfaces need not be cone-shaped to change what reaches the ear.](images/testing-artificial-pinnae-540a5939.jpg)

![Large cones covering both ears. Designs this size change the loudness reaching each ear substantially, but they also make it hard to tell front from back.](images/testing-artificial-pinnae-f88f6efd.jpg)

![Picture of students engaged in the experiment, testing their self-made external pinnae. The large sheet of paper on the floor is not part of the current activity.](images/testing-artificial-pinnae-e2beccd3.jpg)

The procedure is run by an app, which walks a pair through the trials, tells them where to put the speaker, plays the sound, and scores the result at the end.

[soundlocalizationapp-production.up.railway.app](https://soundlocalizationapp-production.up.railway.app)

It is designed for a phone, so the quickest way to start a class is to put this code on the board. It runs just as well on a laptop.

![The code students can scan to open the sound localization app on their phones.](images/sound-localization-app-qr.png){#fig:sl-qr}

On the opening screen, a pair enters a name, chooses whether this run is with **Real ears** or **Artificial ears**, and sets how many trials to do — fewer if time is short. The `Instructions` bar folds out into a full description of the activity, including how to lay the setup out, so students can work from the app rather than from a handout.

![The opening screen. The `Instructions` bar at the top folds out into the full procedure, including how to arrange the room.](images/sound-localization-app-start.png){#fig:sl-start}

Each trial then tells the pair where to place the speaker, waits while they play the sound, and records what the listener answers.

![A trial in progress. The app names the speaker position, plays the sound on request, and moves on when the listener has answered.](images/sound-localization-app-trial.png){#fig:sl-trial}

The test is adaptive: a correct answer makes the next trial harder by moving the speaker nearer the midline, where the difference between the two ears is smallest. A pair whose pinnae work will keep succeeding at angles that defeat a pair without them, which is the comparison the activity is built on. At the end the app reports a score and a table of trials — run it once with real ears and once with the artificial ones, and compare.

After all groups have finished, discuss the pinnae's performance. In their designs, students could have affected the timing (through distance), the loudness (through shape), or both. Ask the class questions to gather information about which were most effective and what they might change with more time.

## Robot phonotaxis

This activity aims to create a robot that follows a sound source. Use the sound file provided on a phone or portable speaker. When the sound source is held close (~50 cm) to the robot, the robot should turn toward the sound and approach it. The robot will do this by comparing the sound intensity between the left and right microphones. If the sound strength at the left receiver is greater than at the right, we will turn left, and vice versa. This is a form of phonotaxis.

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

![The two sound sensors mounted on the front of the robot, angled outwards so that each faces a different side.](images/robot-phonotaxis-5f001102.jpg)

![One of the sensors close up. The microphone is the small black disc; the rest of the board amplifies and filters its signal.](images/robot-phonotaxis-9b19fbad.jpg)

![The sound sensor.](images/robot-phonotaxis-e133beed.jpg)

Next, have students build a setup like the one shown below. You can have students put a large sheet of paper or a whiteboard on the floor (as in the example below) and draw several compass directions. Below, angles from -40 to 40 degrees have been drawn in 20-degree steps. Place the sound source at an angle of 0 ° and about 50 cm from the robot. The sound source can be a phone or a speaker. The speaker is not shown in the image below.

![Measuring directionality. The robot sits at the centre of a protractor scale so it can be rotated to a known angle between readings.](images/robot-phonotaxis-748fdb0b.jpg)

Have the sound source play the following sound on repeat. The sound consists of bursts of white noise. [Temporal response of the Makeblock sound sensor](#temporal-response-of-the-makeblock-sound-sensor) explains why this sound is pulsed.  Click the link below, then click the 3 dots in the sound player to download the file.

[Pulsed tone for the robot (.mp3)](files/pip_exported.mp3)

Students should align the robot with each marked direction. Run the program below. In the program, ensure the block "set left_scale" contains the value 1. You can change this number by clicking on the small oval with the number.

![The `left_scale` block, which holds the correction factor. It starts at 1, meaning no correction.](images/robot-phonotaxis-35eb8c6f.png)

When they click the green flag, the robot will take 20 measurements of sound intensity from the left and right microphones. Finally, it will calculate the average of the 20 measurements. The robot will beep when it is done. Once the robot beeps, they should write down the number for `left_sound` and `right_sound`.

Next, turn the robot to align it with the next direction and click the green button again to measure the next angle. In this way, the students will determine the loudness of the sound as picked up by the robot's two microphones (or ears) at different positions of the sound source relative to the robot.

> **Tip**
>
> If you use the program below, the mBlock software will load an extension that lets you work with the sound sensor. To start programming from scratch, you must add the extension yourself. Click the following link for instructions:
>
> [Adding the sound sensor extension](#adding-the-sound-sensor-extension)

[Open the mBlock project](https://planet.mblock.cc/project/3941521). If your school blocks the Makeblock site, [download `sound_localization_directionality.mblock`](files/programs/sound_localization_directionality.mblock) instead.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
> You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to my computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#step-1-open-the-example-program) for an example and more instructions.

After collecting all measurements, students can create a graph of their data. Below, we have included a typical plot resulting from the measurements.

![Loudness at each ear as the robot is rotated, with no ears fitted. Both lines are nearly flat: the bare microphones barely distinguish direction at all.](images/robot-phonotaxis-d4731c59.png)

From the graph, we can derive two conclusions. First, the intensity of the picked-up sound varies little with the angle. This means that the microphones register about the same sound intensity regardless of the angle relative to the sound source. This is due to the microphones' omnidirectionality. Stated differently, from the sound intensity picked up by the left and right microphones, you cannot tell whether the sound is coming from the left or the right. That is not a good basis for sound localization. Secondly, across (most) directions, the left microphone (in the provided example) registered larger values than the right one. This suggests that the microphones are not equally sensitive. The two microphones on the robot feature the same electronic components. Therefore, one would expect them to be similarly sensitive to sound. However, for various reasons, one is often more sensitive than the other. This makes localizing sound by comparing the intensity at both microphones harder.

In summary, based on the measurements, we conclude that the microphones are not suited for sound localization due to their omnidirectional nature. However, this will be fixed in the next step.

### Step 2: Make the ears directional

Students can make the ears (microphones) directional by constructing artificial pinnae around the microphones. Students can use paper, modeling clay, or other materials. In the example below, we made external ears for the robot by rolling sheets of paper into cones. Notice that the ears are quite large with respect to the robot. Larger ears typically result in higher directionality. We also show images of a student’s robot, which is provided with external ears made out of model magic clay.

![Paper cone ears, taped to the sensors and angled outwards.](images/robot-phonotaxis-3b931d59.jpg)

![A moulded pair, shaped to gather sound from one side and shield the other.](images/robot-phonotaxis-3c135ee9.jpg)

![Another design. What matters is not realism but that the two ears face away from each other.](images/robot-phonotaxis-5b1579be.jpg)

![Students take the brief further than strictly necessary, which is no bad thing.](images/robot-phonotaxis-caff0520.jpg)

Once students have created ‘ears’ for their robots, have them repeat the measurements above. The graph should now show a clear directionality. If not, they should keep working on the ears until they obtain directional ears. If the ears are not directional, they can not be used to localize sound.

Below, we show an example of data collected with directional ears. These data show that the right ear picks up more sound when the sound source is to the right of the robot (negative x-axis angles), and vice versa.

![The same measurement with ears fitted. The lines now separate and cross: each ear hears its own side more loudly, which is the difference the robot steers on.](images/robot-phonotaxis-f4124490.png)

One problem with the graph above, which often occurs with students’ external ears, is that the amount of sound picked up by the left and right ears is not the same at zero degrees. Indeed, in the data shown, when the sound source is directly in front of the robot, the left ear picks up more sound than the right. The amount of sound picked up by the left ear seems higher overall. This indicates that the left ear is more sensitive than the right. At angle zero, the right value is about 70% of the value for the left ear:

$$
\frac{right ear value at zero degrees}{left ear value at zero degrees} \approx \frac{250}{340} \approx 0.7
$$

Students’ values will differ. Perhaps their right ear is more sensitive than the left. In this case, the equation above will return a value larger than 1.

We can correct for the differences in microphone sensitivity. The example program provides for this through the `left_scale` block. You can enter the result of the equation into that block to correct for differences in microphone sensitivity. For the example above, we would enter 0.7

![Setting the correction factor. Here the left microphone reads high, so `left_scale` is set below 1 to bring the two into agreement.](images/robot-phonotaxis-3f2fd20b.png){#fig:leftscale}

Students could rerun the measurements to check whether this correction results in the left and right ears picking up about the same amount of sound at zero degrees. Below, we have included an example graph.

![After scaling. The two curves now cross close to zero degrees, so equal loudness means the sound really is straight ahead.](images/robot-phonotaxis-6f33c641.png)

Now, the left and right ear values are approximately equal at angle zero. Moreover, the left ear returns a higher value if the sound source is on the robot's left side (angle > 0). The right ear has a larger response when the sound source is on the robot's right side (angle < 0). These response curves allow us to perform phonotaxis now.

### Step 3: Phonotaxis

We will now have the robot follow a sound source. Students can run the example program. The robot should approach the sound source. They can try moving the sound source while the program is running to see whether the robot notices the change.

[Open the mBlock project](https://planet.mblock.cc/project/3941523). If your school blocks the Makeblock site, [download `sound_localization_approach.mblock`](files/programs/sound_localization_approach.mblock) instead.

When running this program, be sure to fill in the correction factor you determined earlier, in the same [`left_scale` block](#fig:leftscale) as before.

The example program does the following:

1. It takes 3 measurements of sound intensity at the left and right ears.
2. Depending on which ear receives the loudest sound, the robot turns slightly left or right.
3. Next, the robot drives a few cm forward. And the cycle repeats.

This approach to sound localization results in a jittery path: the robot stops, measures, rotates, and moves. However, this approach gives the robot enough time to collect data (sound). Moreover, many animals adopt the same stopping-moving strategy when approaching sound sources. Even humans "stop to listen" when looking for their ringing phone. Biology and engineering use similar strategies!
