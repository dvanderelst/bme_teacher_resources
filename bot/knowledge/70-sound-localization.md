---
chapter: "Sound Localization"
source: 70-sound-localization.md
edition: "27 July 2026"
fingerprint: "677bb65-stale"
---

# Sound Localization

## Required materials

| Item | Description |
| :--- | :--- |
| mBot Robot | The mBot robot. |
| Bluetooth Dongle | A dongle for connecting the robot to a computer. Currently the recommended connection method. |
| Makeblock Sound Sensor | A sensor that reads current sound intensity. Used in the Sound Localization lesson and programming introduction. |
| Screws | The robot uses M4 machine screws. Provide extra screws for mounting additional sensors and the Robot Pipe Plate onto PVC pipe. |
| Extra cables (short) | Extra cables for connecting sensors. These allow students to add sensors without removing existing connections, preventing lost cables. Cables come in packs of 4; supply 1 extra per robot. Each is 20 cm long, matching the two cables included with the robot. |
| Lego compatible blocks | Blocks compatible with the robot's screw holes. These provide flexibility for mounting sensors as an alternative to provided brackets. |
| Materials to make robot ears | Students can make ears from modeling clay or craft paper. |
| Gaffer's tape | Versatile tape useful throughout the activities. |
| Batteries | The robot requires 4 AA batteries. A 100-pack provides sufficient spares: with more than 8 batteries per robot, you can swap batteries without interrupting the curriculum. |
| Speaker | A speaker for playing sounds during sound localization activities. |
| Measuring Tape | Measuring tape for setting up sound localization experiments. |

**Note:** Newer versions of the sensor have a potentiometer for adjusting sensitivity. For example, the sensor shown below has a small dial beside the microphone. Use a screwdriver to gently rotate the dial. If your sensor has such a dial, turn it to the halfway position on both sensors.

Figure: An image of the sound sensor with a dial for changing sensitivity (indicated by the arrow). ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/sound-localization-lesson-plan-98af73ad.png))

## Prerequisites

Students should be familiar with Microsoft Excel or Google Sheets, able to enter data, and create and read simple graphs. They should also understand how humans hear sound and have some understanding of algorithmic thinking and the design process.

## Investigating/Essential Questions

- How do humans localize sound?
- How does a microphone differ from a human ear?
- How can we use information from living animals to improve human technology (biomimicry)?
- What is phonotaxis?

## Educational Standards

## Introduction

In this lesson, students explore how humans localize sound and how robots can be programmed to do the same through phonotaxis. Sound localization has numerous applications. In engineering, localizing noise sources in machinery can improve design. Engineers typically use microphone arrays to pinpoint sound more precisely than two microphones or ears can. Other applications include speaker localization: some conference cameras automatically focus on the active speaker, providing visual information about who is speaking and improving recorded sound quality. Robots that interact with people increasingly use sound localization to approach speakers, allowing them to fixate on and identify the person talking, and point microphones optimally for better sound quality.

This lesson has two sections. First, students learn about human sound localization abilities, design and test pinnae for human ears, and investigate how microphones differ from human ears. Second, students apply what they have learned to design and test pinnae for their robots, enabling the robot to move toward a sound source.

This unit was created collaboratively with faculty from the University of Cincinnati College of Arts and Sciences, College of Engineering, and School of Education. Combining biology with engineering gives students a unique opportunity to understand the parallels between animal and robot behavior and sensory/sensor function. It addresses the Next Generation Science Standards (NGSS Lead States, 2013) and the International Society for Technology in Education Standards (International Society for Technology in Education, 2022).
3. Design pinnae for a human and a robot.
4. Explore the design and placement of the robot's ears to increase sensitivity to sound.
## Introduction to Sound Localization

Humans (and many other animals) use several cues to localize sound. These include interaural timing differences (the time difference for sound to reach each ear), interaural level differences (the loudness difference at each ear), and monaural spectral cues (how the pinna, or outer ear, shapes the frequency of incoming sound). Interaural timing and level differences help locate sounds on the horizontal plane, while monaural spectral cues help locate sounds on the vertical plane.

### Sound localization cues

Humans locate sound using multiple cues simultaneously: the difference in arrival time between the two ears, the difference in level, and how the outer ear alters sounds arriving from different directions. The article below provides a readable survey.

