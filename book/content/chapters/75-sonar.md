# Sonar


## Materials

| Item | Description |
| :--- | :--- |
| mBot Robot | The mBot robot |
| Bluetooth Dongle | This is a dongle that allows to connect to the robot from a computer. This is currently the recommended way to work with the robot. |
| Makeblock Sonar sensor | The robot comes with one sonar sensor. However, students will need a second sonar sensor to complete the Sonar lesson plan. They can also use more than 1 sensor during the sonar cane activity. |
| 3D printed brackets | These are brackets that allow sensors to be mounted on the front of the robot, in different orientations. |
| PVC Pipe | This is the pvc pipe used to make the sonar cane. The pipes sold are usually too long. They can be cut to about 6 ft. |
| Robot Pipe Plate | This is an acrylic plat that can be attached to the pvc pipe using pipe brackets. The plate also has holes to mount the robot. Hence, this plate is used to mount the robot on the PVC pipe. |
| Pipe brackets | These brackets are used to mount the plate to the pvc pipe |
| Screws | The robot use M4 machine screws. Students should be supplied with an ample supply of extra screws allowing to mount extra sensors. These screws are also used to mount the Robot Pipe Plate onto the PVC pipe. |
| Extra motors | Motors seem to be a component that fails from time to time. Students should be provided with replacement motors |
| Extra cables (short) | Extra cables for connecting sensors. This allows students to add sensors without removing cables and covers for losing cables.  The cables come in a pack of 4. I suggest supplying 1 extra cable per robot.  This cable is 20 cm long and has the same length as the 2 cables that come with the robot. |
| Extra cables (long) | We should provide students with a least one long cable. This will provide them with freedom in mounting their sensors on the sonar cane.  This cable is 2 ft long. |
| Lego compatible blocks | These blocks are compatible with the screws and the hole spacing used by the robot. Therefore these blocks allow students freedom in mounting sensors (as an alternative to the brackets we provide) |
| Gaffers tape | It’s tape. What else can I say. I comes in handy everywhere. |
| Batteries | The robot takes 4 AA batteries. These should last a while. This is a 100 pack of AA batteries Providing more than 8 batteries per robot should allow swapping out the batteries and getting new stock without interruption to the curriculum. |
| Blindfolds | We need 1 per student. These are used during the sonar cane activity. |
| Protractors | Allows for measuring angles for one of the sonar robot activities |

## Prerequisites

Student knowledge: High school Biology and Algebra 2 or equivalent.

## Investigating / Essential Questions

What limitations do human-made sensors have compared to the ability of
echolocating animals?

## Educational Standards

