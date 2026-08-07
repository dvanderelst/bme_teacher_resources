# Sound Localization

## Materials

| Item | Description |
| :--- | :--- |
| mBot robot | The mBot robot. |
| Bluetooth dongle | A dongle for connecting the robot to a computer. Currently the recommended connection method. |
| Makeblock sound sensor | A sensor that reads current sound intensity. Used in the sound localization lesson and programming introduction. |
| Screws | The robot uses M4 machine screws. Provide extra screws for mounting additional sensors and the Robot Pipe Plate onto PVC pipe. |
| Extra cables (short) | Extra cables for connecting sensors. These allow students to add sensors without removing existing connections, preventing lost cables. Cables come in packs of 4. Supply 1 extra per robot. Each is 20 cm long, matching the two cables included with the robot. |
| Lego-compatible blocks | Blocks compatible with the robot's screw holes. These provide flexibility for mounting sensors as an alternative to provided brackets. |
| Materials to make robot ears | Students can make ears from modeling clay or craft paper. |
| Gaffer's tape | Versatile tape useful throughout the activities. |
| Batteries | The robot requires 4 AA batteries. A 100-pack provides sufficient spares. With more than 8 batteries per robot, you can swap batteries without interrupting the curriculum. |
| Speaker | A speaker for playing sounds during sound localization activities. |
| Measuring tape | Measuring tape for setting up sound localization experiments. |

## Prerequisites

Students should be familiar with Microsoft Excel or Google Sheets and able to enter data and create and read simple graphs. They should also understand how humans hear sound and have some understanding of algorithmic thinking and the design process.

## Investigating / Essential Questions

- How do humans localize sound?
- How does a microphone differ from a human ear?
- How can we use information from living animals to improve human technology (biomimicry)?
- What is phonotaxis?

## Educational Standards