[How We Localize Sound — *Physics Today*](https://pubs.aip.org/physicstoday/article/52/11/24/410870/How-We-Localize-SoundRelying-on-a-variety-of-cues)

### Motivation

Engage students by asking for a volunteer to sit blindfolded in the middle of the room. Tell the volunteer you will make a sound, and they should point to the source when they hear it. Use a clicker, snap your fingers, or jingle keys. Walk quietly around the volunteer at ear level to the right or left. The person should be able to identify the sound's location fairly well. Then, quietly walk behind the volunteer and make the sound directly above their head. They will likely struggle to locate it. Humans are much better at localizing sound on the horizontal plane (using interaural timing and level differences) than on the vertical plane (using monaural spectral cues).

## Activity: pinnae design

In this activity, students create and test their own artificial pinnae to see whether these can increase the cues available for sound localization.

Testing artificial pinnae
## Microphones versus the human ear

Before moving to the robotics section, students need to understand how a microphone differs from the human ear. The robot will use sensors that do not allow precise timing of sound arrival at the microphones. Therefore, only sound loudness (intensity) can be used to approach a source.

### Sensitivity

The graph below is an **audiogram**. It is worth explaining how to read one, as the shape is counterintuitive.

Every point on a curve is a **threshold**: the faintest sound the animal can detect at that frequency. A curve that dips low means *good* hearing — the animal can detect fainter sounds. A curve that rises means hearing is *worse* there, requiring louder sounds before they register. The lowest point on a curve indicates the frequency the animal hears best. This graph does not indicate how loud a sound is; it shows how quiet a sound can be before becoming inaudible.

Figure: Audiograms for four species, with the sound sensor's threshold in red. Each curve gives the faintest sound that animal can detect at each frequency, so **lower on the graph means more sensitive**. Humans hear best at around 3 kHz, where the threshold dips below 0 dB SPL. The red line is flat because the sensor is about equally sensitive at every frequency, and it lies above all four curves because it is far less sensitive than any of these ears. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/sound-localization-lesson-plan-fd572681.png))

These are average curves. Hearing thresholds for individuals can vary significantly. The graph shows that humans are typically most sensitive around 3 kHz. Like a mouse, a small animal typically has a higher best frequency. To find similar curves for other animals, search for "audiogram x" (replacing x with the animal). Researchers have measured audiograms for many species.

The red line is the approximate threshold of the robot's sound sensor, estimated from manufacturer data. It sits at about 36 dB SPL — above every animal curve on the graph. The sensor is much less sensitive than any of these ears, which is not surprising, as animal ears are extraordinarily sensitive. Many sounds we hear easily are undetectable to the robot. The table of everyday sound levels gives context for what 36 dB SPL means.

Figure: Everyday sounds and their approximate levels. The sensor's threshold of about 36 dB SPL falls between a quiet whisper and a quiet auditorium, so anything fainter than a quiet room will not register at all. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/sound-localization-lesson-plan-58c2fb72.png))
Figure: A measured frequency response for a simple microphone. Unlike the schematic red line in the audiogram, this one is real data, but the story is the same: within a decibel or two, the microphone treats every frequency alike. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/sound-localization-lesson-plan-abed05bc.png))

You can demonstrate the contrast with your own ears using an online tone generator, playing tones of different frequencies without touching the volume control.

[Online Tone Generator - generate pure tones of any frequency](https://www.szynalski.com/tone-generator/)

Even with the volume fixed, sounds around 3000 Hz are perceived as louder than lower- and higher-frequency ones. Play a 2000 Hz tone, then stop it, move the slider to 10,000 Hz, and play again. Students will hear the change in pitch, of course, but they should also notice the 10,000 Hz tone sounds quieter, even though nothing about the volume has changed.

This has a practical consequence that is easy to miss, and it matters for the robot activities later in this chapter. Because our sensitivity falls away at both ends of the range and the sensor's does not, **your own ears are a poor guide to what the robot can hear.** A 10 kHz tone that sounds faint to you is no harder for the sensor than a 2 kHz tone that sounds loud, and a low rumble you can barely hear may be perfectly detectable to it. So when you are setting up a sound for the robot, judge it by what the robot reports rather than by how loud it seems in the room — and resist turning the volume up because a tone sounds quiet to you, since the sensor may be well above its threshold already.

### Directionality

### Frequency response

The audiogram reveals a second difference. The sensor is almost equally sensitive from 20 Hz to 20,000 Hz and beyond, which is why its line is flat and trails off at the right-hand edge. Our ears are not like that. Two sounds with the same physical amplitude at 2 kHz and 10 kHz do not sound equally loud to us: the 2 kHz tone sounds louder.

The curve describing how sensitive a microphone is at each frequency is called its **frequency response**. Because the red line is flat, an engineer would say this microphone has a *flat frequency response*. The red line is schematic rather than a measurement. A real one, measured from a simple microphone, is flat within a decibel or two across most of the range, with small ripples at the top end.

Figure: A measured frequency response for a simple microphone. Unlike the schematic red line in the audiogram, this one is real data, but the story is the same: within a decibel or two, the microphone treats every frequency alike. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/sound-localization-lesson-plan-abed05bc.png))

