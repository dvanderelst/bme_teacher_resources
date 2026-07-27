---
chapter: "Block reference"
source: 57-block-reference.md
edition: "27 July 2026"
fingerprint: "677bb65-stale"
---

# Block reference

This chapter lists the programming blocks available for the mBot (mCore) board in mBlock, with what each one does. It is a lookup chapter rather than one to read through; Programming the robot introduces the categories and shows how the blocks fit together.

**What is not listed here.** `Looks` (relevant only if the robot has an add-on LCD display), `My blocks` (custom blocks you define yourself), and the sprite and stage categories that belong to mBlock rather than to the robot. These exist in the palette, but none of the lessons in these materials use them.

**Before any of these blocks appear.** The robot's blocks are only in the palette once the mBot has been added in the devices panel. On a fresh start the device is not there and only the sprite and stage categories are shown. See Adding the mBot to mBlock.

**Extensions.** Two categories require an extension, added with the `+` button at the bottom of the category panel. Opening one of the supplied example programs loads the relevant extension automatically.

| Extension | Adds | Needed for |
| :--- | :--- | :--- |
| `color sensor` | Colour Sensor category | Color Vision lesson |
| `light sound` | Light & Sound category (external sound and light sensors, RGB LED module) | Sound Localization lesson, programming challenge 3 |

**Ports.** Where a block's dropdown restricts which ports it offers, that restriction is noted with the block. For which sensor may be plugged into which port and why, see Ports and sensor compatibility.

## Block shapes

A block's shape says how it can be used, and the shapes are worth recognising because they determine where a block will and will not snap into place.

| Shape | Marked here as | Behaviour |
| :--- | :--- | :--- |
| Stack | *(untagged)* | Does something and passes control to the next block. The default. |
| Reporter | **Reporter** | Rounded. Returns a value. Cannot be used on its own — it must be dropped into a slot on another block. |
| Boolean | **Boolean** | Hexagonal. Returns true or false. Drops into the hexagonal slots of `if`, `while`, `wait until` and the logic operators. |
| Hat | **Hat** | Rounded top. Starts a script. Goes at the top of a stack, never inside one. |

Reporter and Boolean blocks are the ones teachers most often try to use alone. A `timer` block sitting by itself in the program area does nothing; it has to go inside something that asks for a value.

In the signatures below, `(n)` is a slot you type a value into (or drop a reporter block into), `[option ▾]` is a dropdown, `[color]` is a colour picker, and `<>` is a hexagonal slot that takes a Boolean block.

---

## Action blocks

Controls the two drive motors. There are two forms, and the difference matters: **timed** blocks run the motors for the stated time and only then hand control to the next block, while **non-timed** blocks start the motors and continue to the next block immediately, leaving them running.

### Timed movement

`move forward at power (n)% for (n) secs`

:   Drives both motors forward at the given power (0–100%) for the given number of seconds, then stops them and continues.

`move backward at power (n)% for (n) secs`

:   As above, in reverse.

`turn left at power (n)% for (n) secs`

:   Turns the robot left at the given power for the given time, then stops and continues.

`turn right at power (n)% for (n) secs`

:   As above, to the right.

### Non-timed movement

`move [move forward ▾] at power (n)%`

:   Starts the motors in the chosen direction at the given power and continues to the next block immediately. The motors keep running until a `stop moving` block or another Action block changes them. Dropdown: `move forward`, `move backward`, `turn left`, `turn right`.

`left wheel turns at power (n)%, right wheel at power (n)%`

:   Sets each motor's power independently (0–100% each) and continues immediately. Used for curves, and for correcting a robot that drifts when it should run straight.

`stop moving`

:   Stops both motors immediately.

---

## Show blocks

Controls the two onboard RGB LEDs and the onboard buzzer. The two LEDs are addressed as `left`, `right` or `all`.

`LED [all ▾] shows color [color] for (n) secs`

:   Lights the selected LED(s) in the chosen colour, holds the program for the given time, then switches them off and continues. First dropdown: `all`, `left`, `right`. The colour slot opens a picker with separate colour, saturation and brightness controls.

`LED [all ▾] shows color [color]`

:   Sets the selected LED(s) to the chosen colour and continues immediately. The colour stays until something changes it.

`turn on [all ▾] light with color red (n) green (n) blue (n)`

:   Sets the selected LED(s) from explicit red, green and blue values (0–255 each) and continues immediately. The form to use when the colour is calculated rather than picked, since the three slots accept reporter blocks. Red 0, green 0, blue 0 switches the LED off.

`play note [C4 ▾] for (n) beats`

:   Plays a named musical note on the onboard buzzer for the given number of beats, holding the program for that time. The dropdown spans `C2` to `D8`, about six and a half octaves; `C4` is middle C.

