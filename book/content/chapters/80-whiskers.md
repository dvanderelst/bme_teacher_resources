# Touch and Whiskers

## Materials

| Item | Description |
| :--- | :--- |
| mBot | The same robot as every other chapter. |
| Bluetooth Dongle | A dongle for connecting the robot to a computer. Currently the recommended connection method. |
| Whisker sensors | Two per robot for the obstacle avoidance challenge, one for wall following. Two is the ceiling: the block that reads them only offers two ports. Bring spares — these break. These are ours rather than Makeblock's — the same form factor as a Makeblock sensor, with a flex sensor as the active part — so they cannot be bought anywhere. Write to us for a set: the addresses are under [Questions, corrections, and help](#questions-corrections-and-help). Treat them as consumable: they are damaged by creasing, by bending the wrong way, and slowly by oxidation. |
| 3D printed brackets | Brackets for mounting sensors on the front of the robot in different orientations. |
| Lego compatible blocks | Blocks compatible with the robot's screw holes, giving students freedom in how they angle the whiskers. |
| Gaffer's tape | Versatile tape useful throughout the activities. |
| Extra cables (short) | Extra cables for connecting sensors, so students can add whiskers without unplugging what is already there. |
| Batteries | The robot requires 4 AA batteries. |
| Index cards or business cards | The backing for the two-point discrimination pokers. One per pair of students. |
| Toothpicks, or stiff plastic fibre | The points themselves, snapped in half and taped to the card. |
| Printed poker template | Printed from brainmapper.org and glued to the card; it sets the spacings. |
| Sticky tape | For fixing the points to the card. |
| Calipers | An alternative to the paper pokers, and what we normally use: set them to a spacing and poke with the tips of the jaws. |
| Cardboard strips | Taped to a whisker sensor to extend its reach past the flex sensor's own length, and to change how it bends. |
| Painter's tape | For attaching the cardboard. It comes off again without damaging the sensor. |
| Airtight box and desiccant | Where the whisker sensors live between lessons, lying flat. |

<!-- TODO: the whisker entries are in the Required materials chapter now, but the rest of this table is not, and that chapter still reads as a list of things to order when one line on it cannot be ordered. Worth a sentence at the top of it saying so, rather than leaving a teacher to find out at the bottom of a table. -->

## Prerequisites

Student knowledge: High school Biology and Algebra 2 or equivalent.