You can demonstrate this contrast with an online tone generator, playing tones of different frequencies without changing the volume.

[Online Tone Generator - generate pure tones of any frequency](https://www.szynalski.com/tone-generator/)

Even with the volume fixed, sounds around 3000 Hz are perceived as louder than lower- and higher-frequency ones. Play a 2000 Hz tone, then stop it, move the slider to 10,000 Hz, and play again. Students will hear the change in pitch, of course, but they should also notice the 10,000 Hz tone sounds quieter, even though the volume has not changed.

This has a practical consequence that is easy to overlook, and it matters for the robot activities. Because our sensitivity falls away at both ends of the range while the sensor's does not, **your own ears are a poor guide to what the robot can hear.** A 10 kHz tone that sounds faint to you is no harder for the sensor than a 2 kHz tone that sounds loud, and a low rumble you can barely hear may be perfectly detectable to it. When setting up a sound for the robot, judge it by what the robot reports rather than by how loud it seems in the room. Resist turning the volume up because a tone sounds quiet to you, as the sensor may already be well above its threshold.

### Directionality

The microphone is almost omnidirectional, meaning it is nearly equally sensitive to sounds from different directions. Our ears are not equally sensitive to all directions. Our heads and external ears block sound from specific directions and increase sound from others. This effect depends on frequency, making it a bit tricky to demonstrate. Use the directivity figure to convey this idea.

Figure: How sensitivity varies with the direction a sound comes from, for one ear and one frequency. The sphere is cut away so the inside is visible, and warmer colors mark the directions the ear picks up best. Figure from [LmK Music Production, *What is HRTF?*](https://lmkprod.com/what-is-hrtf-brief-explanation/). ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/sound-localization-lesson-plan-d5560ae5.png))

It shows the sensitivity of the left ear, at one frequency, as a function of the direction a sound arrives from. The sphere is cut in half so you can see inside, and warmer colors mark the directions the ear picks up best.

### Temporal response of the Makeblock sound sensor

**Note:** The key takeaway: the robot does not detect sounds longer than about 1 second. It detects only the onset (and offset) of sound. This explains why a pulsed sound is used for robotic activities. A constant sound would be undetectable to the robot.

For the technically inclined, there is a fourth way our ears differ from the robot's sound sensor. The electronics on the sensor board make it responsive to short bursts of sound, while continuous sound goes undetected no matter how loud.

**Aside:** **Important**

This is a quirk of the Makeblock sound sensor, not a general microphone characteristic. The microphone itself follows a continuous sound perfectly. It is the amplifier circuit on the sensor board that removes the steady part of the signal and passes on only the changes. A different sound sensor would behave differently, and the microphone in a phone or laptop certainly does. Be explicit about this with students, as "microphones cannot hear continuous sounds" is both memorable and incorrect.

On the Makeblock sound sensor, the microphone is the round black disk on the sensor board. However, you will notice many other tiny electronic components. These primarily amplify the microphone's signal before sending it to the robot. They also filter the signal so it is high for short, loud bursts of sound. Almost no signal is transmitted to the robot during long bursts.

The oscilloscope trace plots the signal reaching the robot over about ten seconds. At the first red arrow a sound starts playing, and the signal jumps up: the sensor has noticed. But it then falls away, and after about a second it is back at baseline even though the sound is still playing. At the second arrow the sound stops, and the signal dips below baseline for a second or so before recovering. What the sensor reports is not the sound but the *changes* in it.

Figure: The sensor's output on an oscilloscope, over about ten seconds. The sound starts at the first arrow and stops at the second. Both edges produce a response that decays back to baseline within about a second; the steady sound in between produces nothing at all. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/sound-localization-lesson-plan-d9268e13.png))

### Conclusions

Now ask students to list the three (or four) main differences between microphones and human ears. These differences affect how the microphones can be used to steer the robot toward sound. After formatively assessing that students understand, consider how these aspects affect robotic sound localization.
### Background: hearing sensitivity

Our ears are very sensitive, and it is worth quantifying this. The faintest sound a person can hear at around 2 kHz corresponds to a sound pressure of about **20 micropascal** — the figure that defines 0 dB SPL, and the bottom row of the table of sound levels earlier in this chapter.

That 20 micropascal is an RMS value: a kind of average taken over the cycle, not the peak. For a pure tone, the peak is √2 times the RMS value, so at the eardrum the pressure rises about 28 micropascal above atmospheric pressure and falls about 28 micropascal below it. The full swing from top to bottom of the cycle is about **57 micropascal**. This rising and falling pressure pushes and pulls the eardrum, and that movement is eventually perceived as sound.

We can turn that pressure into a force. A pressure of 57 micropascal is 5.8 × 10⁻⁷ grams-force per square centimetre — the weight of just under six ten-millionths of a gram resting on each square centimetre. Force is pressure times area, and the eardrum is about 0.5 cm², so the force on it is about **2.9 × 10⁻⁷ grams-force**, or 0.0000003 grams.

So our ears detect the equivalent of three ten-millionths of a gram being laid on the eardrum and lifted off again, two thousand times a second. A grain of salt weighs about 0.00006 grams — two hundred times more. Imagine a kitchen scale that could weigh a two-hundredth of a grain of salt, and read it two thousand times a second.

## Activity: robot phonotaxis

In this robotic activity, students create a robot that performs phonotaxis. Phonotaxis is the directional movement of an organism with respect to a sound source. The robot compares sound intensity between two sensors to determine whether to turn left or right to move closer to the sound source. Find the activity instructions by following the link below:

Robot phonotaxis

## Assessment Questions

Below are two questions to assess students' comprehension.

**Aside:** Question 1: How does creating 'ears' on the robot increase the robot's ability to respond to sound? Support your reasoning by comparing the measurement made without ears against the one made with ears fitted.

Answer: The variability of each ear has increased. With ears fitted, the right ear ranges from about 380 at -40 degrees down to about 170 at +40, a spread of roughly 210. Without ears it stayed between about 310 and 380, a spread of roughly 70. This increased variability is beneficial: it means the microphone's output varies more with the angle to the sound source. This increased directionality should make sound localization easier (or more reliable).
## Testing artificial pinnae

### Introduction

Before the development of radar, approaching airplanes were often detected and localized acoustically. To increase the range and precision of airplane localization, people built devices to enhance human hearing. Below are pictures of such devices. The following article provides further explanation.

[How warplanes were spotted before radar | CNN](https://www.cnn.com/style/article/war-sound-locators-before-radar/index.html)

Figure: Two Dutch personal sound locators. Each funnels sound from a wide area into the operator's ears, and each turns on its base so the operator can sweep for the direction the sound is loudest. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/testing-artificial-pinnae-affed672.png))

Figure: Four more locators. Note how many use pairs or quads of horns rather than one: separating the collectors widens the difference between what each ear receives, which is exactly what students are trying to achieve with their own pinnae. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/testing-artificial-pinnae-06410d6c.png))

Figure: Left, a locator using honeycomb collectors rather than horns. Right, a row of them on wheeled carriages, ready to be moved into position. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/testing-artificial-pinnae-6587bd75.jpg))

