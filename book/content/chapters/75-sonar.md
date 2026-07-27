# Sonar

## Materials
# Sonar

## Materials

| Item | Description |
| :--- | :--- |
| mBot Robot | The mBot robot. |
| Bluetooth Dongle | A dongle for connecting the robot to a computer. Currently the recommended connection method. |
| Makeblock Sonar sensor | The robot comes with one sonar sensor. Students need a second sonar sensor to complete the Sonar lesson. They can also use more than one sensor during the sonar cane activity. |
| 3D printed brackets | Brackets for mounting sensors on the front of the robot in different orientations. |
| PVC Pipe | PVC pipe used to make the sonar cane. Sold pipes are usually too long. They can be cut to about 6 ft. |
| Robot Pipe Plate | An acrylic plate that attaches to the PVC pipe using pipe brackets. The plate has holes for mounting the robot, used to mount the robot on the PVC pipe. |
| Pipe brackets | Brackets for mounting the plate to the PVC pipe. |
| Screws | The robot uses M4 machine screws. Provide extra screws for mounting additional sensors and the Robot Pipe Plate onto PVC pipe. |
| Extra motors | Motors occasionally fail. Provide replacement motors for students. |
| Extra cables (short) | Extra cables for connecting sensors. These allow students to add sensors without removing existing connections, preventing lost cables. Cables come in packs of 4; supply 1 extra per robot. Each is 20 cm long, matching the two cables included with the robot. |
| Extra cables (long) | Provide at least one long cable per group. This gives flexibility in mounting sensors on the sonar cane. Each cable is 2 ft long. |
| Lego compatible blocks | Blocks compatible with the robot's screw holes. These provide flexibility for mounting sensors as an alternative to provided brackets. |
| Gaffer's tape | Versatile tape useful throughout the activities. |
| Batteries | The robot requires 4 AA batteries. A 100-pack provides sufficient spares: with more than 8 batteries per robot, you can swap batteries without interrupting the curriculum. |
| Blindfolds | One per student. Used during the sonar cane activity. |
| Protractors | For measuring angles in one of the sonar robot activities. |

## Prerequisites

Student knowledge: High school Biology and Algebra 2 or equivalent.

## Investigating / Essential Questions

What limitations do human-made sensors have compared to the abilities of echolocating animals?

## Educational Standards