This lesson stands on its own, but it lands better after [Sonar](#sonar), which introduces active sensing in a form students have already seen, and after [Kinesis and Taxis](#kinesis-and-taxis), which gives them the vocabulary for the robot behaviour they will build here.

## Investigating / Essential Questions

How does an animal build a picture of its surroundings using only touch, and what changes when the sensor has to be moved to the object rather than pointed at it?

## Educational Standards

The educational standards applicable to this lesson are listed in the [Educational standards](#educational-standards) chapter.

<!-- TODO: the standards chapter now has a Touch and Whiskers section, but it is a placeholder saying the alignment is not written yet. Replace it with the real thing. -->

## Learning Objectives

1. Explain that touch is not a single sense, and that different receptors report different aspects of the same contact.
2. Measure tactile acuity and relate the result to receptor density and to cortical representation.
3. Understand that a whisker senses at its base, not along its length.
4. Explain why an animal moves its whiskers, and relate this to other forms of active sensing.
5. Calibrate a flex sensor and use it to drive a robot behaviour.

## Introduction

In this lesson students investigate touch: first their own, then a rat's, then a robot's. Touch is the sense that requires contact, and that constraint shapes everything about how animals use it. An eye or an ear can be pointed at something far away. A whisker has to be put on the object, which means the animal has to move — and moving the sensor to gather information is the thread that runs through this whole lesson.

The lesson has two parts. In Part 1 students measure the spatial acuity of their own skin, learn what the different receptors in it are for, and see how a rat solves the same problem with whiskers. In Part 2 they give a robot whiskers made from flex sensors, calibrate them, and choose one of two challenges to build.

## Part 1: Touch in animals

## Touch is not one sense

Ask students what touch tells them and they will say pressure. Their skin is doing considerably more than that. It contains several types of receptor, and they differ along two dimensions that between them explain most of what touch can and cannot do.

The first is **dynamics**. Phasic receptors respond to *change* — the moment of contact, the moment of release, vibration — and fall quiet during steady pressure. This is why you stop noticing your socks. Tonic receptors keep signalling for as long as the contact lasts.

The second is **receptive field size**, the patch of skin one receptor answers for. A small field means the brain learns precisely where the touch was. A large field covers more skin with fewer receptors, and localises poorly.

> **Note**
>
> "Slow adapting" is the usual term for a tonic receptor, and it misleads almost every student who meets it. It does not mean the receptor is slow to respond. A slow-adapting receptor can fire the instant it is touched. What is slow is how it *stops*.

## The four receptor types

| Receptor | Dynamics | Field and depth | What it gives you |
| :--- | :--- | :--- | :--- |
| Merkel disk | Tonic | Small, shallow | Fine spatial detail, edges, sustained touch. This is the one doing the work when you read Braille. |
| Meissner corpuscle | Phasic | Small, shallow | Light flutter and movement across the skin; low-frequency vibration. |
| Pacinian corpuscle | Very phasic | Large, deep | High-frequency vibration and brief pressure changes. Extremely sensitive. |
| Ruffini ending | Tonic | Large, deep | Skin stretch and lateral deformation; the shape your hand is currently in. |

The pattern is worth drawing out rather than leaving students to memorise four names. Small field plus tonic gives fine spatial detail. Small field plus phasic gives motion across the skin. Large field plus very phasic gives vibration. Large field plus tonic gives stretch. Each receptor is a different answer to the question of what is worth knowing about a contact, and no one of them does everything.

## Whiskers

### A whisker senses at its base

Nearly every mammal has whiskers. Humans are one of the few exceptions, and the reason is worth pausing on before students meet a rat: we investigate objects by handling them, with fingertips that have the finest spatial acuity on the body — which is exactly what they will have measured in Activity 1. An animal that cannot pick things up needs another way to feel them.

A whisker, or vibrissa, is a specialised hair — stiffer than fur, thicker at the base, tapered along its length, and slightly curved. Like any hair, the shaft itself is dead keratin with no nerves in it. Nothing is sensed along the whisker.

What matters is the follicle at the base, which is wrapped in mechanoreceptors and is among the most densely innervated structures in a mammal's skin. The shaft is a lever. When its tip meets an object the whisker bends, the bend puts forces and torques into the follicle, and those are what the animal actually measures.

The shaft is not a uniform rod, either. It tapers, so it is thick and stiff where it leaves the skin and thin and flexible near the tip — which means that on contact it barely bends at the base and bends a great deal at the far end. That flexibility at the tip is thought to be part of how animals read texture.

The tip touches. The base senses. Students find this genuinely surprising, and it is the single most useful fact in the lesson, because it is also exactly how the robot's whisker will work.

From the follicle, superficial and deep vibrissal nerves carry the signal away, join to form the infraorbital nerve, and reach the brain through the trigeminal — the same nerve that serves the rest of the face. The orderly grid on the snout is then preserved the whole way up: as barrelettes in the brainstem, barreloids in the thalamus, and finally the barrels in the cortex. A single whisker can be followed from the hair to a cluster of cells, which is why this system became a workhorse of sensory neuroscience.

An array matters as much as an individual whisker. A rat has some fifty of them, in a stereotyped pattern of five rows that is consistent enough between animals that individual whiskers can be identified and named. Different whiskers bend differently against the same object, so what the animal gets is a spatial pattern of deflections rather than one yes-or-no signal. The brain reflects the investment: in the somatosensory cortex each whisker has its own cluster of cells, called a barrel, and the barrels are laid out in the same arrangement as the whiskers on the face.

### Whisking is active sensing

Many rodents do not hold their whiskers still. Rats and mice sweep them forward and back — whisking — and change the sweep depending on what they are doing: short, fast sweeps to examine a surface closely, wider ones to explore open space. The animal chooses where and when to touch.

The rates are quicker than students expect. An opossum whisks at about 5 Hz, a rat at 8 Hz, a mouse at up to 25 Hz. None of that is being decided moment by moment: the rhythm comes from a pattern generator in the brainstem, in the same way walking does, and what the animal steers is the sweep rather than each individual stroke.

The mechanism is worth following carefully, because the obvious guess about it is wrong. Each follicle is wrapped in a muscular sling, anchored *behind* it. When the sling contracts it hauls the deep end of the follicle backwards — and since the follicle pivots about a point close to the skin surface, the length of whisker outside the skin swings the other way, forwards. The muscle pulls back so that the whisker can point forward.

One more thing about those slings: each one serves a whole row of follicles, so all the whiskers in a row move together rather than independently.

That sounds like a limitation and turns out to be an elegant piece of engineering. Fifty whiskers, each on its own follicle of a different length and at a different spacing, ought to need fifty separately controlled muscles and some way of keeping them in step. Instead, contracting every intrinsic muscle by the same *percentage* sweeps every whisker through the same *angle* — the geometry of the array does the synchronising, so the animal has one thing to command rather than fifty. Engineers reach for the same trick: rather than driving a car's two windscreen wipers with two motors and a controller to keep them together, you link them with a four-bar mechanism and let the linkage guarantee it.

There is a second consequence, and it is the one worth showing students. As the whiskers sweep forward, their tips converge — the same array covers a smaller patch of space, so the sampling gets denser exactly where the animal is about to touch something. It has been called *foveal whisking*, by analogy with the fovea in the eye, though the better analogy is a microscope: turning the zoom knob shrinks the field of view and concentrates the detail. The rat can do this on demand, which the retina's fixed geometry cannot.

![How a whisker is moved, and where it is sensed. **A**, the muscle is relaxed and the whisker lies back. **B**, the muscle contracts, pulls on the follicle, and swings the whisker forward; repeating that cycle is whisking. **C**, the whisker runs into something. The dashed line is where it would have carried on had the obstacle not been there. Note where the bending happens: a whisker tapers, so it is stiffest at the base and most flexible near the tip, and the shaft therefore leaves the follicle almost straight and does its bending out at the far end, which curls away from the obstacle. But that far end is dead keratin with no nerves in it, so nothing is sensed where the contact actually happened. The mechanoreceptors are clustered around the follicle at the base, and the bend is what they measure. Schematic, and not to scale.](images/touch-and-whiskers-follicle.png)

[Rat whiskers moving, with the movement of the head subtracted](https://www.youtube.com/watch?v=d7rSsMZyThQ) — watch the left panel. Taking the head motion out is what makes the point: what is left is the whiskers being *aimed*, independently of where the animal is walking.

This is the same idea as the [Sonar](#sonar) lesson in a different medium. A bat decides when to call and what to call, and so decides what its next echo will be about. A rat decides where its whiskers go, and so decides what its next contact will be about. In both cases the animal is not a passive receiver, and that control is much of what makes the sense useful.

The difference is range. A bat's decision reaches metres; a rat's reaches perhaps three centimetres. Everything else about whiskers follows from that number.

### Animals that rely on whiskers

**Rats and mice** use whiskers as a primary sense. They judge the width of a gap before entering it, tell rough surfaces from smooth, and locate objects relative to their own head — in the dark, in burrows, where vision has nothing to work with.

**Seals** use them in water. A harbour seal can follow the hydrodynamic trail left by a swimming fish: the disturbed water in its wake, which persists for many seconds. A seal with its eyes and ears covered can pick up such a trail and follow the fish's path. Seal whiskers are not smooth cylinders but wavy, undulating along their length, and this shape suppresses the vortices the whisker would otherwise shed as the seal swims. A smooth whisker would vibrate in its own wake and drown out the signal. The undulation is noise cancellation built into the shape of a hair.

The investment in the sense shows in the wiring: aquatic mammals have roughly ten times as many nerve endings around a whisker follicle as land mammals do.

Seals whisk as well, and recent work suggests why they bother. A whisker held forward is the more sensitive arrangement, but holding it there costs continuous muscular effort. Rather than pay that all the time, the seal keeps its whiskers back and sweeps them rhythmically instead — buying most of the sensitivity for a fraction of the energy. It is a trade-off students can appreciate directly, and the same one an engineer makes when deciding how often to poll a sensor.

[Harbour seal whiskers, in three minutes](https://www.youtube.com/watch?v=-ozBE6f3hrE) — the anatomy, then the undulated shape, then the experiment itself: a blindfolded seal following the wake of a small remote-controlled submarine using nothing but touch.

> **Note**
>
> Insect antennae do a similar job — touch and movement sensing, close to the body — and students often propose them as the same thing. They are not: antennae and vibrissae are completely different structures anatomically. The behaviour rhymes; the anatomy does not. It is a useful analogy as long as it is labelled as one.

## Activity 1: Two-point discrimination

How close together can two touches be before your skin reports them as one? The smallest spacing you can still tell apart is the **threshold** for that patch of skin, and it varies across the body by more than an order of magnitude.

The activity follows the protocol published at [brainmapper.org](https://brainmapper.org), an outreach project from the Max Planck Florida Institute for Neuroscience, which also provides the tool that turns the class's numbers into a homunculus.

### Two ways to make the points

**Calipers** are the simpler option and the one we use. Set them to a spacing, read it off the scale, and poke with the tips of the two jaws. One pair per group is enough, the spacing is exact, and changing it takes a second.

**Paper pokers** are brainmapper's own method, and the answer for a class without enough calipers. Print the template from the site, glue it to an index card or a business card, and tape a pair of points to each marked spacing — toothpicks snapped in half work, as does stiff plastic fibre — so the points overhang the edge of the card by about half an inch. Each card then carries a fixed set of spacings, which is slower to work through but means every group is testing the same distances.

> **Tip**
>
> Whichever you use, the two points must be level with each other. If one sits proud of the other it lands first, and the subject answers using the timing rather than the spacing. This is worth checking on calipers as well as on cards — jaws that are worn or bent do it too.

### Procedure

One student is the tester, one the subject. The subject closes their eyes and keeps them closed. The tester presses both points against the skin at the same instant and asks: one point, or two?

Start at the widest spacing, 60 mm, and work down. Continue until the subject reports feeling only one point, and record **that** distance — the first spacing that felt like one. If the subject still reports two points at the smallest spacing on the card, record the smallest distance tested.

> **Note**
>
> Recording the first distance that felt like *one* point is brainmapper's convention, not an arbitrary choice: it is what the site's dropdowns expect. Recording the last distance that felt like two — the other obvious way round — will put every value one step out and distort the homunculus.

Six sites are tested, and these are the six the site asks for: forehead, back, arm, palm of the hand, leg, and foot.

> **Tip**
>
> Three things ruin this measurement, and all three are easy to avoid once named:
>
> **Apply both points at the same instant.** If one lands before the other, the subject can use the timing rather than the spacing, and will score far better than their skin deserves.
>
> **Keep the pressure gentle and the same every time.** Pressing harder changes the answer.
>
> **Test the same spot each time.** Receptor density varies within a body region, not just between regions, so wandering across the forearm between trials measures several different patches of skin and averages them.
>
> If it hurts, it has stopped being a discrimination task and become a pain task. Blunt points, light pressure.

### Interpreting the results

A lower threshold means finer spatial acuity: more receptors per unit area, with smaller receptive fields. The palm and the forehead usually do far better than the back, the leg, or the arm — though the exact ranking varies between people and between testers, and variation across the class is a result rather than a mistake.

Students reliably read the result backwards, so it is worth saying explicitly: a lower threshold does not mean the touch feels *stronger* there. It means the brain can tell two nearby touches *apart*. Precision, not intensity.

### The homunculus

The six distances go into the dropdown boxes at [brainmapper.org/experiment](https://brainmapper.org/experiment), which draws a cortical homunculus from them — a figure whose body parts are scaled by how much cortex is devoted to them rather than by their actual size. The hands and face are enormous, the back and legs barely there. The site says the whole thing takes about ten minutes, which is roughly right once the pokers are made.

The point to land is that the distortion is the class's own data made visible. The brain allocates cortex in proportion to acuity, not area, which is why the map of the body inside the head is not shaped like the body.

![The sensory homunculus: a human body redrawn with each part scaled to the amount of cortex devoted to feeling it rather than to its actual size. The hands, lips and tongue dominate; the trunk and legs almost disappear. This is the same shape a class's own two-point measurements produce. Photograph by Wikimedia Commons user Mpj29, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).](images/touch-and-whiskers-homunculus.png)

## Part 2: Giving the robot whiskers

Students often find the idea odd — whiskers belong on animals, and a robot has cameras. It is worth saying at the outset that mechanical whiskers are not a novelty borrowed from biology for this lesson. They are among the oldest sensors in robotics, for the same reasons they are useful to a rat: a wire and a switch are cheap, they need almost no computation, and they report an obstacle that is already touching you.

Rodney Brooks's *Genghis*, a six-legged walking robot built at MIT around 1991, is the standard example. It navigated rough ground with a set of simple behaviours layered on top of each other, and one of those layers was called, plainly, "whiskers".

The case for them is not only that they are cheap. A whisker works where the sensors we usually reach for do not. Vision needs light, and a robot in a pipe, a burrow, a collapsed building or an unlit room has none. Sonar and cameras both struggle in dust and smoke. Under any of those conditions, feeling your way is not a poor substitute for looking — it is the sensible thing to do, which is exactly why the animals that live in the dark evolved whiskers rather than better eyes.

There is a second motivation, which turns the lesson around. Building a robot with whiskers is also a way of *studying* whiskers: a physical model whose parameters you can change, and which tells you something about the animal when it fails. Pearson and colleagues make both arguments, and their review is the place to send a teacher who wants more than this chapter has room for.

> Pearson, M. J., Mitchinson, B., Sullivan, J. C., Pipe, A. G., and Prescott, T. J. (2011). Biomimetic vibrissal sensing for robots. *Philosophical Transactions of the Royal Society B* **366**(1581), 3085–3096. [doi:10.1098/rstb.2011.0164](https://doi.org/10.1098/rstb.2011.0164). Not open access.

Their robot is worth showing before students build anything of their own.

[Shrewbot: shrew whiskers inspire robot design](https://www.youtube.com/watch?v=oRgE3-niJSI)

Shrewbot's whiskers are *active*: they sweep back and forth rather than sitting still, which is whisking done in hardware. Ask students to watch the head rather than the whiskers. When the robot touches something, it turns its head to bring the sweeping whiskers onto the object and go over it again — it is not waiting to be touched, it is deciding where to touch next, and that is the whole of active sensing in one movement.

It is also the thing the robot in this lesson cannot do. Our whiskers are bolted to the chassis, so the only way to aim them is to drive the whole robot. Worth planting now, because the point comes back at the end of the chapter.

## The flex sensor

The robot's whisker is a flex sensor: a thin strip whose electrical resistance changes as it bends. Flat, it is about 10 kΩ; bending raises the resistance. Mounted so that it projects forward and to the side, it meets an obstacle tip-first and bends, and the bending is what the robot reads.

This makes it a far better model of a whisker than a switch would be. A switch reports contact or no contact. A flex sensor reports *how much* it is bent — a graded measure of deflection, which is much closer to what the follicle gives the animal than a yes-or-no would be.

> **Note**
>
> There is one place where the copy is not a copy, and it is worth pointing out rather than glossing over, because it is the sort of thing a sharp student notices.
>
> An animal's whisker senses nothing along its length. The shaft is dead, and every receptor sits at the base. The flex sensor is the other way round: the strip *is* the sensing element, and it responds to bending anywhere along itself. The robot's whisker is sensitive along its whole length; the rat's is sensitive at one end only.
>
> What the two share is the thing that matters for this lesson — a slender probe that deflects on contact, and a deflection converted into a signal. Where they differ, the robot is arguably doing the easier thing.

![A whisker sensor. The board is the same shape as a Makeblock sensor and plugs into an RJ25 port like one, but the board is ours and the working part is the flex sensor clamped to the front of it. The segmented side facing up here is the metallic side: the whisker bends away from it, and bending it the other way is what ruins the sensor.](images/touch-and-whiskers-sensor.png)

> **Warning**
>
> Flex sensors are fragile in specific ways, and a class will destroy them if not told.
>
> They bend in **one direction only** — away from the metallic side. Bent the other way, they are damaged.
>
> They must not be **creased or sharply folded**. A crease is permanent and the sensor is finished.
>
> Mount so the bending region is free to flex, and do not tape over it. Seat the connector fully and provide strain relief, so the sensor is not worked at the plug every time the robot moves.
>
> **Between lessons they live flat, in an airtight box with a desiccant sachet.** The metallic layer oxidises, and a set left in a drawer over a summer will read differently, or not at all. This one is invisible until it has already happened.

### Making the whisker longer

The flex sensor is only about 10 cm long, which is a short whisker for a robot the size of an mBot: it detects the wall at the moment the robot has more or less arrived at it.

Reach is extended by taping a strip of cardboard to the end of the sensor with painter's tape — painter's tape because it peels off again without taking the sensor with it. The cardboard does no sensing, so bending happens only in the 10 cm that can bend, but the robot now meets obstacles further out and has time to react.

This is worth pointing out to students rather than doing for them, because it accidentally rebuilds the animal's arrangement. A cardboard extension is a dead length of whisker that transmits force back to a sensing region nearer the base — which is what a vibrissa is. The trick is also the tuning knob for the whole activity: how long the cardboard is, how stiff it is, and where it is taped all change how the whisker bends and therefore how early and how strongly the robot reacts. Groups that fiddle with this get better robots than groups that do not.

## Reading a whisker in mBlock

A whisker plugs into an RJ25 port and is read with the **`light sensor [port] light intensity`** block, choosing the whisker's port from the block's dropdown. Not the sonar block, not the line follower block. That block lives in the same light-and-sound extension as the sound sensor blocks, so if you have run the sound localization lesson it is already installed; if not, add the extension in mBlock first or the block will not be there to find.

The block offers **ports 3 and 4** and no others, so those are the two the whiskers go in. One whisker can use either. Two whiskers use both, and that is the robot's limit.

> **Note**
>
> Do not read too much into the block being called *light sensor*. The whisker is not measuring light. Both sensors happen to work by changing their resistance, and this block reads whatever resistance is on the port and reports a number — the label reflects what the block was written for, not what is plugged into it. The only consequence for the lesson is the one above: the whisker inherits the light sensor's ports.

> **Note**
>
Here is the whole of reading two whiskers. It does nothing with the numbers yet; it simply puts each whisker into a variable, once per loop, so that everything afterwards can talk about `whisker1` and `whisker2` rather than repeating the sensor block.

![The smallest useful whisker program: read each whisker into a variable, forever. Port 3 and port 4 are the only two the light sensor block offers, so a two-whisker robot uses both. Naming the variables is not decoration — every program later in this chapter is written in terms of them, and a threshold comparison is far easier to debug when the reading has a name.](images/touch-and-whiskers-read-two.png)

[Open the mBlock project](https://planet.mblock.cc/project/8233113).

Run this and watch the variables on the stage while bending each whisker by hand. That is also the calibration step below, done informally: you are reading off the resting value and the bent value before deciding anything.

> **Note**
>
> The value **goes down** when the whisker bends. This is the opposite of what you might expect, students and teachers alike, and it is correct: bending the sensor reduces the number mBlock reports. An unbent whisker reads somewhere around 400, and bending it takes the reading down from there.
>
> *Around* 400, because whiskers vary. Two sensors sitting untouched on the same robot will not report the same number, which is why each one is calibrated separately and why left and right get their own thresholds. A threshold copied from another group's robot, or from another whisker on the same robot, will not work.
>
> The rule to teach is a general one, worth more than the specific fact: trust what you measure, not what you assume the sensor ought to do. Bend the whisker by hand and watch the number before writing a single line of behaviour.

## Calibration

Nothing in Part 2 works until this is done, and it must be redone for every whisker. Resting values sit near 400 but vary from sensor to sensor, so the numbers a group needs are the ones their own robot reports, not the ones in this book. A threshold goes *below* the resting reading it was measured from, since bending drives the value down — which is why the example program's thresholds of 400 and 375 sit where they do.

| Step | What to do |
| :--- | :--- |
| 1. Read resting values | With nothing touching the whiskers, note the left and right values separately. |
| 2. Read bent values | Gently bend each whisker as it would bend against an obstacle, and note the value. |
| 3. Choose a threshold | Pick a number between resting and bent, for each whisker independently. The left and right thresholds do not need to match, and usually will not. |
| 4. Test slowly | Run the robot at low speed first. Logic errors are easier to see, and a slow robot is less likely to break a whisker against a wall. |
| 5. Refine from behaviour | Reacting too late means the threshold is too close to the bent value. Reacting constantly with nothing there means it is too close to the resting value, or the whisker is not sitting neutral. |

## Activity 3: Choose a challenge

Students pick **one** of the two challenges below. There is no required order and neither is the correct answer; they are different problems that happen to use the same hardware.

| Challenge | Goal | Whiskers needed |
| :--- | :--- | :--- |
| Avoid obstacles | Drive around without bumping into things | Two, left and right |
| Follow a wall | Keep one whisker lightly touching a wall without crashing into it | One is enough |

### Challenge 1: Avoiding obstacles

Contact on one side should push the robot away from that side — the direct biomimetic link, and the same rule the rat uses.

| Condition | Action |
| :--- | :--- |
| Neither whisker bent | Drive forward |
| Left whisker bent | Turn right |
| Right whisker bent | Turn left |
| Both whiskers bent | Back up briefly, then turn to escape |

Remembering that a bent whisker reads *below* its threshold:

```text
If left > threshold and right > threshold: forward
If left < threshold and right < threshold: reverse briefly, then turn
If left < threshold: turn right
If right < threshold: turn left
```

Keeping the left and right readings in separate variables with obvious names makes this far easier to debug than nesting the comparisons.

A worked version, building straight on the reading program from earlier:

![One way to write the obstacle avoidance challenge. The two thresholds are set once at the start and then never mentioned again, which is what makes this program easy to retune: a robot reacting too late or too eagerly is fixed by editing two numbers at the top rather than hunting through the logic. Note that the two thresholds are different — they belong to two different whiskers, and there is no reason two sensors should agree.](images/touch-and-whiskers-avoid-obstacles.png)

[Open the mBlock project](https://planet.mblock.cc/project/8233137).

<!-- TODO: mirrors. Every other robot activity in the book pairs its planet.mblock.cc link with a copy in content/files/programs/, because some school networks block the Makeblock site, and check-links.py counts the two and complains when they do not match -- it is complaining now. Export both projects from the IDE and drop them in as whisker_read.mblock and whisker_obstacle_avoidance.mblock, then add the usual "If your school blocks the Makeblock site, download ... instead" sentence to both. -->


### Challenge 2: Following a wall

Keep one whisker just barely in contact with the wall. Lose contact, turn slightly towards it; bend too far, turn slightly away.

```text
If the value is at or near resting (contact lost): turn slightly toward the wall
If the value is below threshold (bending too much): turn slightly away
Otherwise: drive forward
```

This is a different kind of program from the first challenge, and the difference is worth naming for students. Obstacle avoidance reacts to an event. Wall following runs a continuous feedback loop, making small corrections against a target it never quite settles on — which is much closer to how an animal actually uses a whisker, and also why it is the harder of the two to tune.

## Troubleshooting

| Problem | Likely cause | What to try |
| :--- | :--- | :--- |
| The value never changes | Wrong port, wrong block, loose cable, or a dead sensor | Check the port in the block matches the port the whisker is in; reseat the cable; bend the sensor by hand and watch |
| The value changes but the robot does nothing | Threshold never crossed, or the test is outside the loop | Read the live values and compare them with the threshold; check the `if` is inside the forever loop |
| The robot reacts with nothing there | Threshold too close to resting, or the whisker is mounted pre-bent | Recalibrate; remount so the whisker sits neutral when untouched |
| The robot turns the wrong way | Left and right swapped in the logic, or the motors wired opposite | Fix the logic first; if everything is mirrored, check the M1/M2 wiring |
| A sensor stopped working after handling | Bent the wrong way, or creased | Inspect for damage, replace, and re-teach the one-direction rule |
| Wall following oscillates | Turn response too strong, or speed too high | Slow down, soften the turn, or put a short delay between corrections |

## Comparing the robot and the animal

| In the animal | In the robot | The connection |
| :--- | :--- | :--- |
| The shaft bends on contact | The flex sensor bends on contact | Both turn a physical deflection into a signal |
| Sensing happens at the follicle; the shaft is dead | The strip itself is the sensor, along its whole length | The one place the robot is *not* a copy — see the note under The flex sensor |
| Left and right whiskers compared | Left and right thresholds compared | Both use two sides to decide which way to go |
| Turn away from the side touched | Contact on the left, turn right | The same rule, arrived at independently |
| Wall following by whisker contact | Wall following by threshold loop | Both keep just enough contact to stay near the surface |
| An array of whiskers, dozens of them | Two, and no room for a third | Where the comparison runs out: the rat's spatial picture is built from many whiskers at once, and the robot has left and right |
| Whisking | The robot moving through space | Both gather information by moving the sensor |

The last row is the one to dwell on. The robot moves its whole body to bring its whiskers to things. A rat moves its whiskers independently of its head, several times a second, and can therefore examine something without going to it. That is a difference in capability, not just in degree — and it is the reason the robot has to drive into a wall to learn the wall is there.

## Common misconceptions

**"Whiskers feel at the tip."** The tip makes contact, but the sensing is at the follicle where the shaft bends. Think of it as a flexible lever: the tip touches the object, the base measures what happened.

**"Better touch sensitivity means feeling things more intensely."** In the two-point task, better means finer spatial resolution — telling two nearby touches apart. It is about precision, not strength.

**"Tonic means slow to respond."** Slow-adapting describes how long the receptor keeps firing, not how quickly it starts.

**"Antennae are basically whiskers."** Behaviourally similar in places, anatomically unrelated.

**"The value goes up when the whisker bends more."** Not in this setup. Bending lowers the number mBlock reports. Measure it and see.

<!-- D: what is left on this chapter.

     1. The chapter has not been taught FROM. The activities themselves have been run with students -- that is where the module document and the whisker lab data came from -- but nobody has yet worked through this text as written and checked that its port numbers, thresholds, calibration steps and troubleshooting table match what a robot actually does. That is the difference between the activities being tested and the chapter being tested.
     2. The two .mblock mirrors, which check-links.py reports on every build. planet.mblock.cc does not serve the files over a plain URL; they have to be exported from the IDE.
     3. Required materials chapter entries beyond the whisker sensors, with quantities per group.
     4. A photograph of a robot with whiskers mounted. In TODO.md as well, since it needs a robot in front of a camera.
     5. The standards section stays a placeholder for now, deliberately.

     Settled: the resting reading is about 400, not 300. The homunculus photograph stays as it is, uncropped, which also keeps it clear of ShareAlike. -->