Figure: Left, a head-mounted locator, which is the closest of these to the pinnae students will build. Right, a large locator worked by three operators at once. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/testing-artificial-pinnae-f4295f63.png))

All these devices were designed to increase the cues available for sound localization. In this activity, students build their own devices to enhance sound localization.

### Activity

Students pair up for their sound localization test. They build pinnae to enhance their ability to locate sound, then test their design's effectiveness. For inspiration, show students pictures of acoustic locators built in the early 20th century or various animal ears. Previously, we provided students with cardboard, pipe cleaners, tape, etc., to build artificial pinnae. Examples of student-built ears appear below.

Figure: Pinnae made from card cones on a headband. The shape gathers sound from in front of the ear and shields it from behind. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/testing-artificial-pinnae-fe673636.jpg))

Figure: A flatter design, taped to the side of the head. Reflecting surfaces need not be cone-shaped to change what reaches the ear. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/testing-artificial-pinnae-540a5939.jpg))

Figure: Large cones covering both ears. Designs this size change the loudness reaching each ear substantially, but they also make it hard to tell front from back. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/testing-artificial-pinnae-f88f6efd.jpg))

Figure: Picture of students engaged in the experiment, testing their self-made external pinnae. The large sheet of paper on the floor is not part of the current activity. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/testing-artificial-pinnae-e2beccd3.jpg))