The educational standards applicable to this lesson are listed in the [Educational standards](#educational-standards) chapter.

## Learning Objectives

1. Students will understand the factors that determine the strength of an echo.
2. Students will identify the limitations of sonar sensors used in robots.
3. Students will learn how two sonar sensors can be used to avoid obstacles.
4. Students will build and analyze the functionality of a sonar cane.
5. Students will learn about how echolocation in animals works.
6. Students will learn about the limits and advantages of echolocation in animals.

## Introduction

In this lesson, students explore echolocation. They will learn about the differences between our human-made devices and the abilities of echolocating animals. Students will also explore how two sonar sensors can be used to avoid obstacles and build and analyze a sonar cane for a blind person.

Sonar sensors provide a relatively cheap and reliable way of detecting obstacles. Therefore, they are often used in cars (for example, parking sensors), robots, and drones. Sonar sensors are also used as occupancy detectors. These sensors (typically mounted in the ceiling or above a light switch) detect movement in a room and switch on the lights. Maxbotix is a manufacturer of sonar sensors. They provide a [web page that lists the many applications of their sensors](https://maxbotix.com/blogs/blog/ultrasonic-sensor-applications).

The applications discussed in the previous paragraph pertain to so-called in-air sonar. However, sonar is also used extensively underwater. Because sound waves travel much further underwater, sonar has a much longer detection range underwater than in the air. Fishermen use sonar to detect schools of fish. Submarines use (huge!) sonar sensors to detect obstacles and other submarines (google “submarine sonar dome” for images). [Sonar is also used to map the seafloor](https://oceanservice.noaa.gov/facts/sonar.html).

This lesson has two parts. In the first part, students will learn about sonar sensors, the sonar that animals use, and how we have tried to mimic that to improve devices in our world. After some initial information about the sensor from the instructor, students will experiment with the robot using the sonar sensor to explore the sensor's directionality and the problem with ‘sound mirrors’.

Sound mirrors, in the context of sonar, refer to surfaces that strongly reflect sound waves. These can be flat or curved surfaces that redirect sound in a specific direction, similar to how optical mirrors reflect light. In sonar applications, sound mirrors can cause unexpected echoes or create "blind spots" where objects are difficult to detect. Common examples of sound mirrors include flat walls, corners, or curved surfaces that can focus sound waves. Understanding how sound mirrors affect sonar readings is crucial for accurately interpreting sensor data and avoiding potential errors in obstacle detection.

During part two of the lesson, students will build a robot that uses two sensors to avoid obstacles and then design a sonar cane for a blind person that can detect obstacles above the sweep of the cane.

## Introduction to Sonar

This part of the lesson plan introduces sonar in technology and animals. You can begin the lesson by showing the four short video clips below. The videos of sperm whales and bats below will introduce students to echolocation. We also include a video of a sonar-based parking sensor.

[https://www.youtube.com/watch?v=tw7E7owEBm8](https://www.youtube.com/watch?v=tw7E7owEBm8)

[https://www.youtube.com/watch?v=MgRh_Q_xwys](https://www.youtube.com/watch?v=MgRh_Q_xwys)

[https://www.youtube.com/watch?v=BGd38676nF0](https://www.youtube.com/watch?v=BGd38676nF0)

### The principle of sonar

In principle, sonar is simple: a sound pulse is emitted, and the returned echoes are analyzed. Echolocating animals can derive several features from echoes. For example, it is assumed that insectivorous echolocating bats can infer information about the size or type of insect returning the echo. In contrast, human-made sonar sensors typically only derive one piece of information from the echoes: the distance to the nearest obstacle. The time it took for the first (detected) echo to return is used to calculate the distance to the object causing the echo. The link below takes you to the webpage of a manufacturer of sonar sensors explaining how artificial sonar sensors work.

[How Ultrasonic Sensors Work](https://maxbotix.com/blogs/blog/how-ultrasonic-sensors-work)

The use of sonar as a distance sensor is widespread. For example, parking sensors on cars often use sonars. Many robots also use sonar to detect obstacles in their path. Below, a picture of NAO, an advanced humanoid robot, has been included. This robot features four sonar sensors in the torso that help it avoid bumping into obstacles.

![The NAO robot is an advanced humanoid robot with four sonar sensors in its torso. These sensors play a crucial role in helping the robot avoid bumping into obstacles. Using sonar enables the robot to detect the presence of objects in its path and calculate the distance to them, thus preventing potential collisions.](images/sonar-lesson-plan-d1293026.png)

The sonar sensor used by the mBot is a typical example of sonar as a distance sensor. The device looks like it has two sensors. However, the sensor consists of two transducers with different functions. One of the tin cylinders is the emitter (marked with a T), and the other is the receiver (marked with an R). The emitter produces ultrasound sound bursts, while the receiver is a microphone listening for the echoes.

![The mBot sonar sensor. One of the two cylinders is the emitter, while the other is the receiver.](images/sonar-lesson-plan-b7c001ad.png)

The sensor reports distance: It uses the time delay between the emitted sound and the returning echo to estimate the distance to the object from which the sound is reflected. This is illustrated below. In this image, the same device is used as an emitter and receiver. Some sonar sensors can also use the emitter as a microphone. As said, the emitter and receiver are separated in our sensor.

![](images/sonar-lesson-plan-19f7e7c8.png)

### Animals that use sonar

#### Bats

Bats are divided into two main suborders: Microchiroptera (microbats) and Megachiroptera (megabats), and their echolocation abilities vary between these groups.

Most bats belonging to the suborder Microchiroptera are capable of echolocation. Microbats emit ultrasonic sounds through their mouths or noses and use the returning echoes to navigate, locate prey, and avoid obstacles in the dark. Examples of microbats that echolocate include common species like the Little Brown Bat (Myotis lucifugus), Big Brown Bat (Eptesicus fuscus), Mexican Free-tailed Bat (Tadarida brasiliensis), and many others found across different regions worldwide.

Megabats, which include fruit bats and flying foxes, generally do not use echolocation to navigate or hunt for food. Instead, they rely primarily on their excellent eyesight and sense of smell.

Megabats have large eyes and well-developed visual centers in their brains, which help them find food (fruits, nectar, or pollen) and navigate through forests or open spaces during nighttime.
Megabats include the Fruit Bat (Family Pteropodidae) and Flying Foxes (Genus Pteropus), predominantly found in tropical and subtropical regions of Africa, Asia, Australia, and the Pacific Islands.

![](images/sonar-lesson-plan-c31a35a4.jpg)

#### Whales

Whales are divided into two main groups based on their echolocation abilities: toothed whales (odontocetes) and baleen whales (mysticetes).

Toothed whales, such as dolphins, porpoises, sperm whales, and orcas (killer whales), are known for their echolocation capabilities. They produce high-frequency clicks or sounds that are emitted through the forehead. These whales use echolocation for various purposes, including navigation and hunting prey (such as fish and squid). Examples of toothed whales that echolocate include: the Bottlenose Dolphin (Tursiops truncates), the Sperm Whale (Physeter macrocephalus), the Orca (Orcinus orca), the Beluga Whale (Delphinapterus leucas), the Narwhal (Monodon monoceros), and porpoises (family Phocoenidae)

Baleen whales like humpback, blue, and fin whales do not echolocate.

![Toothed whales echolocate.](images/sonar-lesson-plan-76fb404b.jpg)

![Toothed whales produce sonar sounds using phonic lips in their heads. Bats produce sonar sounds using vocal cords, akin to how humans produce speech.](images/sonar-lesson-plan-8458aef6.png)

Besides bats and whales, several other animals across different taxa use echolocation. Certain species of shrews, such as the Eurasian water shrew (Neomys fodiens) and the American water shrew (Sorex palustris), are known to use echolocation. These small mammals emit ultrasonic calls to navigate and locate prey in dark or underwater environments. Oilbirds (Steatornis caripensis) are nocturnal birds found in Central and South America. They navigate and locate food in dark caves using a form of echolocation called 'clicking' or 'sonar-like vocalization'. Some species of swiftlets, such as the black-nest swiftlet (Aerodramus maximus), use echolocation to navigate within their dark cave habitats. They emit calls and listen to the echoes bouncing off cave walls to orient themselves.  

Below, we provide two links providing information on echolocating birds and rodents. We also link to a paper describing the differences and similarities of sonar in bats and whales.  

[Frontiers | Echolocation in Oilbirds and swiftlets](https://doi.org/10.3389/fphys.2013.00123)

[Functional Convergence in Bat and Toothed Whale Biosonars | Physiology](https://doi.org/10.1152/physiol.00008.2013)

[Echolocation_in_Insectivores_and_Rodents.pdf](files/Echolocation_in_Insectivores_and_Rodents.pdf)

## Part 1: Understanding sonar

### The mBot sonar sensor

#### Basic operation

The sound emitted by the sensor is ultrasonic. Many sonar sensors, including the mBot sensor, use pulses with a frequency of about 40 kHz. This frequency is too high for us to hear. However, many other species of animals would have no problem detecting the emitted pulses. For example, 40 kHz is at the higher end of the rat’s hearing range. And echolocating species of bats would have no problem detecting this sound as many hear frequencies well over 100 kHz. Similarly, echolocating dolphins and whales should be able to hear the emissions of the sonar sensor (if we find a way to conduct the sound to the water).

Even though we can’t hear the emission of the sonar sensor without help, we can measure and visualize the output using ultrasonic microphones. Most microphones are sensitive to our hearing range (up to about 20 kHz). However, specially manufactured devices exist that allow high-frequency recording of sound.

Below, the sound (waveform) has been plotted as recorded by an ultrasonic microphone. This snippet is about 0.03 seconds (or 30 milliseconds) long. The sound burst at the left side of the graph is the emission of the ultrasonic pulse. The sound bursts at the right of this are returning echoes. It should be noted that the sensor uses very short sound bursts. The emitted sound is about 1 ms (millisecond) long.

![](images/sonar-lesson-plan-e223f011.png)

The mBot sensor, like many other sonar-based distance sensors, ignores all but the first echo. The interval shaded in pink is the time between the emission of the pulse and the reception of the first echo. Looking closely, you will see that some very weak echoes return before the indicated echo. But these are too weak for the sensor to detect. The sensor uses the time interval to the first detected echo to determine the distance to an object. In this case, the interval is about 0.0104 seconds (or 10.4 ms).

Assuming that sound travels about 34 cm per millisecond, we can work out the distance (d) from which the echo returned using the following formula:

$$
d = \frac{34.3 \frac{cm}{ms} \times delay}{2} = \frac{34.3 \frac{cm}{ms} \times 10.4\ ms}{2} = 178.36\ cm
$$

Using a laser distance meter, the object returning the echo (in this case, a wall) was found to be about 185 cm away from the sonar sensor. Therefore, the calculation is close but not entirely exact. One reason for this is that the speed of sound (sound travel) depends on temperature and humidity. The applet linked below lets you calculate a more precise speed of sound for different environmental conditions:

[Calculation speed of sound in humid air and the air pressure humidity moist air water vapor density of water atmospheric pressure - sengpielaudio Sengpiel Berlin](https://sengpielaudio.com/calculator-airpressure.htm)

The value of 34.3 cm/millisecond for the speed of sound only holds for temperatures around 20 degrees Celsius and 50% humidity. The speed of sound increases with temperature and humidity. Taking temperature and humidity measurements would have allowed a correction to the equation above and a more accurate result.

> **Tip**
>
> **Cautionary Note:** In the previous section, it was shown how the sensor derives a distance measure from the delay of the echo. However, it turns out that the distance returned by the robot is biased: it consistently underestimates the distance. For the example given in the previous section, using a real distance of 184 cm, the robot reported a distance of 142 cm. An internet search indicated this might be a problem with the sensor's hardware. This can be corrected by multiplying the distances reported by the sensor by 1.25. The programs in this lesson include this correction factor. However, it might be worthwhile to check the distances reported by the sensors used by the students to see whether such a correction factor is needed (and, if so, what factor).

#### Directionality and Range

As said above, the sensor consists of an emitter and a receiver. The emitter does not emit sound equally in all directions. It has some directionality. It emits most strongly directly ahead and less strongly at larger angles from the central axis.  Likewise, the receiver is not equally sensitive to all directions.  It is also most sensitive to echoes returning from straight ahead and less so for echoes returning at an angle. The upshot of the directionality of both the emitter and the receiver is that the whole sensor (combination of receiver and transmitter) has some directionality.

The sensor's variable sensitivity as a function of angle means that the weakest echo it can detect depends on the angle from which the echo returns. The strength of an echo depends mostly on two factors: first, the distance from which it returns, and second, the object from which it returns. Echoes returning from further away are weaker. The strength of an echo also depends on the shape and material of the object. In general, smaller objects return weaker echoes.

The conclusion of this discussion is that for a given target object, the sensor has a maximum range at which it can detect the echo. This range depends on the angle at which the object is placed with respect to the sensor.

To make this a bit more tangible, consider the following graph. This graph is provided by a manufacturer of a specific sonar sensor (Maxbotix, a well-known manufacturer of a wide range of sonar sensors). This is not the sensor used in this lesson, but the example is illustrative.

![](images/sonar-lesson-plan-3ea35653.jpg)

Each square of the grid measures 30 x 30 cm. The sensor is assumed to be placed at the bottom of the graph, pointing upwards. The black line shows the area where the sensor can detect a target object. The red dots show the same for another setting of the sonar sensor. For our purpose, these can be ignored. In this case, a 10 cm diameter wooden pole was used. This graph shows that the pole can be detected at a maximum range of 240 cm (8 squares x 30 cm) straight ahead.

In contrast, in the direction of the blue arrow (which was added to the graph), the maximum detection distance is smaller, estimated at about 190 cm. Note the blue arrow only deviates from the centerline by about 20 degrees. However, the detection range for the same wooden pole is 50 cm (or 20%) less at an angle of only 20 degrees from the centerline.  At 30 degrees, the detection distance is only about 120 cm (50% reduction in detection distance).

This shows that the Maxbotix sensor is very directional: detection distances fall rapidly as the angle with the centerline increases. The same holds for our mBot sensor. Makeblock specifies a detection range of 3 to 400 cm for this sensor. The upper figure is only theoretical, however: it assumes a very large object straight ahead. In practice the range is substantially smaller, especially for smaller objects. There is a lower limit too — objects closer than about 3 cm cannot be detected at all.

Students will explore the directionality and the problem with sound mirrors in the following activities.

### The mBot sensor compared to animal sonar

Here, we relate the above concepts to animal sonar, enabling students to see parallels and differences between artificial sonar systems and biological echolocators. Above, we learned that the mBot sonar sensor emits sound pulses of about 40 kHz. Many echolocating bats use calls with a broad frequency range. For example, below, we show a recording of the big brown bat, copied from the U.S. National Park Service website. This plot is a spectrogram. It shows the frequencies in the bat's calls as a function of time. This spectrogram shows that this bat's call contains frequencies between about 60 and 25 kHz. You can play a slowed-down version of the sound recording on the U.S. National Park Service website. By slowing down the recording, the sound becomes audible to humans. When you listen to the recording, you will notice that this bat’s calls sound like ‘chirps’; indeed, bat calls are often called chirps, as this is what they sound like on slowed-down recordings.

![](images/sonar-lesson-plan-bcb99b25.png)

[Echolocation - Bats (U.S. National Park Service)](https://www.nps.gov/subjects/bats/echolocation.htm)

Echolocating whales and dolphins' calls typically contain an even broader range of frequencies than bats' calls. Below, we show the spectrogram of dolphin sonar sounds. The sounds contain frequencies from 0 to 150 kHz (the highest frequency measured).

![From https://acoustics.org/pressroom/httpdocs/163rd/Mishima_2aAO5.html](images/sonar-lesson-plan-342a9881.jpg)

From [https://acoustics.org/pressroom/httpdocs/163rd/Mishima_2aAO5.html](https://acoustics.org/pressroom/httpdocs/163rd/Mishima_2aAO5.html)

> **Tip**
>
> In summary, a key difference between animal echolocators and artificial sonar is that animals typically use sounds with a broad spectrum (i.e., their sounds contain a broad range of frequencies). This has several advantages but is difficult to reproduce in artificial sonar. Therefore, artificial sound most often uses sound with a narrow spectrum (i.e., a very limited range of frequencies)

Above, we discussed that artificial sonar sensors are directional: they are more sensitive in some directions than others. Likewise, animal sonar systems are also directional. Below, we show an image showing a top view of the emission directionality of a bat and a dolphin. These images show the “loudness” of their calls in each direction. Straight in front of the animal, the calls are the loudest. Left and right, the call is quieter. On top of this, the animals’ hearing is also directional. They are more sensitive to echoes coming from straight ahead and less to peripheral echoes.

![](images/sonar-lesson-plan-c01f834f.png)

> **Tip**
>
> In summary, just like the mBot sonar, animal sonar is directional. Animals can detect small objects more readily straight ahead than from the side.

### Activities

Below, we introduce two activities that familiarize the students with the operation of the robot’s sonar sensor.

> **Note**
>
> These two activities are optional and can be skipped if time is limited.

[Activity 1: Measuring the sonar’s directivity](#activity-1-measuring-the-sonars-directivity)

[Activity 2: Acoustic mirrors](#activity-2-acoustic-mirrors)

## Part 2: Programming and Building

Below, we provide two activities that can be used to challenge the students. The first activity asks the students to program a robot equipped with two sonar sensors to avoid obstacles. The second activity asks students to design, program, and test a sonar-based cane to support visually impaired people.

### Activity: Robot obstacle avoidance

Click the link below to access the robot obstacle avoidance activity instructions.

[Robot obstacle avoidance](#robot-obstacle-avoidance)

### Activity: Building a sonar cane

Click the link below to access the sonar cane building instructions.

[Sonar cane](#sonar-cane)


## Activity 1 Measuring the sonar’s directivity


In this activity, students will create a graph (on the floor) to understand what a single sonar sensor can be expected to detect.

> **Tip**
>
> For this activity, plug in the sonar sensor to port 1. The robot should be equipped with only one sonar sensor for this activity (see image below).

![For this activity, the robot should be equipped with a single sonar sensor (this is the default configuration of the robot). **In this stock image, the sonar is plugged in to port 2 but we will use port 1 for this activity.**](images/activity-1-measuring-the-sonars-directivity-60d0fadf.jpg)

Open the Sonar Directionality Program in mBlock 5 from the link below and connect to your robot using the dongle connection. [See here for instructions](#getting-started-with-the-robot) on how to connect to the robot.

[sonar_directionality](https://planet.mblock.cc/project/3916152) — or [download `sonar_directionality.mblock` directly](https://drive.google.com/file/d/1ycsKwRZEAqmBKjQ5AxTq4WWw4T5JBfVx/view?usp=sharing) if your school blocks the Makeblock site.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
> You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to your computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#running-your-first-program) for an example and more instructions.

The program is straightforward: It continuously measures the distance from the sonar and checks whether the returned value is smaller than 400 cm. If nothing is detected, the sensor returns a value of 400 cm. If the sensor detects something, the green LEDs on the robot are switched on.
If nothing is detected, the red LEDs are switched on. Therefore, the robot’s color should indicate whether the sonar picks up an echo.

To measure the region in which the robot can detect an obstacle, place the robot in a large open space (see image below). Next, move an obstacle in front of the robot (in this case, a black pole) to find the largest distance at which the object is detected (the robot turns green) for several directions. While doing this, ensure that the robot is not picking up echoes from your body. In all likelihood, your body will be a larger object than the one you use to assess the sonar’s reach.

![](images/activity-1-measuring-the-sonars-directivity-d833df5e.jpg)

In trials for this lesson, a black plastic tube pole was used as the obstacle, and straws (or tape) were placed on the floor, connecting the positions at which the robot could detect it. For every position in the area delineated by the straws, the robot could detect the tube pole (the robot turned green). Moving the tube pole outside this area turned the robot red.

You could repeat the measurements with different objects and compare the resulting patterns.

### Questions

- What is your robot's maximum detection distance?
- Is the sensor’s directionality symmetric?


## Activity 2 Acoustic mirrors


The previous activity revealed that the sonar sensor's range is limited. To use the sonar effectively, especially indoors, we must understand a second limitation.
In contrast to natural environments, indoor environments contain many smooth surfaces, which can be a problem for sonar. If the sonar pulse strikes a smooth surface at an angle, much of the sound will be reflected away from the receiver instead of towards it. This might result in the sonar sensor not detecting large smooth surfaces. This is called the acoustic mirror effect.

This effect can be observed by pointing the robot to a smooth surface (like a wall) while the program used in [Activity 1](#activity-1-measuring-the-sonars-directivity) is running:

[sonar_directionality](https://planet.mblock.cc/project/3916152) — or [download `sonar_directionality.mblock` directly](https://drive.google.com/file/d/1ycsKwRZEAqmBKjQ5AxTq4WWw4T5JBfVx/view?usp=sharing) if your school blocks the Makeblock site.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
> You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to your computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#running-your-first-program) for an example and more instructions.

- Point the robot straight at the wall from about 30 cm. Can the robot detect the wall?
- Now, point the robot at the wall at an angle of about 45 degrees.  Is the robot still able to detect the wall?  Experiment with different angles to see how well the robot can detect the wall at an angle.
- This acoustic mirror effect might be essential to understanding our robot's behavior in upcoming activities. If your robot keeps colliding with large, smooth objects or surfaces, it might be suffering from this acoustic mirror problem. What solutions can you devise to avoid this issue?

![Left: the robot is pointed straight at a smooth, flat wall. The sonar sensor has no problem detecting the wall and turns green. Right: The robot is pointed at the wall from an angle. Due to the acoustic mirror effect, the robot does not detect the wall.](images/activity-2-acoustic-mirrors-3936ab65.png)


## Robot obstacle avoidance


### Preparing the robot

In this activity, students will build a robot that uses two sonar sensors to avoid obstacles. Students will need to attach the two sensors to the robot.

> **Tip**
>
> You could ask the students for thoughts about how two sensors might be helpful.
>
> A single sonar sensor gives us the distance to the nearest detected obstacle. However, this yields little information about the obstacle’s position. All we know is an obstacle is somewhere in front of the robot. Using two sensors, the distances they return can be compared. If the distance picked up by the left sonar sensor is lower, one can assume that the obstacle is more to the robot's left. Or perhaps there is an obstacle at the left that the right sensor cannot detect (which means that obstacle is either further away or smaller). In either case, turning right to avoid this obstacle makes sense. In summary, having two sensors makes it possible to decide whether to turn left or right.

The [Thingiverse](https://www.thingiverse.com/dvanderelst/designs) page provides several brackets that can be 3D printed to facilitate mounting two sensors on the robots (two versions of the brackets are used in the image below). Alternatively, the spacing of the holes on the robot is compatible with Lego Technic. In the past, we have provided students with Lego and asked them to be creative about mounting the robot's sensors.

![The red brackets were 3D printed. The STL files accompanying these lesson plans are available on the Thingiverse page.](images/robot-obstacle-avoidance-a3f214cb.jpg)

The red brackets were 3D printed. The STL files accompanying these lesson plans are available on the [Thingiverse](https://www.thingiverse.com/dvanderelst/designs) page.

![](images/robot-obstacle-avoidance-519ceb09.jpg)

![](images/robot-obstacle-avoidance-72615833.jpg)

### Programming the robot

Students could be asked to design a program for the robot that allows it to avoid obstacles using the sonar sensors. Below, we discuss the linked example program. This program assumes that the left sonar sensor is connected to port 1 and the right sensor to port 2. A screenshot of the program is provided below.

[sonar_obstacle_avoidance](https://planet.mblock.cc/project/3916162) — or [download `sonar_obstacle_avoidance.mblock` directly](https://drive.google.com/file/d/1-NNPwR_EeliOnSDDOA87IJ-XHtJDunZ1/view?usp=sharing) if your school blocks the Makeblock site.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
> You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to your computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#running-your-first-program) for an example and more instructions.

The main program loop is shown first. This loop continuously goes through the same steps. It queries the sensors. If the left sonar sensor detects the smallest distance (`min_side = left`), the robot turns left as long as the left sonar returns a distance smaller than the safe distance. If the right sonar detects the shortest distance, the robot turns right as long as the right sonar returns a distance smaller than the safe distance.

![](images/robot-obstacle-avoidance-18f6461b.png)

The safe distance is defined at the start of the program. Here, it is set to 30 cm. The result is that the robot turns left or right (on the spot) if one of the sensors returns a distance smaller than the safe distance.  And the robot keeps turning until that sensor returns a large enough value.

Let's break down the program into simpler terms:

1. `do_sensing`: This block collects data from both sonar sensors. It measures the distances to obstacles on the left and right sides of the robot. It also multiplies the values by 1.25. See [here](#sonar) for an explanation of why this multiplication is performed.
2. `min_distance`: This variable stores the smaller of the two distances measured. It tells us how close the nearest obstacle is, regardless of which side it's on.
3. `min_side`: This variable tracks which sensor (left or right) detected the closest obstacle. It's crucial to decide which way the robot should turn to avoid the obstacle.

Here's how these elements work together:

- The robot constantly checks both sensors using `do_sensing`.
- It compares the distances and updates `min_distance` and `min_side`.
- If `min_distance` is less than the safe distance, the robot must turn.
- The `min_side` then determines which way to turn: if it's "left,” the robot turns right to avoid the obstacle, and vice versa.

The red blocks in the program above are defined in the image below.

![Screenshot from 2024-10-28 16-11-25.png](images/robot-obstacle-avoidance-57525850.png)

### Running the program

When students run the program, the robot should move forward as long as it is far away from obstacles. It should turn on the spot when close to them. Depending on where the robot is tested, students might notice that the robot seems blind to some obstacles. This happens when the obstacles have a small surface area. These return weak echoes and might go undetected. They might also see the mirror effect coming into play. When approaching a smooth wall or other surfaces under an oblique angle, the robot happily drives into the obstacle as no strong echoes return.
Therefore, it might be worthwhile to construct an arena for the robot populated with obstacles the sensors should be able to detect. A circular arena of children’s toys has been built in the example below. These objects consist of multiple surfaces oriented in many different directions. This makes them very likely to return echoes the robot can pick up.

Plastic drinking cups could also be used to build an arena. If drinking cups are used, make sure they are tall enough to reach the level of the robot's sensors. If not, the sonar sensor might literally overlook the cups.

The acoustic complexity of the toy arena can be appreciated by looking at a recording made of the echoes received by the robot. For this, the ultrasonic recorder was placed on top of the robot to record emissions and echoes. This procedure is also used by scientists who study bats: by placing a mini recorder on the bats' back, they learn what echoes the bat perceives. The recording shows that the first echo returns from a distance of about 30 cm. However, many other echoes can be seen as well. This shows that the toys return many echoes, increasing the chance one will be picked up by the robot.

![Here, the robot is tested in an arena that consists of several toys. These complex objects (as opposed to flat walls) are guaranteed to return strong echoes to the robot.](images/robot-obstacle-avoidance-3237775a.jpg)

![One recorded echo as perceived by the robot. The marked part is the robot’s emission. The remainder of the signal consists of echoes returned from the many surfaces in the arena depicted on the left.](images/robot-obstacle-avoidance-6a79cb0c.png)


## Sonar cane


Several inventors and companies have designed sonar-enabled canes for visually impaired people. The general idea of these devices is to use a sonar sensor (or multiple sensors) to detect obstacles in the user's path. The distance picked up by the sensors is then conveyed to the user by employing non-visual cues.

> **Tip**
>
> Show students the YouTube video below describing such a device. Using the robot, students will build a device that does something similar: use one or two sensors to detect obstacles and the robot's speaker to convey this information to a (blindfolded) user. The student guide for this part can be found here.

[https://www.youtube.com/watch?v=cnW1_XMUIzM](https://www.youtube.com/watch?v=cnW1_XMUIzM)

In this activity, the student builds a device that does something similar: use one or two sonar sensors to detect obstacles and use the speaker on the robot to convey this information to a (blindfolded) user. The sonar device should detect obstacles missed by the cane (the user employs their cane to probe for obstacles on the floor while the sonar device looks horizontally for overhanging obstacles).

![](images/sonar-cane-6beb49f4.png)

### Mounting the robot on the PVC pipe

Students will mount the robot on a 1/2-inch PVC pipe for this activity. They can mount 1 or more sonar sensors anywhere on the PVC pipe. For this, they can use 3D-printed brackets, Lego-compatible blocks, or other materials. Here, we explain how to mount the robot on the PVC pipe using a mounting plate.

#### Step 1

Remove the caster wheel from the front of the robot.

![](images/step-1-b0e9918f.jpg)

#### Step 2

Mount the platform on the PVC pipe using two screws and a 1/2 inch pipe bracket. It is important to mount the platform with the broad side to the side of the pipe that will be used as the top of the sonar cane.

![](images/step-2-f2db380c.jpg)

#### Step 3

Use at least two screws to fix the robot to the platform. You can use the screws from the caster or any M4 machine screw.

![](images/step-3-a36ea32a.jpg)

![](images/step-3-dffc78d1.jpg)

#### Step 4

Add more screws using the holes pointed out in the image below.

![](images/step-4-2686475f.jpg)

#### End result

This image shows the end result: the robot is mounted on the cane. Now students can add one or more sonar sensors to the cane.

![](images/end-result-ccd5463c.jpg)

### Example Program

We provide an example program. The program is linked and displayed below.

> **Note**
>
> The example program below assumes one sonar sensor is being used. However, students can use more than one sensor.

[sonar_cane](https://planet.mblock.cc/project/3916250) — or [download `sonar_cane.mblock` directly](https://drive.google.com/file/d/1nENLgknP-9-Gud3_HAl-3C0QFPo1bq6T/view?usp=sharing) if your school blocks the Makeblock site.

> **Tip**
>
> Clicking the link to the program will open the mBlock website. To see the actual program, click `Source` at the bottom left of the page that opened.
>
> You can use the program in the online version of mBlock or download it to your computer by selecting `File` and `Save to your computer`. The downloaded program can then be edited using mBlock if installed on your computer.
>
> See [Step 1: Open the example program](#running-your-first-program) for an example and more instructions.

The program continuously measures the distance recorded by a sonar sensor, [applies the correction](#sonar), and converts the measurement in cm to meters.

![](images/sonar-cane-894677a6.png)

The distance (variable `distance`) is then used to set the duration of a beep. Smaller distances result in longer beeps, while higher distances result in shorter beeps. In equation form, the value `b` (in seconds) is determined as follows: 

$$
\begin{aligned}
b &= 0.49 - 0.4 \times \text{distance} \\
b &= 
\begin{cases}
0, & \text{if } b < 0 \\
0.25, & \text{if } b > 0.25 \\
b, & \text{otherwise}
\end{cases}
\end{aligned}
$$

The relationship between the distance `d` and the duration of the beep `b` is visualized in the following plot. The values `0.49` and `0.4` determine the slope of the line for intermediate distances. When the distance is over about 1.2 meters, the duration of the beep is zero, and the robot will not beep at all. For distances below 0.6 meters, the duration of the beep is maximal (0.25 seconds). At these short distances, the motors are also turned on for 0.25 seconds to give the user some vibrational feedback.

![](images/sonar-cane-b9caef3a.png)

### Testing the program

The sonar device was designed to detect obstacles missed by the cane sweeping the floor. Therefore, test the sonar cane with overhanging obstacles. For example, have students hold out pieces of cardboard or other objects in the path of a blindfolded student testing the cane. The blindfolded student should use the physical cane to sweep their path for obstacles on the floor. The sonar should inform them of upcoming overhanging obstacles.

It is worthwhile for students to take time to practice using the sonar cane. Afterward, they can reflect on the system's benefits and drawbacks. Try to have them think critically about the potential benefits of sonar-based systems to visually impaired people. What are the drawbacks? What improvements can they conceive?

The images below show students using a sonar cane to avoid obstacles. Note that these students use a different robot and have mounted the robot in a different way than explained above.

![](images/sonar-cane-630a642a.jpg)

![](images/sonar-cane-ff190d27.jpg)

![](images/sonar-cane-7bef03ce.jpg)

![](images/sonar-cane-314965f7.jpg)

![](images/sonar-cane-935870be.jpg)

![](images/sonar-cane-b5d37240.jpg)