The educational standards applicable to this lesson are listed in the [Educational standards](#educational-standards) chapter.

## Learning Objectives

1. Understand the factors that determine the strength of an echo.
2. Identify the limitations of sonar sensors used in robots.
3. Learn how two sonar sensors can be used to avoid obstacles.
## Introduction

In this lesson, students explore echolocation. They learn about the differences between human-made devices and the abilities of echolocating animals. Students also explore how two sonar sensors can be used to avoid obstacles and build and analyze a sonar cane for a blind person.

Sonar sensors provide a relatively inexpensive and reliable way of detecting obstacles. Therefore, they are often used in cars (e.g., parking sensors), robots, and drones. Sonar sensors are also used as occupancy detectors. These sensors, typically mounted in ceilings or above light switches, detect movement in a room and switch on the lights. Maxbotix, a manufacturer of sonar sensors, provides a [web page listing many applications of their sensors](https://maxbotix.com/blogs/blog/ultrasonic-sensor-applications).

The applications above pertain to in-air sonar. However, sonar is also used extensively underwater. Because sound waves travel much further underwater, sonar has a much longer detection range underwater than in air. Fishermen use sonar to detect schools of fish. Submarines use large sonar sensors to detect obstacles and other submarines. Sonar is also used to [map the seafloor](https://oceanservice.noaa.gov/facts/sonar.html).

This lesson has two parts. In Part 1, students learn about sonar sensors, animal echolocation, and how we have tried to mimic animal abilities to improve human devices. After initial information from the instructor, students experiment with the robot using the sonar sensor to explore the sensor's directionality and the problem with sound mirrors.

During Part 2, students build a robot that uses two sensors to avoid obstacles, then design a sonar cane for a blind person that can detect obstacles above the sweep of the cane.

## Introduction to Sonar

This part of the lesson introduces sonar in technology and animals. You can begin by showing the three short video clips below. The sperm whale and bat videos introduce students to echolocation. We also include a video of a sonar-based parking sensor.

[Feeling the Force of Sperm Whales Ultrasound — BBC Earth](https://www.youtube.com/watch?v=tw7E7owEBm8)

[Bat echolocating and capturing moths](https://www.youtube.com/watch?v=MgRh_Q_xwys)

[A sonar parking sensor: Toyota's enhanced parking support](https://www.youtube.com/watch?v=BGd38676nF0)

### The principle of sonar

In principle, sonar is simple: a sound pulse is emitted, and the returned echoes are analyzed. Echolocating animals can derive several features from echoes. For example, insectivorous bats can infer information about the size or type of insect returning the echo. In contrast, human-made sonar sensors typically derive only one piece of information: the distance to the nearest obstacle. The time it takes for the first detected echo to return is used to calculate the distance to the object causing the echo. The link below explains how artificial sonar sensors work.

[How Ultrasonic Sensors Work](https://maxbotix.com/blogs/blog/how-ultrasonic-sensors-work)

Sonar as a distance sensor is widespread. For example, parking sensors on cars often use sonar. Many robots also use sonar to detect obstacles. Below is a picture of NAO, an advanced humanoid robot, which features four sonar sensors in the torso that help it avoid bumping into obstacles.

![The NAO robot is an advanced humanoid robot with four sonar sensors in its torso. These sensors help the robot avoid bumping into obstacles by detecting objects and calculating distance.](images/sonar-lesson-plan-d1293026.png)

The sonar sensor used by the mBot is a typical example of sonar as a distance sensor. The device looks like it has two sensors. However, the sensor consists of two transducers with different functions. One of the tin cylinders is the emitter (marked with a T), and the other is the receiver (marked with an R). The emitter produces ultrasound bursts, while the receiver is a microphone listening for the echoes.

![The mBot sonar sensor. One of the two cylinders is the emitter, while the other is the receiver.](images/sonar-lesson-plan-b7c001ad.png)

The sensor reports distance: it uses the time delay between the emitted sound and the returning echo to estimate the distance to the object. This is illustrated below. In this image, the same device is used as an emitter and receiver. Some sonar sensors can also use the emitter as a microphone. In our sensor, the emitter and receiver are separate.

![The principle. The sensor emits a pulse, the pulse reflects off an object, and the time until the reflection returns gives the distance.](images/sonar-lesson-plan-19f7e7c8.png)
### Animals that use sonar

#### Bats

Bats are divided into two main suborders: Microchiroptera (microbats) and Megachiroptera (megabats), with different echolocation abilities.

Most microbats are capable of echolocation. They emit ultrasonic sounds through their mouths or noses and use the returning echoes to navigate, locate prey, and avoid obstacles in the dark. Examples include the Little Brown Bat (*Myotis lucifugus*), Big Brown Bat (*Eptesicus fuscus*), and Mexican Free-tailed Bat (*Tadarida brasiliensis*).

Megabats, which include fruit bats and flying foxes, generally do not use echolocation to navigate or hunt. Instead, they rely primarily on their excellent eyesight and sense of smell. Megabats have large eyes and well-developed visual centers in their brains, which help them find food (fruits, nectar, or pollen) and navigate through forests or open spaces at night. Megabats include the Fruit Bat (Family Pteropodidae) and Flying Foxes (Genus *Pteropus*), predominantly found in tropical and subtropical regions of Africa, Asia, Australia, and the Pacific Islands.

![Microbats and megabats. Broadly, it is the microbats that echolocate; the fruit-eating megabats mostly navigate by sight and smell.](images/sonar-lesson-plan-c31a35a4.jpg)

#### Whales

Whales are divided into two main groups based on their echolocation abilities: toothed whales (odontocetes) and baleen whales (mysticetes).

Toothed whales, such as dolphins, porpoises, sperm whales, and orcas (killer whales), are known for their echolocation capabilities. They produce high-frequency clicks emitted through the forehead. These whales use echolocation for navigation and hunting prey such as fish and squid. Examples include: the Bottlenose Dolphin (*Tursiops truncatus*), the Sperm Whale (*Physeter macrocephalus*), the Orca (*Orcinus orca*), the Beluga Whale (*Delphinapterus leucas*), the Narwhal (*Monodon monoceros*), and porpoises (family Phocoenidae).

Baleen whales like humpback, blue, and fin whales do not echolocate.

![Toothed whales echolocate.](images/sonar-lesson-plan-76fb404b.jpg)

![Toothed whales produce sonar sounds using phonic lips in their heads. Bats produce sonar sounds using vocal cords, akin to how humans produce speech.](images/sonar-lesson-plan-8458aef6.png)

Besides bats and whales, several other animals use echolocation. Certain shrew species, such as the Eurasian water shrew (*Neomys fodiens*) and the American water shrew (*Sorex palustris*), emit ultrasonic calls to navigate and locate prey in dark or underwater environments. Oilbirds (*Steatornis caripensis*) are nocturnal birds found in Central and South America that navigate and locate food in dark caves using clicking or sonar-like vocalizations. Some swiftlets, such as the black-nest swiftlet (*Aerodramus maximus*), use echolocation to navigate within dark cave habitats by emitting calls and listening to echoes bouncing off cave walls.

Below are links with more information on echolocating birds and rodents, and a paper describing the differences and similarities of sonar in bats and whales.

[Echolocation in Oilbirds and swiftlets | *Frontiers in Physiology*](https://doi.org/10.3389/fphys.2013.00123)

[Functional Convergence in Bat and Toothed Whale Biosonars | *Physiology*](https://doi.org/10.1152/physiol.00008.2013)

[Echolocation in insectivores and rodents (.pdf)](files/Echolocation_in_Insectivores_and_Rodents.pdf)

#### Basic operation

The sound emitted by the sensor is ultrasonic. Many sonar sensors, including the mBot sensor, use pulses with a frequency of about 40 kHz — too high for humans to hear. However, many other species would have no problem detecting these pulses. For example, 40 kHz is at the higher end of a rat's hearing range. Echolocating bat species would have no problem, as many hear frequencies well over 100 kHz. Similarly, echolocating dolphins and whales should be able to hear the sonar sensor's emissions (if conducted to water).

Even though we cannot hear the sensor's emission without help, we can measure and visualize the output using ultrasonic microphones. Most microphones are sensitive to our hearing range (up to about 20 kHz). However, specialized devices exist for high-frequency recording.

Below, the sound waveform has been plotted as recorded by an ultrasonic microphone. This snippet is about 0.03 seconds (30 milliseconds) long. The sound burst at the left is the emission of the ultrasonic pulse. The bursts to the right are returning echoes. The sensor uses very short sound bursts — the emitted sound is about 1 ms long.

![About 30 milliseconds of sound recorded next to the sensor. The tall burst at the left is the emitted pulse, and the bursts to the right are returning echoes. The shaded region is the interval the sensor times: emission to first detected echo. The faint echoes inside it are too weak for the sensor to register.](images/sonar-lesson-plan-e223f011.png)

The mBot sensor, like many other sonar-based distance sensors, ignores all but the first echo. The pink-shaded interval is the time between the emission of the pulse and the reception of the first echo. Looking closely, you will see that some very weak echoes return before the indicated echo. But these are too weak for the sensor to detect. The sensor uses the time interval to the first detected echo to determine distance. In this case, the interval is about 0.0104 seconds (10.4 ms).

Assuming sound travels about 34 cm per millisecond, we can calculate the distance (d) from which the echo returned:

$$
d = \frac{34.3 \frac{cm}{ms} \times \text{delay}}{2} = \frac{34.3 \frac{cm}{ms} \times 10.4\ ms}{2} = 178.36\ cm
$$

Using a laser distance meter, the object returning the echo (in this case, a wall) was about 184 cm away from the sonar sensor. The calculation is close but not exact. One reason is that the speed of sound depends on temperature and humidity. The applet below lets you calculate a more precise speed of sound for different environmental conditions:

[Calculate speed of sound in humid air](https://sengpielaudio.com/calculator-airpressure.htm)

The value of 34.3 cm/millisecond for the speed of sound holds for temperatures around 20°C and 50% humidity. The speed of sound increases with temperature and humidity. Taking temperature and humidity measurements would allow a correction to the equation for more accurate results.

#### The sensor under-reports distance

The distance the sensor reports is not the distance calculated from the echo. It is consistently too small. In the measurement above, with the wall about 184 cm away, the sensor reported **142 cm**. This appears to be a quirk of the sensor rather than a fault in one unit. Checks at several distances found the error to be proportional — the reading is always short by roughly the same fraction, not by a fixed number of centimetres. This is why a single multiplier is the right way to correct it.

The programs in this lesson multiply the reported distance by **1.25** to compensate. It is worth understanding rather than taking on trust, because it does not quite reconcile:

| | Distance |
|---|---|
| Reported by the sensor | 142 cm |
| Sensor reading × 1.25 | 177.5 cm |
| Calculated from the echo delay | 178.4 cm |
| Measured with a laser distance meter | about 184 cm |

So × 1.25 brings the sensor into line with the time-of-flight calculation almost exactly, and still leaves it about 6 cm short of the laser measurement. Correcting all the way to 184 cm would take a factor of about 1.30. That remaining gap is small enough to come from the assumed speed of sound, or from the two instruments not measuring from quite the same point on the robot.

> **Note**
>
> Sensors differ, and mBlock is updated from time to time, so check your own rather than trusting ours. Put the robot a measured distance from a large flat wall, read what the sensor reports, and divide:
>
> **correction factor = true distance / reported distance**
>
> Do this at two or three distances, say half a metre, one metre and two metres. You should get roughly the same answer each time.
> If that answer is close to **1**, the under-reporting has been fixed in your version of mBlock and the correction is no longer needed — remove the multiplier, or the robot will think obstacles are further away than they are and leave everything too late. If it is close to **1.25**, our programs will work as they are. If it is something else, put your own number in place of 1.25, which appears in the `do_sensing` block of the obstacle avoidance program and near the top of the sonar cane program.

#### Directionality and Range
#### Directionality and Range

The sensor consists of an emitter and a receiver. The emitter does not emit sound equally in all directions — it has some directionality. It emits most strongly directly ahead and less strongly at larger angles from the central axis. Likewise, the receiver is not equally sensitive to all directions. It is most sensitive to echoes returning from straight ahead and less so for echoes returning at an angle. The result is that the whole sensor has some directionality.

The sensor's variable sensitivity as a function of angle means that the weakest echo it can detect depends on the angle from which the echo returns. Echo strength depends mostly on two factors: the distance from which it returns, and the object from which it returns. Echoes from further away are weaker. Echo strength also depends on the shape and material of the object. In general, smaller objects return weaker echoes.

The conclusion is that for a given target object, the sensor has a maximum range at which it can detect the echo. This range depends on the angle at which the object is placed with respect to the sensor.

To make this more tangible, consider the following graph from Maxbotix, a manufacturer of sonar sensors. This is not the sensor used in this lesson, but the example is illustrative.

![The region in which a Maxbotix sensor can detect a 10 cm wooden pole, each grid square being 30 cm. The sensor sits at the bottom, pointing up. Straight ahead it reaches about 240 cm; along the blue arrow, only about 20 degrees off axis, about 190 cm. The red dots are a different sensor setting and can be ignored.](images/sonar-lesson-plan-3ea35653.jpg)

Each grid square measures 30 × 30 cm. The sensor is at the bottom of the graph, pointing upwards. The black line shows the area where the sensor can detect a 10 cm diameter wooden pole. The red dots show the same for another sensor setting (which can be ignored). In this case, the pole can be detected at a maximum range of 240 cm (8 squares × 30 cm) straight ahead.

In contrast, in the direction of the blue arrow (about 20 degrees off axis), the maximum detection distance is about 190 cm — 50 cm (20%) less at an angle of only 20 degrees from the centerline. At 30 degrees, the detection distance is only about 120 cm (50% reduction).

This shows that the Maxbotix sensor is very directional: detection distances fall rapidly as the angle from the centerline increases. The same holds for our mBot sensor. Makeblock specifies a detection range of 3 to 400 cm for this sensor. However, the upper figure is theoretical: it assumes a very large object straight ahead. In practice the range is substantially smaller, especially for smaller objects. There is also a lower limit — objects closer than about 3 cm cannot be detected at all.

Students will explore the directionality and the problem with sound mirrors in the following activities.

### The mBot sensor compared to animal sonar

Here, we relate the above concepts to animal sonar, enabling students to see parallels and differences between artificial sonar systems and biological echolocators.

Above, we learned that the mBot sonar sensor emits sound pulses of about 40 kHz. Many echolocating bats use calls with a broad frequency range. Below is a recording of the big brown bat, from the U.S. National Park Service website. This plot is a spectrogram, showing the frequencies in the bat's calls as a function of time. This spectrogram shows that this bat's call contains frequencies between about 60 and 25 kHz. You can play a slowed-down version of the sound recording on the U.S. National Park Service website. By slowing down the recording, the sound becomes audible to humans. When you listen, you will notice that this bat's calls sound like 'chirps' — indeed, bat calls are often called chirps, as this is what they sound like on slowed-down recordings.

![A big brown bat's calls, recorded by the U.S. National Park Service. Each stroke is one call, sweeping downwards from about 60 kHz to about 25 kHz. The calls come closer together towards the right as the bat closes on a target.](images/sonar-lesson-plan-bcb99b25.png)

[Echolocation - Bats (U.S. National Park Service)](https://www.nps.gov/subjects/bats/echolocation.htm)

Echolocating whales and dolphins' calls typically contain an even broader range of frequencies than bats' calls. Below is the spectrogram of dolphin sonar sounds. The sounds contain frequencies from 0 to 150 kHz (the highest frequency measured).

![A spectrogram of eight echolocation clicks from a dolphin, about 40 milliseconds apart. Each click is the narrow vertical stripe, and it spans the whole height of the plot: a single click contains everything from the lowest frequencies shown up to about 150 kHz. Compare this with the bat call above, and with the sensor's single frequency of 40 kHz. Source: [Acoustical Society of America](https://acoustics.org/pressroom/httpdocs/163rd/Mishima_2aAO5.html).](images/sonar-lesson-plan-342a9881.jpg)

> **Tip**
>
> In summary, a key difference between animal echolocators and artificial sonar is that animals typically use sounds with a broad spectrum (a broad range of frequencies). This has several advantages but is difficult to reproduce in artificial sonar. Therefore, artificial sonar most often uses sound with a narrow spectrum (a very limited range of frequencies).

Above, we discussed that artificial sonar sensors are directional: they are more sensitive in some directions than others. Animal sonar systems are also directional. Below is an image showing a top view of the emission directionality of a bat and a dolphin. These images show the "loudness" of their calls in each direction. Straight ahead of the animal, the calls are the loudest. Left and right, the call is quieter. In addition, the animals' hearing is also directional. They are more sensitive to echoes coming from straight ahead and less to peripheral echoes.

![Emission directionality of a bat and a dolphin, seen from above. The calls are loudest straight ahead and fall away to the sides, just as the mBot's sensor does. From Madsen, P. T. & Surlykke, A. (2013), *Functional Convergence in Bat and Toothed Whale Biosonars*, Physiology 28, 276-283.](images/sonar-lesson-plan-c01f834f.png)

> **Tip**
>
> In summary, just like the mBot sonar, animal sonar is directional. Animals can detect small objects more readily straight ahead than from the side.

The next two activities let students find these limits for themselves. Both are optional and can be skipped if time is short.
## Activity 1: Measuring the sonar's directivity

In this activity, students create a graph (on the floor) to understand what a single sonar sensor can be expected to detect.

> **Tip**
>
> For this activity, plug the sonar sensor into port 1. The robot should be equipped with only one sonar sensor for this activity (see image below).

![For this activity, the robot should be equipped with a single sonar sensor (this is the default configuration of the robot). **In this stock image, the sonar is plugged into port 2 but we use port 1 for this activity.**](images/activity-1-measuring-the-sonars-directivity-60d0fadf.jpg)

Open the Sonar Directionality Program in mBlock 5 from the link below and connect to your robot using the dongle connection. [See here for instructions](#getting-started-with-the-robot) on how to connect to the robot.

[Open the mBlock project](https://planet.mblock.cc/project/3916152). If your school blocks the Makeblock site, [download `sonar_directionality.mblock`](files/programs/sonar_directionality.mblock) instead.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
> You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to my computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#step-1-open-the-example-program) for an example and more instructions.

The program is straightforward: it continuously measures the distance from the sonar and checks whether the returned value is smaller than 400 cm. If nothing is detected, the sensor returns a value of 400 cm. If the sensor detects something, the green LEDs on the robot switch on. If nothing is detected, the red LEDs switch on. Therefore, the robot's color indicates whether the sonar picks up an echo.

To measure the region in which the robot can detect an obstacle, place the robot in a large open space (see image below). Next, move an obstacle in front of the robot (in this case, a black pole) to find the largest distance at which the object is detected (the robot turns green) for several directions. While doing this, ensure the robot is not picking up echoes from your body. Your body will likely be a larger object than the one used to assess the sonar's reach.

![The setup. The robot is at the bottom, the black pole is the target, and the white straws mark the positions where the robot could just detect it.](images/activity-1-measuring-the-sonars-directivity-d833df5e.jpg)

In trials for this lesson, a black plastic tube pole was used as the obstacle, and straws (or tape) were placed on the floor, connecting the positions at which the robot could detect it. For every position in the area delineated by the straws, the robot could detect the tube pole (the robot turned green). Moving the tube pole outside this area turned the robot red.

You could repeat the measurements with different objects and compare the resulting patterns.

### Questions

- What is your robot's maximum detection distance?
- Is the sensor's directionality symmetric?

## Activity 2: Acoustic mirrors

The previous activity revealed that the sonar sensor's range is limited. To use the sonar effectively, especially indoors, we must understand a second limitation. In contrast to natural environments, indoor environments contain many smooth surfaces, which can be a problem for sonar. If the sonar pulse strikes a smooth surface at an angle, much of the sound is reflected away from the receiver rather than toward it. This might result in the sonar sensor not detecting large smooth surfaces. This is called the acoustic mirror effect.

This effect can be observed by pointing the robot at a smooth surface (like a wall) while the program from [Activity 1](#activity-1-measuring-the-sonars-directivity) is running:

[Open the mBlock project](https://planet.mblock.cc/project/3916152). If your school blocks the Makeblock site, [download `sonar_directionality.mblock`](files/programs/sonar_directionality.mblock) instead.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
> You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to my computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#step-1-open-the-example-program) for an example and more instructions.

- Point the robot straight at the wall from about 30 cm. Can the robot detect the wall?
- Now, point the robot at the wall at an angle of about 45 degrees. Is the robot still able to detect the wall? Experiment with different angles to see how well the robot can detect the wall from an angle.
- This acoustic mirror effect might be essential to understanding the robot's behavior in upcoming activities. If your robot keeps colliding with large, smooth objects or surfaces, it might be suffering from this acoustic mirror problem. What solutions can you devise to avoid this issue?

![Left: the robot is pointed straight at a smooth, flat wall. The sonar sensor has no problem detecting the wall and turns green. Right: The robot is pointed at the wall from an angle. Due to the acoustic mirror effect, the robot does not detect the wall.](images/activity-2-acoustic-mirrors-3936ab65.png)
## Part 2: Programming and building

The two activities that follow are the challenges of this lesson. In the first, students program a robot with two sonar sensors to avoid obstacles. In the second, they design, program, and test a sonar cane to support a visually impaired user.

## Activity 3: Robot obstacle avoidance

### Preparing the robot

In this activity, students build a robot that uses two sonar sensors to avoid obstacles. Students will need to attach the two sensors to the robot.

> **Tip**
>
> Ask students for thoughts about how two sensors might be helpful.
>
> A single sonar sensor gives the distance to the nearest detected obstacle. However, this yields little information about the obstacle's position. All we know is that an obstacle is somewhere in front of the robot. Using two sensors, the distances they return can be compared. If the distance from the left sonar sensor is lower, we can assume the obstacle is more to the robot's left. Or perhaps there is an obstacle at the left that the right sensor cannot detect (meaning that obstacle is either further away or smaller). In either case, turning right to avoid this obstacle makes sense. Having two sensors makes it possible to decide whether to turn left or right.

The [Thingiverse](https://www.thingiverse.com/dvanderelst/designs) page provides several brackets that can be 3D printed to facilitate mounting two sensors on the robots (two versions are used in the image below). Alternatively, the spacing of the holes on the robot is compatible with Lego Technic. In the past, we have provided students with Lego and asked them to be creative about mounting the robot's sensors.

![The red brackets were 3D printed. The STL files accompanying these lesson plans are available on the Thingiverse page.](images/robot-obstacle-avoidance-a3f214cb.jpg)

![Two sonar sensors on 3D-printed brackets, angled apart so each covers its own side.](images/robot-obstacle-avoidance-519ceb09.jpg)

### Programming the robot

Students could be asked to design a program for the robot that allows it to avoid obstacles using the sonar sensors. Below, we discuss the linked example program. This program assumes the left sonar sensor is connected to port 1 and the right sensor to port 2. A screenshot of the program appears below.

[Open the mBlock project](https://planet.mblock.cc/project/3916162). If your school blocks the Makeblock site, [download `sonar_obstacle_avoidance.mblock`](files/programs/sonar_obstacle_avoidance.mblock) instead.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
> You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to my computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#step-1-open-the-example-program) for an example and more instructions.

The main program loop is shown first. It goes through the same steps continuously: it queries the sensors; if the left sonar reports the smaller distance (`min_side = left`) the robot turns **right**, away from the obstacle, and keeps turning until the left sonar reports a distance greater than the safe distance. If the right sonar reports the smaller distance it turns left in the same way. Between turns it drives forward — at half power when the nearest obstacle is more than 100 cm away, and at quarter power when it is closer, so it has more time to sense as it approaches something.

![The main loop. `do_sensing` reads both sensors; if the nearer obstacle is on the left the robot turns right, and the other way round; otherwise it drives on, more slowly when something is within a metre.](images/robot-obstacle-avoidance-18f6461b.png)

The safe distance is defined at the start of the program. Here, it is set to 30 cm. The result is that the robot turns left or right (on the spot) if one of the sensors returns a distance smaller than the safe distance, and keeps turning until that sensor returns a large enough value.

Let us break down the program into simpler terms:

1. `do_sensing`: This block collects data from both sonar sensors. It measures the distances to obstacles on the left and right sides of the robot. It also multiplies both values by 1.25, for the reason given in [The sensor under-reports distance](#the-sensor-under-reports-distance).
2. `min_distance`: This variable stores the smaller of the two distances measured. It tells us how close the nearest obstacle is, regardless of which side it is on.
3. `min_side`: This variable tracks which sensor (left or right) detected the closest obstacle. It is crucial for deciding which way the robot should turn to avoid the obstacle.

Here is how these elements work together:

- The robot constantly checks both sensors using `do_sensing`.
- It compares the distances and updates `min_distance` and `min_side`.
- If `min_distance` is less than the safe distance, the robot must turn.
- The `min_side` then determines which way to turn: if it is "left," the robot turns right to avoid the obstacle, and vice versa.

The red blocks in the program above are defined in the image below.

![The blocks the main loop calls. `do_sensing` reads both sensors and applies the correction factor; `get_min_distance` and `get_min_side` work out how near the closest obstacle is and which side it is on; `turn_left` and `turn_right` turn in short bursts, re-sensing between each, until that side is clear.](images/robot-obstacle-avoidance-57525850.png)

### Running the program

When students run the program, the robot should move forward as long as it is far from obstacles. It should turn on the spot when close to them. Depending on where the robot is tested, students might notice that the robot seems blind to some obstacles. This happens when the obstacles have a small surface area. These return weak echoes and might go undetected. They might also see the mirror effect coming into play. When approaching a smooth wall or other surfaces at an oblique angle, the robot happily drives into the obstacle as no strong echoes return.

Therefore, it might be worthwhile to construct an arena for the robot populated with obstacles the sensors should be able to detect. A circular arena of children's toys has been built in the example below. These objects consist of multiple surfaces oriented in many different directions, making them very likely to return echoes the robot can pick up.

Plastic drinking cups could also be used to build an arena. If drinking cups are used, ensure they are tall enough to reach the level of the robot's sensors. Otherwise, the sonar sensor might literally overlook the cups.

The acoustic complexity of the toy arena can be appreciated by looking at a recording of the echoes received by the robot. For this, an ultrasonic recorder was placed on top of the robot to record emissions and echoes. This procedure is also used by scientists who study bats: by placing a mini recorder on a bat's back, they learn what echoes the bat perceives. The recording shows that the first echo returns from a distance of about 30 cm. However, many other echoes can be seen as well. This shows that the toys return many echoes, increasing the chance one will be picked up by the robot.

![Here, the robot is tested in an arena consisting of several toys. These complex objects (as opposed to flat walls) are guaranteed to return strong echoes to the robot.](images/robot-obstacle-avoidance-3237775a.jpg)

![One recorded echo as perceived by the robot. The marked part is the robot's emission. The remainder of the signal consists of echoes returned from the many surfaces in the arena depicted on the left.](images/robot-obstacle-avoidance-6a79cb0c.png)

## Activity 4: Building a sonar cane

Several inventors and companies have designed sonar-enabled canes for visually impaired people. The general idea is to use a sonar sensor (or multiple sensors) to detect obstacles in the user's path. The distance picked up by the sensors is then conveyed to the user through non-visual cues.

> **Tip**
>
> Show students the YouTube video below describing such a device. Using the robot, students will build a device that does something similar: one or two sensors to detect obstacles, and the robot's speaker to convey what they find to a blindfolded user.
>
> [Video: a sonar cane for visually impaired users](https://www.youtube.com/watch?v=cnW1_XMUIzM)

In this activity, students build a device that does something similar: use one or two sonar sensors to detect obstacles and use the speaker on the robot to convey this information to a (blindfolded) user. The sonar device should detect obstacles missed by the cane (the user employs their cane to probe for obstacles on the floor while the sonar looks horizontally for overhanging obstacles).

![The idea. The cane sweeps the floor while the sonar, mounted higher up, looks ahead for obstacles at head and chest height that the cane would miss.](images/sonar-cane-6beb49f4.png)

### Mounting the robot on the PVC pipe

Students will mount the robot on a 1/2-inch PVC pipe for this activity. They can mount one or more sonar sensors anywhere on the PVC pipe using 3D-printed brackets, Lego-compatible blocks, or other materials. Here, we explain how to mount the robot on the PVC pipe using a mounting plate.

#### Step 1

Remove the caster wheel from the front of the robot.

![The caster wheel removed from the front of the robot, with the two screws that held it.](images/step-1-b0e9918f.jpg)

#### Step 2

Mount the platform on the PVC pipe using two screws and a 1/2 inch pipe bracket. It is important to mount the platform with the broad side to the side of the pipe that will be used as the top of the sonar cane.

![The mounting plate fixed to the pipe. The broad end must point towards the top of the cane, as marked.](images/step-2-f2db380c.jpg)

#### Step 3

Use at least two screws to fix the robot to the platform. You can use the screws from the caster or any M4 machine screw.

![The robot screwed onto the platform.](images/step-3-a36ea32a.jpg)

![The same join seen from the other side.](images/step-3-dffc78d1.jpg)

#### Step 4

Add more screws using the holes pointed out in the image below.

![The additional holes used to add further screws.](images/step-4-2686475f.jpg)

#### End result

### Example Program

We provide an example program. The program is linked and displayed below.

> **Note**
>
> The example program below assumes one sonar sensor is being used. However, students can use more than one sensor.

[Open the mBlock project](https://planet.mblock.cc/project/3916250). If your school blocks the Makeblock site, [download `sonar_cane.mblock`](files/programs/sonar_cane.mblock) instead.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
> You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to my computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#step-1-open-the-example-program) for an example and more instructions.

The program continuously measures the distance recorded by a sonar sensor, [applies the correction factor](#the-sensor-under-reports-distance), and converts the measurement from cm to meters.

![The cane program. The distance is read, corrected, and converted to metres; the `beep` block turns it into a beep whose length grows as the obstacle gets closer, and runs the motors briefly at close range so the user feels it as well as hears it.](images/sonar-cane-894677a6.png)

The distance (variable `distance`) is then used to set the duration of a beep. Smaller distances result in longer beeps, while larger distances result in shorter beeps. In equation form, the value `b` (in seconds) is determined as follows:

$$
\begin{aligned}
b &= 0.49 - 0.4 \times \text{distance} \\
b &= \\n\begin{cases}
0, & \text{if } b < 0 \\
0.25, & \text{if } b > 0.25 \\
b, & \text{otherwise}
\end{cases}
\end{aligned}
$$

The relationship between the distance `d` and the duration of the beep `b` is visualized in the following plot. The values `0.49` and `0.4` determine the slope of the line for intermediate distances. When the distance is over about 1.2 meters, the duration of the beep is zero, and the robot will not beep at all. For distances below 0.6 meters, the duration of the beep is maximal (0.25 seconds). At these short distances, the motors are also turned on for 0.25 seconds to give the user some vibrational feedback.

The relationship between the distance `d` and the duration of the beep `b` is visualized in the following plot. The values `0.49` and `0.4` determine the slope of the line for intermediate distances. When the distance is over about 1.2 meters, the duration of the beep is zero, and the robot will not beep at all. For distances below 0.6 meters, the duration of the beep is maximal (0.25 seconds). At these short distances, the motors are also turned on for 0.25 seconds to give the user some vibrational feedback.

The relationship between the distance `d` and the duration of the beep `b` is visualized in the following plot. The values `0.49` and `0.4` determine the slope of the line for intermediate distances. When the distance is over about 1.2 meters, the duration of the beep is zero, and the robot will not beep at all. For distances below 0.6 meters, the duration of the beep is maximal (0.25 seconds). At these short distances, the motors are also turned on for 0.25 seconds to give the user some vibrational feedback.

![Beep length against distance. Beyond about 1.2 m there is no beep at all; below 0.6 m the beep is at its longest, a quarter of a second.](images/sonar-cane-b9caef3a.png)

### Testing the program

The sonar device was designed to detect obstacles missed by the cane sweeping the floor. Therefore, test the sonar cane with overhanging obstacles. For example, have students hold out pieces of cardboard or other objects in the path of a blindfolded student testing the cane. The blindfolded student should use the physical cane to sweep their path for obstacles on the floor. The sonar should inform them of upcoming overhanging obstacles.

It is worthwhile for students to take time to practice using the sonar cane. Afterward, they can reflect on the system's benefits and drawbacks. Have them think critically about the potential benefits of sonar-based systems for visually impaired people. What are the drawbacks? What improvements can they conceive?

The images below show students using a sonar cane to avoid obstacles. Note that these students use a different robot and have mounted the robot differently than explained above.

![A blindfolded student navigating a corridor with the cane, with an obstacle placed in the path.](images/sonar-cane-630a642a.jpg)

![The sonar is mounted low on this cane. Where it points decides which obstacles it finds.](images/sonar-cane-ff190d27.jpg)

![Testing against a bench, the kind of overhanging obstacle a cane sweeping the floor would miss.](images/sonar-cane-7bef03ce.jpg)

![Obstacles marked out with tape. The rest of the group watches and records what happens.](images/sonar-cane-314965f7.jpg)

![Several canes in use at once. These students mounted the robot differently from the method described above.](images/sonar-cane-935870be.jpg)

![Another group's design, tested along the same corridor.](images/sonar-cane-b5d37240.jpg)