The procedure runs via an app, which walks a pair through the trials, tells them where to place the speaker, plays the sound, and scores the result.

[soundlocalizationapp-production.up.railway.app](https://soundlocalizationapp-production.up.railway.app)

It is designed for a phone; the quickest way to start a class is to put this QR code on the board. It also runs on a laptop.

Figure: The code students can scan to open the sound localization app on their phones. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/sound-localization-app-qr.png))

On the opening screen, a pair enters a name, chooses whether this run uses **Real ears** or **Artificial ears**, and sets the number of trials — fewer if time is short. The `Instructions` bar expands into a full description of the activity, including how to lay the setup out, so students can work from the app rather than from a handout.

Figure: The opening screen. The `Instructions` bar at the top expands into the full procedure, including how to arrange the room. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/sound-localization-app-start.png))

Each trial tells the pair where to place the speaker, waits while they play the sound, and records the listener's answer.
## Robot phonotaxis

This activity creates a robot that follows a sound source. Use the sound file provided on a phone or portable speaker. When the sound source is held close (~50 cm) to the robot, the robot should turn toward the sound and approach it. The robot does this by comparing sound intensity between the left and right microphones. If the sound is louder at the left receiver, it turns left, and vice versa. This is a form of phonotaxis.

In principle, the robot could approach a sound source anywhere in the environment. However, as discussed earlier, the microphones are not very sensitive, so the robot may struggle with distant sound sources.

**Note:** This robotic activity works best if the sound source the robot is approaching is the only sound source. This means it is difficult to do this activity with different groups in the same room.

**Note:** Because the robot's sensors are not very sensitive, turn the speaker or phone volume up quite high. However, do not turn it up so much that it is uncomfortable or that you need to raise your voice to be understood by someone three feet away. Loud noise can damage hearing. If in doubt, students could wear hearing protection.

**Note:** In the programs provided for this activity, we assume the left microphone is plugged into port 3 and the right microphone into port 4.

### Step 1: Measuring the directionality of the microphones

**Note:** If time is limited, Step 1 (measuring the robot's directionality without external ears) can be skipped. However, we still recommend discussing the lack of directionality of bare microphones so students understand why they need to add external ears to the robot.

If we want to find sound by comparing intensities at both receivers, the left microphone must be more sensitive than the right for sound coming from the left. However, this is not guaranteed. As previously discussed, the microphones are almost omnidirectional. Therefore, they pick up sound almost equally from all directions. A sound to the left of the robot may stimulate both microphones equally, leaving the robot unable to determine direction.

In this step, students measure the microphones' directionality. Provide the robot with two microphone sensors, mounted as shown below.

**Note:** If you mount the sound sensors as shown, do not overtighten the screws. This might damage the sensors.

Figure: The two sound sensors mounted on the front of the robot, angled outwards so that each faces a different side. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-5f001102.jpg))

Figure: One of the sensors close up. The microphone is the small black disc; the rest of the board amplifies and filters its signal. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-9b19fbad.jpg))

Figure: The sound sensor. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-e133beed.jpg))

Next, have students build a setup like the one shown below. Students can place a large sheet of paper or a whiteboard on the floor (as in the example) and draw several compass directions. In the example, angles from -40 to 40 degrees are drawn in 20-degree steps. Place the sound source at an angle of 0° and about 50 cm from the robot. The sound source can be a phone or a speaker.

Figure: Measuring directionality. The robot sits at the centre of a protractor scale so it can be rotated to a known angle between readings. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-748fdb0b.jpg))

Have the sound source play the following sound on repeat. The sound consists of bursts of white noise. Temporal response of the Makeblock sound sensor explains why this sound is pulsed. Click the link below, then click the 3 dots in the sound player to download the file.

[Pulsed tone for the robot (.mp3)](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/files/pip_exported.mp3)

Students should align the robot with each marked direction. Run the program below. In the program, ensure the `set left_scale` block contains the value 1. You can change this number by clicking on the small oval containing the number.