`play sound at frequency of (n) Hz for (n) secs`

:   Plays a tone at the given frequency in Hz for the given number of seconds, holding the program for that time.

There is no dedicated "off" block for the LEDs. Set the colour to black in the picker, or use red 0, green 0, blue 0.

---

## Sensing blocks

The onboard sensors and the sensors in the robot's default configuration. The external sound sensor and the RGB LED module are in the Light & Sound extension.

`ultrasonic sensor [port ▾] distance(cm)`

:   **Reporter.** Distance in centimetres from the sonar sensor on the selected port to whatever is in front of it. Any of the four ports.

`light sensor [on-board ▾] light intensity`

:   **Reporter.** Ambient light level, higher values meaning more light. The onboard sensor reads roughly 0–1000. Dropdown: `port3`, `port4`, `on-board` — so this block reads an external light sensor as well as the onboard one, and like the sound sensor it is limited to the two analog ports.

`line follower sensor [port ▾] value`

:   **Reporter.** Reads the line-follower sensor's two sub-sensors as a single number. See Reading the line follower value below.

`line follower sensor [port ▾] detects [leftside ▾] being [black ▾] ?`

:   **Boolean.** True when the chosen side of the line-follower sensor sees the chosen surface colour. A per-sub-sensor alternative to reading the combined value.

`when on-board button [pressed ▾] ?`

:   **Boolean.** True when the onboard button is in the chosen state at the moment the block is evaluated. Dropdown: `pressed`, `released`.

`IR remote [A ▾] pressed?`

:   **Boolean.** True while the named button on an infrared remote is being pressed.

`send IR message (text)`

:   Transmits a message from the board's infrared transmitter.

`IR message received`

:   **Reporter.** The most recent message picked up by the board's infrared receiver.

`timer`

:   **Reporter.** Seconds the robot has been running. The timer starts from zero each time the robot is powered on — not when the program starts — and `reset timer` returns it to zero.

`reset timer`

:   Sets the timer back to zero.

### Reading the line follower value

The sensor has two sub-sensors that each emit infrared light and detect what comes back. A pale, reflective surface returns a signal; a dark line absorbs it and returns none. The reported value encodes which of the two received a signal:

| Value | Sub-sensor 1 (left) | Sub-sensor 2 (right) | Position | Correction |
| :--- | :--- | :--- | :--- | :--- |
| 0 | no signal — over the line | no signal — over the line | both on the line | none |
| 1 | no signal — over the line | signal — off the line | drifted right | turn left |
| 2 | signal — off the line | no signal — over the line | drifted left | turn right |
| 3 | signal — off the line | signal — off the line | line lost | search |

Note that `0` means *both sub-sensors are on the line*, not that nothing was detected, and `3` means the line has been lost entirely. Students frequently assume the reverse.

The left and right readings assume the sensor is mounted in the normal orientation, with sub-sensor 1 on the left. The interpretation also assumes the usual track, a dark line on a pale background; on a pale line over a dark background every value inverts.

---

## Events blocks

Where a program starts. The choice between the first two is the choice between the robot's two operating modes; see Live versus Upload mode.

`when [green flag] clicked`

:   **Hat.** Starts the script when the green flag is clicked. The program runs on the computer and drives the robot over the live connection (Live mode). Used throughout these materials except in the Color Vision lesson.

`when mBot(mcore) starts up`

:   **Hat.** Starts the script when the robot is switched on, running the program from the robot's own memory (Upload mode). The program has to be uploaded over USB first; the cable can then be disconnected.

`when on-board button [pressed ▾]`

:   **Hat.** Starts the script when the onboard button is pressed.

`when [space ▾] key pressed`

:   **Hat.** Starts the script when the chosen key is pressed on the computer's keyboard. Live mode only.

`when I receive [message ▾]`

:   **Hat.** Starts the script when the named broadcast message is sent.

`broadcast [message ▾]`

:   Sends the named message and continues immediately.

`broadcast [message ▾] and wait`

:   Sends the named message and waits until every script it started has finished.

---

## Control blocks

`forever`

:   Repeats the enclosed blocks indefinitely. Never exits on its own.

`wait (n) seconds`

:   Pauses the script for the given time.

`if <> then`

:   Runs the enclosed blocks once if the condition is true.

`if <> then / else`

:   Runs the first group of blocks if the condition is true, the second group otherwise. It sits directly below `if ... then` in the palette and the two look almost identical in the list, so it is easily missed.

`while <> repeat`

:   Repeats the enclosed blocks for as long as the condition stays true.

`repeat until <>`

:   Repeats the enclosed blocks until the condition becomes true.

`repeat (n)`