The educational standards applicable to this lesson are listed in the [Educational Standards](#standards) chapter.

## Introduction

In this lesson, students explore how humans localize sound and how robots can be programmed to do the same through phonotaxis. Sound localization has numerous applications. In engineering, localizing noise sources in machinery can improve design. Engineers typically use microphone arrays to pinpoint sound more precisely than two microphones or ears can. Other applications include speaker localization. Some conference cameras automatically focus on the active speaker, providing visual information about who is speaking and improving recorded sound quality. Robots that interact with people increasingly use sound localization to approach speakers. This allows them to fixate on and identify the person talking and point microphones optimally for better sound quality.

This lesson has two sections. First, students learn about human sound localization abilities and design and test pinnae for human ears. They also investigate how microphones differ from human ears. Second, students apply what they have learned to design and test pinnae for their robots, enabling the robot to move toward a sound source.

This unit was created collaboratively with faculty from the University of Cincinnati College of Arts and Sciences, College of Engineering, and School of Education. Combining biology with engineering gives students a unique opportunity to understand the parallels between animal and robot behavior and between sensory and sensor function. It addresses the Next Generation Science Standards (NGSS Lead States, 2013) and the International Society for Technology in Education Standards (International Society for Technology in Education, 2022).

## Background: sound localization

Humans and many other animals use several cues to localize sound. These include interaural timing differences (the time difference for sound to reach each ear), interaural level differences (the loudness difference at each ear), and monaural spectral cues (how the pinna, or outer ear, shapes the frequency of incoming sound). Interaural timing and level differences help locate sounds on the horizontal plane, while monaural spectral cues help locate sounds on the vertical plane.

### Sound localization cues

Humans locate sound using multiple cues simultaneously: the difference in arrival time between the two ears, the difference in level, and how the outer ear alters sounds arriving from different directions. The article below provides a readable survey.

[How We Localize Sound — *Physics Today*](https://pubs.aip.org/physicstoday/article/52/11/24/410870/How-We-Localize-SoundRelying-on-a-variety-of-cues)

### Motivation

Engage students by asking for a volunteer to sit blindfolded in the middle of the room. Tell the volunteer you will make a sound, and they should point to the source when they hear it. Use a clicker, snap your fingers, or jingle keys. Walk quietly around the volunteer at ear level to the right or left. The person should be able to identify the sound's location fairly well. Then, quietly walk behind the volunteer and make the sound directly above their head. They will likely struggle to locate it. Humans are much better at localizing sound on the horizontal plane using interaural timing and level differences than on the vertical plane using monaural spectral cues.

## Activity: pinnae design

In this activity, students create and test their own artificial pinnae to see whether these can increase the cues available for sound localization.

[Testing artificial pinnae](#testing-artificial-pinnae)

## Microphones versus the human ear

Before moving to the robotics section, students need to understand how a microphone differs from the human ear. The robot will use sensors that do not allow precise timing of sound arrival at the microphones. Therefore, only sound loudness (intensity) can be used to approach a source.

### Sensitivity

The graph below is an **audiogram**. It is worth explaining how to read one, as the shape is counterintuitive.

Every point on a curve is a **threshold**: the faintest sound the animal can detect at that frequency. A curve that dips low means *good* hearing. The animal can detect fainter sounds. A curve that rises means hearing is *worse* there, requiring louder sounds before they register. The lowest point on a curve indicates the frequency the animal hears best. This graph does not indicate how loud a sound is. It shows how quiet a sound can be before becoming inaudible.

![Audiograms for eleven species, with the mBot's sound sensor added as the dashed black line. Each curve gives the faintest sound that animal can detect at each frequency, so **lower on the graph means more sensitive**. The U shape says that every ear has a best frequency with sensitivity falling away on either side of it. Humans hear best at around 3 kHz, where the threshold dips below 0 dB SPL. The sensor's line is flat because it is about equally sensitive at every frequency. Audiogram figure from Lue, P.-Y., Oliver, M. H., Neeff, M., Thorne, P. R. & Suzuki-Kerr, H. (2023), *Sheep as a large animal model for hearing research: comparison to common laboratory animals and humans*, Laboratory Animal Research 39:31, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The sensor line and its label are our addition.](images/sound-localization-audiogram.png){#fig:audiogram}

These are average curves. Hearing thresholds for individuals can vary significantly. The graph shows that humans are typically most sensitive around 3 kHz. The smaller the animal, the higher its best frequency tends to be: the mouse and the rat hear best above 10 kHz, which is territory a human ear barely reaches at all. The sheep, pig, dog, cat, and monkey, animals nearer our own size, have their best frequencies much closer to ours.

Curves like these have been measured for a great many species. There is a database of them: the [Animal Audiogram Database](https://www.animalaudiograms.org), built at the Museum für Naturkunde Berlin. It is free, needs no account to browse, and every curve in it was extracted by hand from a peer-reviewed paper and linked back to it. You can select several species and have them drawn on one set of axes. In other words, you can build a version of the figure above for whichever animals you like and download the numbers behind it.

One caveat worth knowing before you send a class there: it currently covers **marine mammals and birds**, so it has none of the eleven species plotted above. A group comparing a seal, a dolphin, and a penguin can produce that kind of plot in a couple of minutes. For a terrestrial mammal, searching for "audiogram" and the animal's name is still the way.

### Where the sensor's line comes from

The dashed line is the approximate threshold of the robot's sound sensor. It is worth seeing where the number comes from rather than taking it on trust. Makeblock's datasheet gives the microphone a **signal-to-noise ratio of 54 dB**. By convention, this is measured against a 1 pascal sound (94 dB SPL), so the microphone's own electrical hiss is equivalent to a sound of

$$94 - 54 = 40\ \text{dB SPL}$$

Below that level, whatever the microphone produces is buried in its own noise. So **40 dB SPL** is the sensor's floor, and that is where the line is drawn.

Treat it as an upper bound on the sensor's quality rather than a precise figure. Makeblock does not say which capsule is on the board. Capsules of this class are commonly specified at 60 dB rather than 54, which would put the floor nearer 34 dB SPL. We use the number the manufacturer publishes for the board they actually sell.

Two things follow. First, this is a *best case*: it is the microphone capsule alone, in silence. The amplifier on the sensor board adds noise of its own. The robot's analog-to-digital converter rounds the result to one of 1024 steps. A classroom with children in it sits at 50–60 dB SPL. In a real room, the robot's threshold is set by the room, not by the microphone.

Second, look at where that line falls. It is above every curve on the graph, so there is no animal here that the sensor can out-hear, but the margin varies enormously. Against a human, a cat, or a dog, whose curves bottom out around or below 0 dB SPL, the sensor is 45–50 dB worse, a factor of two to three hundred in sound pressure. Against the mouse and the rat, it is only a few decibels worse. The small rodents' ears, for all that they reach far higher frequencies than ours, are not especially sensitive in absolute terms. A cheap electret microphone is nearly their equal.

The table below gives context for what 40 dB SPL means. It sits at the bottom of the range for a normal conversation, so the robot can just hear people talking. It is above a very calm room, so an empty, quiet classroom registers as nothing at all. Leaves rustling at about 10 dB SPL carry a thousandth of the sound power the sensor needs before it notices anything.

| Sound | Measured | dB SPL |
| :--- | :--- | ---: |
| Threshold of pain | at the ear | 120 |
| Two-stroke chainsaw | 1 m | 110 |
| Jackhammer | 1 m | 100 |
| Hearing damage from long exposure | at the ear | 85 |
| Vacuum cleaner | 1.8 m | 85 |
| Television | in the room | 75 |
| Passenger car at 30 km/h | 10 m | 65–70 |
| Normal conversation | 1 m | 40–60 |
| **The mBot's sound sensor, at its threshold** | — | **40** |
| Very calm room | in the room | 20–30 |
| Leaves rustling; calm breathing | in the room | 10 |
| Threshold of human hearing at 1 kHz | at the ear | 0 |
| Anechoic chamber, University of Salford | in the room | -12 |

Two rows of that table are worth dwelling on with a class. **Normal conversation spans 40–60 dB**, which straddles the sensor's threshold: the robot hears the loud half of a conversation and misses the quiet half. And the **threshold of human hearing is 0 dB**, forty decibels below the sensor, a hundredfold difference in sound pressure, and that is before considering that our ears reach it only in the narrow band around 3 kHz where they are best.

Values are drawn from the *Sound pressure* article on Wikipedia, which cites a source for each. The selection and the wording here are ours.

You can demonstrate the contrast with your own ears using an online tone generator, playing tones of different frequencies without touching the volume control.

[Online Tone Generator - generate pure tones of any frequency](https://www.szynalski.com/tone-generator/)

Even with the volume fixed, sounds around 3000 Hz are perceived as louder than lower- and higher-frequency ones. Play a 2000 Hz tone, then stop it, move the slider to 10,000 Hz, and play again. Students will hear the change in pitch, of course, but they should also notice the 10,000 Hz tone sounds quieter, even though nothing about the volume has changed.

This has a practical consequence that is easy to miss, and it matters for the robot activities later in this chapter. Because our sensitivity falls away at both ends of the range and the sensor's does not, **your own ears are a poor guide to what the robot can hear.** A 10 kHz tone that sounds faint to you is no harder for the sensor than a 2 kHz tone that sounds loud, and a low rumble you can barely hear may be perfectly detectable to it. So when you are setting up a sound for the robot, judge it by what the robot reports rather than by how loud it seems in the room. And resist turning the volume up because a tone sounds quiet to you, since the sensor may be well above its threshold already.

### Frequency response

The [audiogram](#fig:audiogram) reveals a second difference. The sensor is almost equally sensitive at every frequency, which is why its line is straight and level while every animal curve is a U. Our ears are not like that. Two sounds with the same physical amplitude at 2 kHz and 10 kHz do not sound equally loud to us: the 2 kHz tone sounds louder.

The curve describing how sensitive a microphone is at each frequency is called its **frequency response**. Because the sensor's line is flat, an engineer would say this microphone has a *flat frequency response*. That line is schematic rather than a measurement: a single number drawn across the whole range. A [measured one](#fig:freqresp) is not perfectly flat, but it is close: level to within a fraction of a decibel from 50 Hz to about 2.5 kHz, then some 3 dB up around 6 kHz and about 4 dB down by 20 kHz. Set against an ear, whose threshold swings by fifty or sixty decibels across the same span, that counts as flat.

![The measured frequency response of an electret condenser microphone, a CUI Devices CMA-4544PF-W: the same class of capsule as the one on the robot's sound sensor. It is not the identical part: Makeblock does not publish which capsule it uses, and the one we can look up differs in its quoted signal-to-noise ratio, though its output impedance and current draw match. The shape is what matters here, and it is the shape every capsule of this kind has: level from 50 Hz to about 2.5 kHz, a gentle rise of about 3 dB near 6 kHz, and a fall of about 4 dB by 20 kHz. Compare the sweep of an ear over the same range. Redrawn by us from the values in the manufacturer's datasheet.](images/sound-localization-frequency-response.png){#fig:freqresp}

You can demonstrate this contrast with an online tone generator, playing tones of different frequencies without changing the volume.

[Online Tone Generator - generate pure tones of any frequency](https://www.szynalski.com/tone-generator/)

Even with the volume fixed, sounds around 3000 Hz are perceived as louder than lower- and higher-frequency ones. Play a 2000 Hz tone, then stop it, move the slider to 10,000 Hz, and play again. Students will hear the change in pitch, of course, but they should also notice the 10,000 Hz tone sounds quieter, even though the volume has not changed.

This has a practical consequence that is easy to overlook, and it matters for the robot activities. Because our sensitivity falls away at both ends of the range while the sensor's does not, **your own ears are a poor guide to what the robot can hear.** A 10 kHz tone that sounds faint to you is no harder for the sensor than a 2 kHz tone that sounds loud, and a low rumble you can barely hear may be perfectly detectable to it. When setting up a sound for the robot, judge it by what the robot reports rather than by how loud it seems in the room. Resist turning the volume up because a tone sounds quiet to you, as the sensor may already be well above its threshold.

### Directionality

The microphone is almost omnidirectional, meaning it is nearly equally sensitive to sounds from different directions. Our ears are not equally sensitive to all directions. Our heads and external ears block sound from specific directions and increase sound from others. This effect depends on frequency, making it a bit tricky to demonstrate. Use the [directivity figure](#fig:hrtf) to convey this idea.

![How sensitivity varies with the direction a sound comes from, for one ear and one frequency. The sphere is cut away so the inside is visible, and warmer colors mark the directions the ear picks up best. Figure from [LmK Music Production, *What is HRTF?*](https://lmkprod.com/what-is-hrtf-brief-explanation/).](images/sound-localization-lesson-plan-d5560ae5.png){#fig:hrtf}

It shows the sensitivity of the left ear, at one frequency, as a function of the direction a sound arrives from. The sphere is cut in half so you can see inside, and warmer colors mark the directions the ear picks up best.

### Temporal response of the Makeblock sound sensor

> **Note**
>
> The key takeaway: the robot does not detect sounds longer than about 1 second. It detects only the onset (and offset) of sound. This explains why a pulsed sound is used for robotic activities. A constant sound would be undetectable to the robot.

For the technically inclined, there is a fourth way our ears differ from the robot's sound sensor. The electronics on the sensor board make it responsive to short bursts of sound while continuous sound goes undetected no matter how loud.

> **Important**
>
> This is a quirk of the Makeblock sound sensor, not a general microphone characteristic. The microphone itself follows a continuous sound perfectly. It is the amplifier circuit on the sensor board that removes the steady part of the signal and passes on only the changes. A different sound sensor would behave differently, and the microphone in a phone or laptop certainly does. Be explicit about this with students, as "microphones cannot hear continuous sounds" is both memorable and incorrect.

On the Makeblock sound sensor, the microphone is the round black disk on the sensor board. However, you will notice many other tiny electronic components. These primarily amplify the microphone's signal before sending it to the robot. They also filter the signal so it is high for short, loud bursts of sound. Almost no signal is transmitted to the robot during long bursts.

The [oscilloscope trace](#fig:temporal) plots the signal reaching the robot over about ten seconds. At the first red arrow a sound starts playing, and the signal jumps up: the sensor has noticed. But it then falls away, and after about a second it is back at baseline even though the sound is still playing. At the second arrow the sound stops, and the signal dips below baseline for a second or so before recovering. What the sensor reports is not the sound but the *changes* in it.

![The sensor's output on an oscilloscope, over about ten seconds. The sound starts at the first arrow and stops at the second. Both edges produce a response that decays back to baseline within about a second; the steady sound in between produces nothing at all.](images/sound-localization-lesson-plan-d9268e13.png){#fig:temporal}

### Conclusions

Now ask students to list the three or four main differences between microphones and human ears. These differences affect how the microphones can be used to steer the robot toward sound. After formatively assessing that students understand, consider how these aspects affect robotic sound localization.

### Background: hearing sensitivity

Our ears are very sensitive, and it is worth quantifying this. The faintest sound a person can hear at around 2 kHz corresponds to a sound pressure of about **20 micropascal**—the figure that defines 0 dB SPL and the bottom row of the table of sound levels earlier in this chapter.

That 20 micropascal is an RMS value: a kind of average taken over the cycle, not the peak. For a pure tone, the peak is √2 times the RMS value, so at the eardrum the pressure rises about 28 micropascal above atmospheric pressure and falls about 28 micropascal below it. The full swing from top to bottom of the cycle is about **57 micropascal**. This rising and falling pressure pushes and pulls the eardrum, and that movement is eventually perceived as sound.

We can turn that pressure into a force. A pressure of 57 micropascal is 5.8 × 10⁻⁷ grams-force per square centimetre, the weight of just under six ten-millionths of a gram resting on each square centimetre. Force is pressure times area, and the eardrum is about 0.5 cm², so the force on it is about **2.9 × 10⁻⁷ grams-force**, or 0.0000003 grams.

So our ears detect the equivalent of three ten-millionths of a gram being laid on the eardrum and lifted off again, two thousand times a second. A grain of salt weighs about 0.00006 grams, two hundred times more. Imagine a kitchen scale that could weigh a two-hundredth of a grain of salt and read it two thousand times a second.

## Activity: robot phonotaxis

In this robotic activity, students create a robot that performs phonotaxis. Phonotaxis is the directional movement of an organism with respect to a sound source. The robot compares sound intensity between two sensors to determine whether to turn left or right to move closer to the sound source. Find the activity instructions by following the link below:

[Robot phonotaxis](#robot-phonotaxis)

## Assessment questions

Below are two questions to assess students' comprehension.

> **Question 1:** How does creating 'ears' on the robot increase the robot's ability to respond to sound? Support your reasoning by comparing the measurement made [without ears]() against the one made [with ears fitted]().
>
> **Answer:** The variability of each ear has increased. With ears fitted, the right ear ranges from about 380 at -40 degrees down to about 170 at +40, a spread of roughly 210. Without ears it stayed between about 310 and 380, a spread of roughly 70. This increased variability is beneficial: it means the microphone's output varies more with the angle to the sound source. This increased directionality should make sound localization easier or more reliable.
## Testing artificial pinnae

### Introduction

Before the development of radar, approaching airplanes were often detected and localized acoustically. To increase the range and precision of airplane localization, people built devices to enhance human hearing. Below are pictures of such devices. The following article provides further explanation.

[How warplanes were spotted before radar | CNN](https://www.cnn.com/style/article/war-sound-locators-before-radar/index.html)

![Two acoustic locators, and the same idea twice over. **Left**, a US Army locator of 1925: four horns collect sound and pipe it down rubber tubes to the ears of two operators, one listening for up-and-down, the other for left-and-right. **Right**, a pair of much larger horns at Bolling Field, Washington, worked by a single operator standing beneath them. In both, the horns gather sound from a wide area and deliver it to a human ear, and the whole frame turns so the operator can sweep until the sound is loudest, which is what tells them the direction. Both photographs are in the public domain.](images/sound-localization-locators-1.jpg)

![**Left**, a row of Japanese locators on wheeled carriages, each with four horns, being inspected before the Second World War. **Right**, the US Army's T3 locator of 1927, using faceted collectors rather than round horns. Note how many of these use pairs or quads rather than a single collector, and how far apart the collectors are set: separating them widens the difference between what each ear receives, which is exactly what students are trying to achieve with their own pinnae. Both photographs are in the public domain.](images/sound-localization-locators-2.jpg)

All these devices were designed to increase the cues available for sound localization. In this activity, students build their own devices to enhance sound localization.

### Activity

Students pair up for their sound localization test. They build pinnae to enhance their ability to locate sound, then test their design's effectiveness. For inspiration, show students pictures of acoustic locators built in the early 20th century or various animal ears. Previously, we provided students with cardboard, pipe cleaners, tape, etc., to build artificial pinnae. Examples of student-built ears appear below.

![Pinnae made from card cones on a headband. The shape gathers sound from in front of the ear and shields it from behind.](images/testing-artificial-pinnae-fe673636.jpg)

![A flatter design, taped to the side of the head. Reflecting surfaces need not be cone-shaped to change what reaches the ear.](images/testing-artificial-pinnae-540a5939.jpg)

![Large cones covering both ears. Designs this size change the loudness reaching each ear substantially, but they also make it hard to tell front from back.](images/testing-artificial-pinnae-f88f6efd.jpg)

![Picture of students engaged in the experiment, testing their self-made external pinnae. The large sheet of paper on the floor is not part of the current activity.](images/testing-artificial-pinnae-e2beccd3.jpg)

The procedure runs via an app, which walks a pair through the trials, tells them where to place the speaker, plays the sound, and scores the result.

[soundlocalizationapp-production.up.railway.app](https://soundlocalizationapp-production.up.railway.app)

It is designed for a phone. The quickest way to start a class is to put this QR code on the board. It also runs on a laptop.

![The code students can scan to open the sound localization app on their phones.](images/sound-localization-app-qr.png){#fig:sl-qr}

On the opening screen, a pair enters a name, chooses whether this run uses **Real ears** or **Artificial ears**, and sets the number of trials, fewer if time is short. The `Instructions` bar expands into a full description of the activity, including how to lay the setup out, so students can work from the app rather than from a handout.

![The opening screen. The `Instructions` bar at the top expands into the full procedure, including how to arrange the room.](images/sound-localization-app-start.png){#fig:sl-start}

Each trial tells the pair where to place the speaker, waits while they play the sound, and records the listener's answer.

## Robot phonotaxis

This activity creates a robot that follows a sound source. Use the sound file provided on a phone or portable speaker. When the sound source is held close (~50 cm) to the robot, the robot should turn toward the sound and approach it. The robot does this by comparing sound intensity between the left and right microphones. If the sound is louder at the left receiver, it turns left, and vice versa. This is a form of phonotaxis.

In principle, the robot could approach a sound source anywhere in the environment. However, as discussed earlier, the microphones are not very sensitive, so the robot may struggle with distant sound sources.

> **Note**
>
> This robotic activity works best if the sound source the robot is approaching is the only sound source. This means it is difficult to do this activity with different groups in the same room.

> **Note**
>
> Because the robot's sensors are not very sensitive, turn the speaker or phone volume up quite high. However, do not turn it up so much that it is uncomfortable or that you need to raise your voice to be understood by someone three feet away. Loud noise can damage hearing. If in doubt, students could wear hearing protection.

> **Note**
>
> In the programs provided for this activity, we assume the left microphone is plugged into `port 3` and the right microphone into `port 4`.

### Step 1: Measuring the directionality of the microphones

> **Note**
>
> If time is limited, Step 1 (measuring the robot's directionality without external ears) can be skipped. However, we still recommend discussing the lack of directionality of bare microphones so students understand why they need to add external ears to the robot.

If we want to find sound by comparing intensities at both receivers, the left microphone must be more sensitive than the right for sound coming from the left. However, this is not guaranteed. As previously discussed, the microphones are almost omnidirectional. Therefore, they pick up sound almost equally from all directions. A sound to the left of the robot may stimulate both microphones equally, leaving the robot unable to determine direction.

In this step, students measure the microphones' directionality. Provide the robot with two microphone sensors, mounted as shown below.

> **Note**
>
> If you mount the sound sensors as shown, do not overtighten the screws. This might damage the sensors.

![The two sound sensors mounted on the front of the robot, angled outwards so that each faces a different side.](images/robot-phonotaxis-5f001102.jpg)

![One of the sensors close up. The microphone is the small black disc; the rest of the board amplifies and filters its signal.](images/robot-phonotaxis-9b19fbad.jpg)

![The same sensor off the robot. Note that there is nothing to adjust on it: the board has no sensitivity control, so the two sensors on a robot cannot be matched by turning anything, which is why the calibration later in this chapter is done in software instead.](images/sound-sensor-photo.jpg)

Next, have students build a setup like the one shown below. Students can place a large sheet of paper or a whiteboard on the floor (as in the example) and draw several compass directions. In the example, angles from -40 to 40 degrees are drawn in 20-degree steps. Place the sound source at an angle of 0° and about 50 cm from the robot. The sound source can be a phone or a speaker.

![Measuring directionality. The robot sits at the centre of a protractor scale so it can be rotated to a known angle between readings.](images/robot-phonotaxis-748fdb0b.jpg)

Have the sound source play the following sound on repeat. The sound consists of bursts of white noise. [Temporal response of the Makeblock sound sensor](#temporal-response-of-the-makeblock-sound-sensor) explains why this sound is pulsed. Click the link below, then click the 3 dots in the sound player to download the file.

[Pulsed tone for the robot (.mp3)](files/pip_exported.mp3)

Students should align the robot with each marked direction. Run the program below. In the program, ensure the `set left_scale` block contains the value 1. You can change this number by clicking on the small oval containing the number.

![The `left_scale` block, which holds the correction factor. It starts at 1, meaning no correction.](images/robot-phonotaxis-35eb8c6f.png)

When they click the green flag, the robot will take 20 measurements of sound intensity from the left and right microphones, then calculate the average. The robot will beep when done. Once the robot beeps, students should record the `left_sound` and `right_sound` values.

Next, turn the robot to align it with the next direction and click the green button again to measure the next angle. This way, students determine the loudness of the sound as perceived by both microphones at different positions relative to the sound source.

> **Tip**
>
> If you use the program below, mBlock automatically loads an extension that allows you to work with the sound sensor. To start programming from scratch, you must add the extension yourself. Click the following link for instructions:
>
> [Adding the sound sensor extension](#adding-the-sound-sensor-extension)

### Step 2: Make the ears directional

Students can make the ears (microphones) directional by constructing artificial pinnae around the microphones. Students can use paper, modeling clay, or other materials. In the example below, we made external ears by rolling sheets of paper into cones. Notice the ears are quite large relative to the robot. Larger ears typically result in higher directionality. We also show images of a student's robot with external ears made from modeling clay.

![Paper cone ears, taped to the sensors and angled outwards.](images/robot-phonotaxis-3b931d59.jpg)

![A moulded pair, shaped to gather sound from one side and shield the other.](images/robot-phonotaxis-3c135ee9.jpg)

![Another design. What matters is not realism but that the two ears face away from each other.](images/robot-phonotaxis-5b1579be.jpg)

![Students take the brief further than strictly necessary, which is no bad thing.](images/robot-phonotaxis-caff0520.jpg)

Once students have created ears for their robots, have them repeat the measurements above. The graph should now show clear directionality. If not, they should keep working on the ears until they achieve directional sensitivity. Without directional ears, the robot cannot localize sound.

Below is an example of data collected with directional ears. These data show that the right ear picks up more sound when the source is to the robot's right (negative angles), and vice versa.

![The same measurement with ears fitted. The lines now separate and cross: each ear hears its own side more loudly, which is the difference the robot steers on.](images/robot-phonotaxis-f4124490.png){}

One problem that often occurs with students' external ears is that the amount of sound picked up by the left and right ears is not the same at zero degrees. In the example data, when the sound source is directly in front of the robot, the left ear picks up more sound than the right. The left ear appears more sensitive overall. This indicates the left ear is more sensitive than the right. At angle zero, the right value is about 70% of the left ear value:

$$
\frac{right ear value at zero degrees}{left ear value at zero degrees} \approx \frac{250}{340} \approx 0.7
$$

Student values will differ. Perhaps their right ear is more sensitive than the left. In this case, the equation above will return a value larger than 1.

You can correct for microphone sensitivity differences. The example program provides the `left_scale` block for this. Enter the result of the equation into that block to correct for differences. For the example above, enter 0.7.

![Setting the correction factor. Here the left microphone reads high, so `left_scale` is set below 1 to bring the two into agreement.](images/robot-phonotaxis-3f2fd20b.png){#fig:leftscale}

Students could rerun the measurements to check whether this correction results in the left and right ears picking up about the same amount of sound at zero degrees. Below is an example graph.

![After scaling. The two curves now cross close to zero degrees, so equal loudness means the sound really is straight ahead.](images/robot-phonotaxis-6f33c641.png)

Now, the left and right ear values are approximately equal at angle zero. Moreover, the left ear returns a higher value if the sound source is on the robot's left side (angle > 0). The right ear has a larger response when the sound source is on the robot's right side (angle < 0). These response curves enable phonotaxis.

### Step 3: Phonotaxis

Now have the robot follow a sound source. Students can run the example program. The robot should approach the sound source. They can try moving the sound source while the program runs to see if the robot notices the change.

[Open the mBlock project](https://planet.mblock.cc/project/3941523). If your school blocks the Makeblock site, [download `sound_localization_approach.mblock`](files/programs/sound_localization_approach.mblock) instead.

When running this program, enter the correction factor determined earlier in the same [`left_scale` block](#fig:leftscale) as before.

The example program does the following:

1. It takes 3 measurements of sound intensity at the left and right ears.
2. Depending on which ear receives the loudest sound, the robot turns slightly left or right.
3. Next, the robot drives a few cm forward. The cycle repeats.

This approach to sound localization results in a jittery path: the robot stops, measures, rotates, and moves. However, this approach gives the robot enough time to collect data. Moreover, many animals adopt the same stopping-moving strategy when approaching sound sources. Even humans "stop to listen" when looking for their ringing phone. Biology and engineering use similar strategies!