Figure: The `left_scale` block, which holds the correction factor. It starts at 1, meaning no correction. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-35eb8c6f.png))

When they click the green flag, the robot will take 20 measurements of sound intensity from the left and right microphones, then calculate the average. The robot will beep when done. Once the robot beeps, students should record the `left_sound` and `right_sound` values.

Next, turn the robot to align it with the next direction and click the green button again to measure the next angle. This way, students determine the loudness of the sound as perceived by both microphones at different positions relative to the sound source.

**Tip:** If you use the program below, the mBlock software will automatically load an extension that allows you to work with the sound sensor. To start programming from scratch, you must add the extension yourself. Click the following link for instructions:

Adding the sound sensor extension
### Step 2: Make the ears directional

Students can make the ears (microphones) directional by constructing artificial pinnae around the microphones. Students can use paper, modeling clay, or other materials. In the example below, we made external ears by rolling sheets of paper into cones. Notice the ears are quite large relative to the robot. Larger ears typically result in higher directionality. We also show images of a student's robot with external ears made from modeling clay.

Figure: Paper cone ears, taped to the sensors and angled outwards. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-3b931d59.jpg))

Figure: A moulded pair, shaped to gather sound from one side and shield the other. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-3c135ee9.jpg))

Figure: Another design. What matters is not realism but that the two ears face away from each other. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-5b1579be.jpg))

Figure: Students take the brief further than strictly necessary, which is no bad thing. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-caff0520.jpg))

Once students have created ears for their robots, have them repeat the measurements above. The graph should now show clear directionality. If not, they should keep working on the ears until they achieve directional sensitivity. Without directional ears, the robot cannot localize sound.

Below is an example of data collected with directional ears. These data show that the right ear picks up more sound when the source is to the robot's right (negative angles), and vice versa.

Figure: The same measurement with ears fitted. The lines now separate and cross: each ear hears its own side more loudly, which is the difference the robot steers on. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-f4124490.png))

One problem that often occurs with students' external ears is that the amount of sound picked up by the left and right ears is not the same at zero degrees. In the example data, when the sound source is directly in front of the robot, the left ear picks up more sound than the right. The left ear appears more sensitive overall. This indicates the left ear is more sensitive than the right. At angle zero, the right value is about 70% of the left ear value:

$$
\frac{right ear value at zero degrees}{left ear value at zero degrees} \approx \frac{250}{340} \approx 0.7
$$

Student values will differ. Perhaps their right ear is more sensitive than the left. In this case, the equation above will return a value larger than 1.

We can correct for microphone sensitivity differences. The example program provides the `left_scale` block for this. Enter the result of the equation into that block to correct for differences. For the example above, enter 0.7.

Figure: Setting the correction factor. Here the left microphone reads high, so `left_scale` is set below 1 to bring the two into agreement. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-3f2fd20b.png))

Students could rerun the measurements to check whether this correction results in the left and right ears picking up about the same amount of sound at zero degrees. Below is an example graph.

Figure: After scaling. The two curves now cross close to zero degrees, so equal loudness means the sound really is straight ahead. ([image](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/images/robot-phonotaxis-6f33c641.png))

Now, the left and right ear values are approximately equal at angle zero. Moreover, the left ear returns a higher value if the sound source is on the robot's left side (angle > 0). The right ear has a larger response when the sound source is on the robot's right side (angle < 0). These response curves enable phonotaxis.

### Step 3: Phonotaxis

Now have the robot follow a sound source. Students can run the example program. The robot should approach the sound source. They can try moving the sound source while the program runs to see if the robot notices the change.

[Open the mBlock project](https://planet.mblock.cc/project/3941523). If your school blocks the Makeblock site, [download `sound_localization_approach.mblock`](https://github.com/dvanderelst/bme_teacher_resources/raw/main/book/content/files/programs/sound_localization_approach.mblock) instead.

When running this program, enter the correction factor determined earlier in the same `left_scale` block as before.

The example program does the following:

1. It takes 3 measurements of sound intensity at the left and right ears.
2. Depending on which ear receives the loudest sound, the robot turns slightly left or right.
3. Next, the robot drives a few cm forward. The cycle repeats.

This approach to sound localization results in a jittery path: the robot stops, measures, rotates, and moves. However, this approach gives the robot enough time to collect data. Moreover, many animals adopt the same stopping-moving strategy when approaching sound sources. Even humans "stop to listen" when looking for their ringing phone. Biology and engineering use similar strategies!