:   Repeats the enclosed blocks a fixed number of times.

`count with [i ▾] from (n) to (n) by step (n) repeat`

:   Repeats the enclosed blocks while counting a variable from a start value to an end value in fixed steps. The counter is available inside the loop.

`wait until <>`

:   Pauses the script until the condition becomes true.

`break`

:   Exits the enclosing loop immediately.

`continue`

:   Skips the rest of the current pass through the loop and starts the next one.

`stop [all ▾]`

:   Stops running scripts; the dropdown selects which. This stops the *program*, not the motors — a robot whose motors were started by a non-timed Action block keeps driving, so pair this with `stop moving`.

---

## Operator blocks

`(n) + (n)`

:   **Reporter.** Adds two values.

`(n) - (n)`

:   **Reporter.** Subtracts the second value from the first.

`(n) * (n)`

:   **Reporter.** Multiplies two values.

`(n) / (n)`

:   **Reporter.** Divides the first value by the second.

`pick random (n) to (n)`

:   **Reporter.** A random whole number between the two values, inclusive.

`(n) > (n)`

:   **Boolean.** True if the first value is greater than the second.

`(n) < (n)`

:   **Boolean.** True if the first value is less than the second.

`(n) = (n)`

:   **Boolean.** True if the two values are equal. Reliable against the small whole numbers the line follower returns; unreliable against a continuously varying reading, which rarely lands on an exact value.

`<> and <>`

:   **Boolean.** True only if both conditions are true.

`<> or <>`

:   **Boolean.** True if either condition is true.

`not <>`

:   **Boolean.** Inverts a condition.

`[abs ▾] of (n)`

:   **Reporter.** Applies the selected mathematical function to a value. Dropdown: `abs`, `floor`, `ceiling`, `sqrt`, `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `ln`, `log`, `exp`, `10^`. Because the function is hidden behind a dropdown, no block in the palette is visibly named "abs", which is why it is hard to find.

`(n) mod (n)`

:   **Reporter.** The remainder after dividing the first value by the second.

`round (n)`

:   **Reporter.** Rounds a value to the nearest whole number.

`join (text) (text)`

:   **Reporter.** Joins two pieces of text.

`letter (n) of (text)`

:   **Reporter.** The character at the given position in a piece of text.

`length of (text)`

:   **Reporter.** The number of characters in a piece of text.

`(text) contains (text) ?`

:   **Boolean.** True if the first piece of text contains the second.

---

## Variables

The category holds only `Make a Variable` until the first variable is created; the blocks below appear once one exists. See Working with variables in mBlock.

`set [variable] to (n)`

:   Puts a value in the variable. The slot takes a typed value, a reporter block, or an expression built from operator blocks.

`change [variable] by (n)`

:   Adds the given amount to the variable's current value.

`[variable]`

:   **Reporter.** The variable's current value.

Every variable a program creates is displayed on the stage, the white area at the top left of the mBlock window.

---

## Extension: Colour Sensor

Requires the `color sensor` extension. The colour sensor works in Upload mode only, so programs using it start from `when mBot(mcore) starts up`.

`color sensor [port ▾] [R ▾] value`

:   **Reporter.** The amount of light the sensor detects in one channel. Channel dropdown: `R`, `G`, `B`.

`color sensor [port ▾] detects [white ▾]`

:   **Boolean.** True when the sensor classifies what it sees as the named colour. Dropdown: `white`, `red`, `yellow`, `green`, `blue`, `black`.

`color sensor [port ▾] set fill light LED to [on ▾]`

:   Switches the sensor's own white illumination LEDs on or off. Dropdown: `on`, `off`. These LEDs give the surface uniform broad-spectrum light, which is what makes colour discrimination reliable.

---

## Extension: Light & Sound

Requires the `light sound` extension.

`sound sensor [port ▾] loudness`

:   **Reporter.** The current sound level at an external Makeblock sound sensor, higher values meaning louder. Dropdown: ports 3 and 4 only, these being the board's only analog inputs.

`light sensor [port ▾] light intensity`

:   **Reporter.** Ambient light level from an external light sensor, higher values meaning more light. The `light sensor` block in the Sensing category reads the same sensors on ports 3 and 4 without needing the extension.

`RGB LED [port ▾] lights up [all ▾] with color [color] for (n) secs`

:   Lights the selected LED(s) on an external RGB LED module for the given time, then switches them off and continues.

`RGB LED [port ▾] lights up [all ▾] with color [color]`

:   Sets the selected LED(s) on an external RGB LED module and continues immediately.

`RGB LED [port ▾] lights up [all ▾] with color red (n) green (n) blue (n)`

:   As above, from explicit red, green and blue values (0–255 each).
