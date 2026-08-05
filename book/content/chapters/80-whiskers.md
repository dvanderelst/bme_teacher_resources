# Touch and Whiskers

## Materials

| Item | Description |
| :--- | :--- |
| mBot | The same robot as every other chapter. |
| Bluetooth Dongle | A dongle for connecting the robot to a computer. Currently the recommended connection method. |
| Whisker sensors | Two per robot for the obstacle avoidance challenge, one for wall following. Two is the maximum: the block that reads them offers only two ports. These are custom sensors with the same form factor as a Makeblock sensor, using a flex sensor as the active element. They are not commercially available. Contact the addresses under [Questions, corrections, and help](#questions-corrections-and-help) to obtain a set. Treat sensors as consumables: they are damaged by creasing, by bending the wrong way, and slowly by oxidation. |
| 3D printed brackets | Brackets for mounting sensors on the front of the robot in different orientations. |
| Lego compatible blocks | Blocks compatible with the robot's screw holes, giving students flexibility in mounting angles. |
| Gaffer's tape | Versatile tape useful throughout the activities. |
| Extra cables (short) | Extra cables for connecting sensors, allowing students to add whiskers without unplugging existing connections. |
| Batteries | The robot requires 4 AA batteries. |
| Index cards or business cards | The backing for the two-point discrimination pokers. One per pair of students. |
| Toothpicks, or stiff plastic fiber | The points themselves, snapped in half and taped to the card. |
| Printed poker template | Printed from brainmapper.org and glued to the card; it sets the spacings. |
| Sticky tape | For fixing the points to the card. |
| Calipers | An alternative to the paper pokers. Set them to a spacing and poke with the tips of the jaws. |
| Cardboard strips | Taped to a whisker sensor to extend its reach past the flex sensor's own length, and to change how it bends. |
| Painter's tape | For attaching the cardboard. Removes cleanly without damaging the sensor. |
| Airtight box and desiccant | For storing whisker sensors between lessons, lying flat. |

<!-- TODO: the whisker entries are in the Required materials chapter, but the rest of this table is not, and that chapter still reads as a list of things to order when one line on it cannot be ordered. Worth a sentence at the top of it saying so, rather than leaving a teacher to find out at the bottom of a table. -->

## Prerequisites

Student knowledge: High school Biology and Algebra 2 or equivalent.

This lesson is self-contained, but builds most effectively upon [Sonar](#sonar), which introduces active sensing in a form students have already encountered, and [Kinesis and Taxis](#kinesis-and-taxis), which provides the vocabulary for the robot behaviors they will implement here.

## Investigating / Essential Questions

- How does an animal build a picture of its surroundings using only touch?
- What changes when the sensor must be moved to the object rather than pointed at it?

## Educational Standards

The educational standards applicable to this lesson are listed in the [Educational standards](#educational-standards) chapter.

<!-- TODO: the standards chapter has a Touch and Whiskers section, but it is a placeholder saying the alignment is not written yet. Replace it with the real thing. -->

## Learning Objectives

1. Explain that touch is not a single sense, and that different receptors report different aspects of the same contact.
2. Measure tactile acuity and relate the result to receptor density and to cortical representation.
3. Understand that a whisker senses at its base, not along its length.
4. Explain why an animal moves its whiskers, and relate this to other forms of active sensing.
5. Calibrate a flex sensor and use it to drive a robot behavior.

## Introduction

In this lesson, students investigate touch in three contexts: human, animal (rat), and robotic. Touch is the only sense that requires direct physical contact with a stimulus, and this constraint fundamentally shapes how animals use it. While eyes and ears can be directed at distant objects, whiskers must make physical contact, requiring the animal to move. This active movement of the sensor to gather information is the central theme of the lesson.

The lesson consists of two parts. In Part 1, students measure the spatial acuity of their own skin, learn the functions of different cutaneous receptors, and examine how rats solve similar problems using whiskers. In Part 2, students equip a robot with whiskers made from flex sensors, calibrate them, and implement one of two behavioral challenges.

## Part 1: Touch in animals

### Touch is not one sense

Touch perception encompasses more than simple pressure detection. Human skin contains multiple receptor types that differ along two key dimensions, which together explain most tactile capabilities and limitations.

The first dimension is **dynamics**. Phasic receptors respond to transient events—initial contact, release, or vibration—and cease firing during sustained, steady pressure. This adaptation explains why constant stimuli, such as clothing against the skin, eventually go unnoticed. Tonic receptors, by contrast, continue signaling throughout the duration of contact.

The second dimension is **receptive field size**, which refers to the area of skin each receptor monitors. Small receptive fields enable precise spatial localization, while large fields cover more area with fewer receptors, resulting in poorer spatial resolution.

> **Note**
>
> The term "slow-adapting" for tonic receptors is frequently misunderstood. It does not indicate a slow response to initial stimulation; slow-adapting receptors can fire immediately upon contact. The term refers instead to their slow cessation of firing when the stimulus is removed.

### The four receptor types

| Receptor | Dynamics | Field and depth | Function |
| :--- | :--- | :--- | :--- |
| Merkel disk | Tonic | Small, shallow | Fine spatial detail, edge detection, sustained touch. Merkel disks are primarily responsible for Braille reading. |
| Meissner corpuscle | Phasic | Small, shallow | Light flutter and movement across the skin; low-frequency vibration. |
| Pacinian corpuscle | Very phasic | Large, deep | High-frequency vibration and brief pressure changes. Extremely sensitive. |
| Ruffini ending | Tonic | Large, deep | Skin stretch and lateral deformation; the shape the hand is currently in. |

These four receptor types demonstrate how combinations of dynamics and field size produce distinct sensory functions. Small receptive fields combined with tonic adaptation enable fine spatial detail, while small fields with phasic adaptation detect motion across the skin. Large fields with highly phasic response detect vibration, and large fields with tonic adaptation signal skin stretch. Each receptor type thus provides a distinct class of tactile information; no single receptor performs all functions.

### Whiskers

#### A whisker senses at its base

Nearly all mammals possess whiskers; humans are among the few exceptions. This absence relates to how humans investigate objects: humans use their fingertips, which have the finest spatial acuity on the body (as students measure in Activity 1). Animals that cannot manipulate objects with their forelimbs require alternative tactile strategies, which whiskers provide.

A whisker, or vibrissa, is a specialized hair that is stiffer than fur, with a thicker base that tapers along its length and a slight curvature. Like all hair, the shaft consists of dead keratin and contains no nerves. Consequently, no sensation occurs along the length of the whisker.

The sensory apparatus is located at the follicle at the whisker's base, which is among the most densely innervated structures in mammalian skin. The whisker shaft functions as a lever: when the tip contacts an object, the whisker bends, transmitting forces and torques to the follicle, where mechanoreceptors transduce these mechanical signals.

The shaft is not uniform in structure. It tapers from a thick, stiff base to a thin, flexible tip. This non-uniform elasticity means that upon contact, minimal bending occurs at the base while substantial deflection happens at the distal end. This tip flexibility is believed to contribute to texture discrimination.

The tip makes contact, but sensing occurs at the base. This distinction is a key concept for the lesson, as it parallels how the robot's whisker functions.

From the follicle, superficial and deep vibrissal nerves transmit signals that converge to form the infraorbital nerve, which reaches the brain via the trigeminal nerve—the same pathway serving the rest of the face. This topographic organization is preserved throughout the neural pathway: whiskers map to barrelettes in the brainstem, barreloids in the thalamus, and barrels in the somatosensory cortex. Each whisker corresponds to a discrete cluster of cortical cells, making this system a model for studying sensory organization in neuroscience.

The array is as important as the individual whisker. Rats possess approximately fifty whiskers arranged in a stereotyped pattern of five rows, with sufficient consistency between animals that individual whiskers can be identified and named. When an object is contacted, different whiskers bend to varying degrees, providing the animal with a spatial pattern of deflections rather than a simple binary signal. The brain's organization reflects this investment: in the somatosensory cortex, each whisker maps to a distinct barrel, with the barrels arranged in the same pattern as the whiskers on the face.

#### Whisking is active sensing

Many rodents do not keep their whiskers stationary. Rats and mice actively sweep them forward and backward—a behavior called whisking—and adjust the sweep parameters based on task demands. Short, rapid sweeps are used for close surface examination, while broader sweeps explore open space. This active movement allows the animal to control where and when contact occurs.

Whisking rates exceed most students' expectations: opossums whisk at approximately 5 Hz, rats at 8 Hz, and mice at up to 25 Hz. These rhythms are not generated moment-to-moment; rather, they originate from a brainstem pattern generator, similar to the mechanism controlling locomotion. The animal modulates the sweep parameters rather than individual strokes.

The whisking mechanism differs from initial expectations. Each follicle is encircled by a muscular sling anchored posterior to it. When the sling contracts, it pulls the deep end of the follicle backward. Because the follicle pivots near the skin surface, the external portion of the whisker swings forward. Thus, the muscle pulls backward to enable forward whisker movement.

Each muscular sling serves an entire row of follicles, causing all whiskers in a row to move synchronously rather than independently.

This arrangement, which initially appears limiting, represents an elegant engineering solution. Fifty whiskers, each with a follicle of unique length and spacing, could theoretically require fifty individual muscles with precise coordination. Instead, a uniform percentage contraction of each intrinsic muscle produces a uniform angular sweep across all whiskers. The array geometry itself ensures synchronization, allowing the animal to control a single parameter rather than fifty. Engineers use the same principle: rather than driving each windshield wiper with a separate motor and coordination system, a four-bar linkage mechanism connects both wipers, ensuring synchronized movement through mechanical constraints.

This mechanism produces a second important consequence: as whiskers sweep forward, their tips converge, causing the same array to sample a progressively smaller area of space. This increases sampling density precisely where the animal is about to make contact. This phenomenon has been termed *foveal whisking* by analogy to the eye's fovea, though a more accurate comparison is to a microscope, where adjusting the zoom concentrates detail within a shrinking field of view. Unlike the retina's fixed geometry, rats can adjust this sampling density on demand.

![How a whisker is moved, and where it is sensed. **A**, the muscle is relaxed and the whisker lies back. **B**, the muscle contracts, pulls on the follicle, and swings the whisker forward; repeating that cycle is whisking. **C**, the whisker runs into something. The dashed line is where it would have carried on had the obstacle not been there. Note where the bending happens: a whisker tapers, so it is stiffest at the base and most flexible near the tip, and the shaft therefore leaves the follicle almost straight and does its bending out at the far end, which curls away from the obstacle. The mechanoreceptors are clustered around the follicle at the base, and the bend is what they measure. Schematic, and not to scale.](images/touch-and-whiskers-follicle.png)

[Video: Rat whiskers moving, with the movement of the head subtracted](https://www.youtube.com/watch?v=d7rSsMZyThQ). With head motion removed, the video demonstrates that whiskers are actively aimed, independently of the animal's locomotion.

This active sensing principle parallels the [Sonar](#sonar) lesson. A bat controls when it vocalizes and what it vocalizes, thereby determining the information its next echo will provide. Similarly, a rat controls where its whiskers go, determining what its next contact will reveal. In both cases, the animal is an active participant in sensory acquisition, and this control is central to the sense's effectiveness.

The primary difference is range: a bat's echolocation can detect objects several meters away, while a rat's whiskers reach only about three centimeters. This limited range fundamentally shapes how whiskers are used.

#### Animals that rely on whiskers

**Rats and mice** rely on whiskers as a primary sensory modality. They use whiskers to judge gap width before entry, discriminate surface textures, and locate objects relative to their head position—particularly in dark or confined environments where vision is ineffective.

![Two vibrissae side by side, at the same scale. **A**, a California sea lion's — a smooth cylinder. **B**, a harbour seal's — undulated along its whole length. The seal's whisker shape prevents vortex shedding and self-generated vibration during swimming, enabling detection of fish hydrodynamic trails. Photograph by Murphy, Eberhardt, Calhoun, Mann and Mann (2013), [CC BY 2.5](https://creativecommons.org/licenses/by/2.5/).](images/touch-and-whiskers-vibrissae.png)

**Seals** use whiskers in aquatic environments. Harbour seals can follow the hydrodynamic trail left by swimming fish—the disturbed water in the wake, which persists for many seconds. Even with eyes and ears covered, seals can detect and follow these trails. Seal whiskers differ from those of terrestrial mammals: they are not smooth cylinders but have a wavy, undulating structure along their length. This shape suppresses vortex shedding that would otherwise cause the whisker to vibrate in the animal's own wake, effectively providing noise cancellation through structural design.

This sensory investment is evident in the neural wiring: aquatic mammals have approximately ten times the nerve endings around each whisker follicle compared to terrestrial mammals.

Seals also whisk. Recent research indicates that while a forward-positioned whisker offers maximum sensitivity, maintaining this position requires continuous muscular effort. Instead, seals keep their whiskers retracted and sweep them rhythmically, achieving most of the sensitivity benefit at a fraction of the energy cost. This represents a classic engineering trade-off between performance and efficiency, similar to decisions about sensor polling rates.

[Video: Harbour seal whiskers, in three minutes](https://www.youtube.com/watch?v=-ozBE6f3hrE). The video covers whisker anatomy, the undulated shape of seal vibrissae, and experimental demonstration of a blindfolded seal following the wake of a small remote-controlled submarine using only touch.

> **Note**
>
> Insect antennae perform similar functions—touch and movement sensing near the body—and students often equate them with whiskers. However, antennae and vibrissae are anatomically distinct structures. While the behaviors may appear similar, the underlying anatomy differs. The comparison can serve as a useful analogy if clearly identified as such.

## Activity 1: Two-point discrimination

This activity measures tactile spatial acuity: the minimum distance at which two separate points of contact are perceived as distinct. This distance is the **threshold** for a given skin region, and it varies across the body by more than an order of magnitude.

The activity uses the protocol developed by [brainmapper.org](https://brainmapper.org), an outreach project of the Max Planck Florida Institute for Neuroscience. The site also provides a tool that generates a cortical homunculus visualization from the class data.

### Two ways to make the points

There are two methods for creating the two-point discrimination tools:

**Calipers** are the recommended option. Set them to a specific spacing using the scale, then use the tips of the two jaws for testing. One pair per group is sufficient. The spacing is precise, and adjusting the distance requires only a moment.

**Paper pokers** provide an alternative for classes without sufficient calipers. Print the template from brainmapper.org, glue it to an index card or business card, and attach a pair of points (such as snapped toothpicks or stiff plastic fiber) to each marked spacing so the points overhang the card edge by approximately 13 mm. Each card carries a fixed set of spacings. While this method is slower to work through, it ensures all groups test identical distances.

> **Tip**
>
> Regardless of the method used, the two points must be perfectly level with each other. If one point sits higher, it contacts the skin first, allowing the subject to use temporal cues rather than spatial separation. Check both calipers and cards for this issue, as worn or bent caliper jaws can also cause it.

### Procedure

Assign roles: one student serves as the tester, another as the subject. The subject closes their eyes and keeps them closed throughout testing. The tester presses both points against the subject's skin simultaneously and asks: "One point, or two?"

Begin with the widest spacing (60 mm) and proceed to narrower distances. Continue until the subject reports feeling only one point, and record **that** distance—the first spacing perceived as a single point. If the subject still reports two points at the smallest available spacing, record the smallest distance tested.

> **Note**
>
> Recording the first distance perceived as *one* point follows brainmapper's established convention. This is not arbitrary; it aligns with the site's data entry requirements. Recording the last distance perceived as two points would shift all values by one step and distort the resulting homunculus.

Test six anatomical sites: forehead, back, arm, palm of the hand, leg, and foot.

> **Tip**
>
> Three factors can compromise measurement accuracy; all are easily avoided:
>
> **Apply both points simultaneously.** If one contacts the skin before the other, the subject may use timing cues rather than spatial separation, producing artificially high acuity scores.
>
> **Maintain consistent, gentle pressure.** Variability in pressure affects the threshold distance.
>
> **Test the same location each time.** Receptor density varies within body regions, not only between them. Moving the test location across the forearm, for example, averages results from different patches of skin.
>
> Use blunt points and light pressure. If testing causes pain, it has become a pain detection task rather than a discrimination task.

### Interpreting the results

A lower threshold indicates finer spatial acuity, reflecting higher receptor density with smaller receptive fields. The palm and forehead typically demonstrate superior acuity compared to the back, leg, or arm, though the precise ranking varies between individuals and testers. Variation across the class represents genuine differences rather than experimental error.

It is important to clarify a common misconception: a lower threshold does not indicate that touch feels *more intense* at that location. Rather, it signifies that the brain can distinguish two nearby touches as *separate*. The difference concerns precision, not intensity.

### The homunculus

Enter the six threshold distances into the dropdown boxes at [brainmapper.org/experiment](https://brainmapper.org/experiment). The site generates a cortical homunculus—a representation of the human body in which each part is scaled according to the amount of somatosensory cortex devoted to it rather than its actual physical size. In this representation, the hands, lips, and tongue appear disproportionately large, while the trunk and legs appear much smaller.

The key educational point is that the distortion visible in the homunculus reflects the class's own experimental data. The brain allocates cortical representation in proportion to tactile acuity, not body surface area, which explains why the neural map of the body differs from its physical form.

![The sensory homunculus: a human body redrawn with each part scaled to the amount of cortex devoted to feeling it rather than to its actual size. The hands, lips and tongue dominate; the trunk and legs almost disappear. This is the same shape a class's own two-point measurements produce. Photograph by Wikimedia Commons user Mpj29, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).](images/touch-and-whiskers-homunculus.png)

## Part 2: Giving the robot whiskers

Mechanical whiskers are not a novel concept introduced for this lesson. They represent one of the oldest sensor types in robotics, valued for the same reasons they are useful to animals: they are inexpensive, require minimal computation, and detect obstacles already in contact with the robot.

Rodney Brooks's *Genghis*, a six-legged walking robot developed at MIT around 1991, provides a historical example. It navigated rough terrain using a hierarchy of simple behaviors, one of which was literally named "whiskers."

Beyond their low cost, whiskers function effectively in environments where other sensors fail. Vision requires light, and robots in pipes, burrows, collapsed buildings, or unlit rooms have none. Both sonar and cameras struggle in dust and smoke. Under such conditions, tactile sensing is not a poor alternative to vision—it is the appropriate solution, which is precisely why animals living in dark environments evolved whiskers rather than enhanced visual systems.

There is a second, research-oriented motivation: building a robot with whiskers provides a physical model for studying whisker biology. By adjusting parameters and observing failures, the robotic system can reveal insights about the animal system it emulates. Pearson and colleagues present both engineering and scientific arguments for biomimetic whisker research.

> Pearson, M. J., Mitchinson, B., Sullivan, J. C., Pipe, A. G., and Prescott, T. J. (2011). Biomimetic vibrissal sensing for robots. *Philosophical Transactions of the Royal Society B* **366**(1581), 3085–3096. [doi:10.1098/rstb.2011.0164](https://doi.org/10.1098/rstb.2011.0164). Not open access.

Demonstrating a robotic implementation before students build their own provides useful context. The Shrewbot project offers an example of how whisker research translates to robotics.

[Video: Shrewbot: shrew whiskers inspire robot design](https://www.youtube.com/watch?v=oRgE3-niJSI)

Shrewbot's whiskers are *active*: they sweep back and forth, replicating biological whisking in hardware. Observing the head rather than the whiskers reveals the key behavior: when the robot contacts an object, it turns its head to bring the sweeping whiskers into contact with the object again. The robot is not passively waiting for contact—it actively decides where to touch next, which captures the essence of active sensing.

This capability highlights a limitation of the robots in this lesson: their whiskers are fixed to the chassis, so the only way to aim them is by moving the entire robot. This distinction is worth noting early, as it returns as an important point in the final comparison.

## Activity 2: Setting up the robot whiskers

### The flex sensor

The robot's whisker uses a flex sensor: a thin strip whose electrical resistance increases as it bends. When flat, the resistance is approximately 10 kΩ; bending raises the resistance. Mounted to project forward and to the side, the whisker contacts obstacles tip-first, causing it to bend. The robot detects this bending.

This design provides a better model of biological whiskers than a simple switch. A switch reports only binary contact information, while a flex sensor provides a graded measure of deflection that more closely approximates the mechanical signals transduced by the follicle.

> **Note**
>
> There is one key difference between the biological and robotic implementations. An animal whisker senses only at its base; the shaft is dead, with all receptors located at the follicle. The flex sensor, by contrast, is itself the sensing element and responds to bending anywhere along its length. The robot's whisker is sensitive along its entire length, while the rat's is sensitive only at the base.
>
> However, both share the essential characteristic relevant to this lesson: a slender probe that deflects on contact, with that deflection converted into a signal.

![A whisker sensor. The board has the same shape as a Makeblock sensor and plugs into an RJ25 port like one, but the board is custom and the working part is the flex sensor clamped to the front of it. The segmented side facing up in this image is the metallic side: the whisker bends away from it, and bending it toward the metallic side damages the sensor.](images/touch-and-whiskers-sensor.png)

> **Warning**
>
> Flex sensors are fragile and require careful handling to prevent damage.
>
> They bend in **one direction only**—away from the metallic side. Bending toward the metallic side causes permanent damage.
>
> They must not be **creased or sharply folded**. A crease permanently damages the sensor.
>
> Mount the sensor so the bending region remains free to flex, and do not tape over it. Ensure the connector is fully seated and provide strain relief so the sensor is not stressed at the plug when the robot moves.
>
> **Store sensors flat in an airtight box with a desiccant sachet between lessons.** The metallic layer oxidizes over time, and sensors left in a drawer over an extended period may read differently or fail entirely. This degradation occurs gradually and may not be noticed until it is too late.

### Making the whisker longer

The flex sensor is only about 10 cm long, which provides a short reach for a robot the size of an mBot: the whisker detects a wall at the moment the robot has essentially arrived at it.

Reach can be extended by taping a strip of cardboard to the end of the sensor using painter's tape, which removes cleanly without damaging the sensor. The cardboard does not sense; bending still occurs only in the 10 cm flex sensor portion. However, the robot now contacts obstacles further away, providing more time to react.

This extension demonstrates an important biological parallel to students. A cardboard strip functions as a dead length of whisker that transmits force back to the sensing region near the base—exactly what a vibrissa does. The cardboard's length, stiffness, and attachment point all affect how the whisker bends and therefore how early and strongly the robot responds. Groups that experiment with these parameters typically achieve better performance than those that do not.

### Reading a whisker in mBlock

A whisker connects to an RJ25 port and is read using the **`light sensor [port] light intensity`** block, with the appropriate port selected from the block's dropdown menu. This is not the sonar block or the line follower block. The block is part of the light-and-sound extension, the same extension that provides the sound sensor blocks. If the sound localization lesson has been completed, this extension is already installed; otherwise, it must be added in mBlock before the block will appear.

The block provides access only to **ports 3 and 4**, which are the two ports whiskers must use. A single whisker can use either port. Two whiskers require both ports, which exhausts the mBot's analog input capacity.

> **Note**
>
> The block's name, *light sensor*, should not be interpreted literally. The whisker does not measure light. Both the light sensor and the whisker operate by changing resistance, and this block reads whatever resistance is present on the port, reporting a numerical value. The label simply reflects the block's original intended purpose, not what is connected to it. The practical consequence is the port limitation described above: whiskers inherit the light sensor's port restrictions.

> **Note**
>
> The reported value **decreases** when the whisker bends. This is counterintuitive to many students and teachers, but it is correct: bending the sensor reduces the number mBlock reports. An unbent whisker typically reads around 400, and bending drives this value downward.
>
> The exact resting value varies between sensors. Two unused whiskers on the same robot will not report identical values, which is why each must be calibrated separately and why left and right whiskers require individual thresholds. A threshold copied from another group's robot, or from another whisker on the same robot, will not function correctly.
>
> This principle extends beyond whiskers: always trust what the sensor measures, not what it seems like it ought to do. Bend the whisker by hand and observe the reported value before writing any control logic.

The simplest functional program reads both whiskers into variables continuously. This program does not yet use the values; it merely assigns each whisker reading to a variable once per loop, allowing subsequent code to reference `whisker1` and `whisker2` rather than repeatedly accessing the sensor blocks.

![The smallest useful whisker program: read each whisker into a variable, forever. Port 3 and port 4 are the only two the light sensor block offers, so a two-whisker robot uses both. Naming the variables is not merely organizational—every program later in this chapter references them, and threshold comparisons are significantly easier to debug when the reading has a descriptive name.](images/touch-and-whiskers-read-two.png)

[Open the mBlock project](https://planet.mblock.cc/project/8233113). If access to the Makeblock site is blocked, [download `mBotReadWhisker.mblock`](files/programs/mBotReadWhisker.mblock) instead.

Run this program and observe the variable values displayed on the stage while manually bending each whisker. This also serves as an informal calibration step: it provides the resting and bent values needed before programming any behavior.

### Calibration

Calibration is essential for Part 2 and must be performed for each whisker individually. Resting values typically sit near 400 but vary between sensors, so the values a group uses must come from their own robot's measurements, not from this text. Because bending drives the value *down*, thresholds must be set *below* the resting reading from which they were measured. This explains why the example program's thresholds of 400 and 375 are positioned as they are.

| Step | Action |
| :--- | :--- |
| 1. Read resting values | With nothing touching the whiskers, note the left and right values separately. |
| 2. Read bent values | Gently bend each whisker as it would bend against an obstacle, and note the value. |
| 3. Choose a threshold | Select a number between the resting and bent values, for each whisker independently. The left and right thresholds do not need to match, and typically will not. |
| 4. Test slowly | Run the robot at low speed first. Logic errors are easier to identify at slow speeds, and a slow robot is less likely to damage a whisker against a wall. |
| 5. Refine from behavior | If the robot reacts too late, the threshold is too close to the bent value. If it reacts constantly with nothing present, the threshold is too close to the resting value, or the whisker is not mounted neutrally. |

## Activity 3: Choose a challenge

Students select **one** of the two challenges below. There is no required order, and neither represents a single correct answer; they are distinct problems that use the same hardware.

| Challenge | Goal | Whiskers needed |
| :--- | :--- | :--- |
| Avoid obstacles | Navigate without colliding with objects | Two (left and right) |
| Follow a wall | Maintain light contact with a wall without crashing | One |

### Challenge 1: Avoiding obstacles

The obstacle avoidance strategy follows a direct biomimetic approach: contact on one side should cause the robot to move away from that side, which is the same rule rats use.

| Condition | Action |
| :--- | :--- |
| Neither whisker bent | Drive forward |
| Left whisker bent | Turn right |
| Right whisker bent | Turn left |
| Both whiskers bent | Reverse briefly, then turn to escape |

Because a bent whisker reads *below* its threshold, the logic translates as follows:

```text
If left > threshold AND right > threshold: forward
If left < threshold AND right < threshold: reverse briefly, then turn
If left < threshold: turn right
If right < threshold: turn left
```

Using separate variables with descriptive names (e.g., `leftWhisker`, `rightWhisker`) for the left and right readings makes this logic far easier to debug than nested comparisons.

A worked example builds directly on the reading program from earlier:

![One way to write the obstacle avoidance challenge. The two thresholds are set once at the start and then never mentioned again, which simplifies retuning: a robot reacting too late or too eagerly is fixed by editing two numbers at the top rather than searching through the logic. Note that the two thresholds are different—they belong to two different whiskers, and there is no reason two sensors should agree.](images/touch-and-whiskers-avoid-obstacles.png)

[Open the mBlock project](https://planet.mblock.cc/project/8233137). If access to the Makeblock site is blocked, [download `mBotWhiskerAvoidance.mblock`](files/programs/mBotWhiskerAvoidance.mblock) instead.

### Challenge 2: Following a wall

This challenge requires maintaining one whisker in light contact with the wall. If contact is lost, the robot should turn slightly toward the wall; if the whisker bends too far, the robot should turn slightly away.

```text
If the value is at or near resting (contact lost): turn slightly toward the wall
If the value is below threshold (bending too much): turn slightly away
Otherwise: drive forward
```

This represents a different programming paradigm from the first challenge. Obstacle avoidance reacts to discrete events, while wall following implements a continuous feedback loop, making small corrections toward a target it never quite reaches. This approach more closely mirrors how animals actually use whiskers, and it is accordingly the more challenging of the two to tune.

## Troubleshooting

| Problem | Likely cause | Solution |
| :--- | :--- | :--- |
| The value never changes | Wrong port selected, wrong block used, loose cable, or a dead sensor | Verify the port in the block matches the whisker's port; reseat the cable; bend the sensor by hand and observe the value |
| The value changes but the robot does nothing | Threshold never crossed, or the test is outside the loop | Read the live values and compare them with the threshold; verify the `if` statement is inside the forever loop |
| The robot reacts with nothing there | Threshold too close to resting value, or the whisker is mounted pre-bent | Recalibrate; remount the whisker so it sits neutral when untouched |
| The robot turns the wrong way | Left and right swapped in the logic, or the motors are wired opposite | Correct the logic first; if the behavior is completely mirrored, check the M1/M2 motor wiring |
| A sensor stopped working after handling | Bent the wrong way, or creased | Inspect for damage, replace the sensor, and reiterate the one-direction rule to students |
| Wall following oscillates | Turn response too strong, or speed too high | Reduce speed, soften the turn angle, or introduce a short delay between corrections |

## Comparing the robot and the animal

| In the animal | In the robot | The connection |
| :--- | :--- | :--- |
| The shaft bends on contact | The flex sensor bends on contact | Both convert physical deflection into a signal |
| Sensing happens at the follicle; the shaft is dead | The strip itself is the sensor, along its whole length | The robot differs at this point: see the note under The flex sensor |
| Left and right whiskers compared | Left and right thresholds compared | Both use bilateral information to determine direction |
| Turn away from the side touched | Contact on the left, turn right | The same behavioral rule, derived independently |
| Wall following by whisker contact | Wall following by threshold loop | Both maintain just enough contact to stay near the surface |
| An array of whiskers, dozens of them | Two, and no room for a third | The rat's spatial picture is built from many whiskers simultaneously; the robot has only left and right |

The final comparison deserves emphasis. The robot moves its entire body to bring its whiskers to objects. A rat, by contrast, moves its whiskers independently of its head, several times per second, and can therefore examine an object without approaching it. This represents a fundamental difference in capability, not merely degree, and it explains why the robot must physically contact a wall to learn of its presence.

## Common misconceptions

**"Whiskers feel at the tip."** The tip makes contact, but the sensing occurs at the follicle where the shaft bends. Consider it as a flexible lever: the tip touches the object, but the base measures the resulting deflection.

**"Better touch sensitivity means feeling things more intensely."** In the two-point discrimination task, better sensitivity means finer spatial resolution—the ability to distinguish two nearby touches as separate. It concerns precision, not strength.

**"Tonic means slow to respond."** Slow-adapting describes how long the receptor continues firing, not how quickly it begins. A slow-adapting receptor can respond instantly to initial contact.

**"Antennae are basically whiskers."** While antennae and whiskers perform similar functions (touch and movement sensing near the body), they are anatomically unrelated structures. The behaviors may be analogous, but the underlying biology differs.

**"The value goes up when the whisker bends more."** In this configuration, the opposite is true. Bending lowers the number mBlock reports. Always verify this by testing before writing control logic.

<!-- D: what is left on this chapter.

     1. The chapter has not been taught FROM. The activities themselves have been run with students -- that is where the module document and the whisker lab data came from -- but nobody has yet worked through this text as written and checked that its port numbers, thresholds, calibration steps and troubleshooting table match what a robot actually does.
     2. Required materials chapter entries beyond the whisker sensors, with quantities per group.
     3. A photograph of a robot with whiskers mounted. In TODO.md 5.0 as well, since it needs a robot in front of a camera.
     4. The standards section stays a placeholder for now, deliberately. -->
