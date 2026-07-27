# mBot (mCore) Block Reference {.unnumbered}

This chapter lists all programming blocks available for the mBot (mCore) board in mBlock. 

**Before the blocks appear:** The robot's blocks only appear once the mBot has been added to mBlock via the devices panel. A fresh start shows only sprite/stage categories.

**Extensions:** Two categories require extensions, added with the `+` button at the bottom of the category panel:

| Extension | Adds | Needed for |
| :--- | :--- | :--- |
| `color sensor` | Colour Sensor category | Color Vision lesson |
| `light sound` | Light & Sound category (external sound/light sensors, RGB LED) | Sound Localization lesson, programming challenge 3 |

Opening a supplied example program loads the relevant extension automatically.

---

## Action Blocks

Controls the two drive motors. There are two forms: **timed** blocks run for a set duration then continue; **non-timed** blocks start the motors and immediately continue to the next block.

### Timed movement

- `move forward at power (n)% for (n) secs` — Drives both motors forward at the given power (0–100%) for the given number of seconds, then stops.
- `move backward at power (n)% for (n) secs` — As above, in reverse.
- `turn left at power (n)% for (n) secs` — Turns the robot left at the given power for the given time.
- `turn right at power (n)% for (n) secs` — Turns the robot right at the given power for the given time.

### Non-timed movement

- `move [move forward ▾] at power (n)%` — Starts the motors in the chosen direction at the given power and continues immediately. Motors keep running until a `stop moving` block or another Action block changes them. Dropdown: `move forward`, `move backward`, `turn left`, `turn right`.
- `left wheel turns at power (n)%, right wheel at power (n)%` — Sets each motor's power independently (0–100% each). Non-blocking.
- `stop moving` — Stops both motors immediately.

---

## Show Blocks

Controls the two onboard RGB LEDs and the onboard buzzer. The mCore board carries two RGB LEDs, addressed as `left`, `right`, or `all`.

- `LED [all ▾] shows color [color] for (n) secs` — Lights the selected LED(s) in the chosen colour, holds the program for the given time, then turns the LED(s) off and continues. First slot: `all`, `left`, `right`.
- `LED [all ▾] shows color [color]` — Sets the selected LED(s) to the chosen colour and continues immediately. The colour stays until changed.
- `turn on [all ▾] light with color red (n) green (n) blue (n)` — Sets the selected LED(s) from explicit RGB values (0–255 each) and continues immediately. First slot: `all`, `left`, `right`. (0,0,0) turns the LED off.
- `play note [C4 ▾] for (n) beats` — Plays a named musical note on the onboard buzzer for the given number of beats, holding the program for that time. Dropdown: standard note names (C4, D4, E4, …).
- `play sound at frequency of (n) Hz for (n) secs` — Plays a tone at the given frequency in Hz for the given number of seconds, holding the program for that time.

**Note:** There is no dedicated "off" block for LEDs. Set the colour to black in the picker, or use RGB (0,0,0).

---

## Sensing Blocks

The onboard sensors and the sensors in the robot's default configuration. External sound and light sensors are in the Light & Sound extension.

- `ultrasonic sensor [port ▾] distance(cm)` — Distance in centimetres from the sonar sensor on the selected port to whatever is in front of it. Dropdown: any of the four ports.
- `light sensor [on-board ▾] light intensity` — Ambient light level from the onboard light sensor. Higher values mean more light; range is roughly 0–1000.
- `line follower sensor [port ▾] value` — Reads the line-follower sensor as a single number combining its two infrared detectors: 0=centred, 1=drifting right, 2=drifting left, 3=line lost.
- `line follower sensor [port ▾] detects [leftside ▾] being [black ▾] ?` — Boolean. True when the chosen side of the line-follower sensor sees the chosen surface colour.
- `when on-board button [pressed ▾] ?` — Boolean. True when the onboard button is in the chosen state. Dropdown: `pressed` / `released`.
- `IR remote [A ▾] pressed?` — Boolean. True while the named button on an infrared remote is being pressed.
- `send IR message (text)` — Transmits a message over the board's infrared transmitter.
- `IR message received` — Reporter. The last message received over infrared.
- `timer` — Reporter. Seconds elapsed since the program started or since the timer was last reset.
- `reset timer` — Sets the timer back to zero.

---

## Events Blocks

Where a program starts. The choice between `when [green flag] clicked` and `when mBot(mcore) starts up` is the choice between the robot's two operating modes.

- `when [green flag] clicked` — Starts the script when the green flag is clicked. The program runs on the computer and drives the robot over the live connection (Live mode).
- `when mBot(mcore) starts up` — Starts the script when the robot is switched on, running the program from the robot's own memory (Upload mode). The program must be uploaded over USB first.
- `when on-board button [pressed ▾]` — Starts the script when the onboard button is pressed.
- `when [space ▾] key pressed` — Starts the script when the chosen key is pressed on the computer's keyboard. Live mode only.
- `when I receive [message ▾]` — Starts the script when the named broadcast message is sent.
- `broadcast [message ▾]` — Sends the named message and continues immediately.
- `broadcast [message ▾] and wait` — Sends the named message and waits until every script started by it has finished.

---

## Control Blocks

- `forever` — Repeats the enclosed blocks indefinitely. Never exits on its own.
- `wait (n) seconds` — Pauses the script for the given time.
- `if <> then` — Runs the enclosed blocks once if the condition is true.
- `if <> then / else` — Runs the first group if the condition is true, the second group otherwise.
- `while <> repeat` — Repeats the enclosed blocks as long as the condition stays true.
- `repeat until <>` — Repeats the enclosed blocks until the condition becomes true.
- `repeat (n)` — Repeats the enclosed blocks a fixed number of times.
- `count with [i ▾] from (n) to (n) by step (n) repeat` — Repeats the enclosed blocks while counting a variable from a start value to an end value in fixed steps.
- `wait until <>` — Pauses the script until the condition becomes true.
- `break` — Exits the enclosing loop immediately.
- `continue` — Skips the rest of the current pass and starts the next one.
- `stop [all ▾]` — Stops running scripts. Dropdown options include `all`, `this script`, etc.

---

## Operator Blocks

- `() + ()` — Adds two values.
- `() - ()` — Subtracts the second value from the first.
- `() * ()` — Multiplies two values.
- `() / ()` — Divides the first value by the second.
- `pick random (n) to (n)` — A random whole number between the two values, inclusive.
- `() > (n)` — Boolean. True if the first value is greater than the second.
- `() < (n)` — Boolean. True if the first value is less than the second.
- `() = (n)` — Boolean. True if the two values are equal.
- `<> and <>` — Boolean. True only if both conditions are true.
- `<> or <>` — Boolean. True if either condition is true.
- `not <>` — Boolean. Inverts a condition.
- `[abs ▾] of ()` — Applies the selected mathematical function to a value. Dropdown: `abs` (absolute value), `floor`, `ceiling`, `sqrt`, `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `ln`, `log`, `e^`, `10^`.
- `() mod ()` — The remainder after dividing the first value by the second.
- `round ()` — Rounds a value to the nearest whole number.
- `join (text) (text)` — Joins two pieces of text.
- `letter (n) of (text)` — The character at the given position in a piece of text.
- `length of (text)` — The number of characters in a piece of text.
- `(text) contains (text) ?` — Boolean. True if the first text contains the second.

---

## Variables

The category is empty until the first variable is created.

- `Make a Variable` — Creates a new variable. Click the Variables category, then this option, and give it a name.
- `set [variable] to ()` — Puts a value in the variable. The slot takes a typed value, a sensor block, or an expression.
- `change [variable] by ()` — Adds the given amount to the variable's current value.

Every variable a program creates is shown on the stage (the white area at the top left of the mBlock window).

---

## Ports

The robot has four RJ25 ports. They are **not** interchangeable.

- **Sound sensor:** ports **3 and 4 only** (the only analog inputs).
- **Sonar (ultrasonic) sensor:** any of the four ports.
- **Line follower sensor:** any of the four ports.
- **Colour sensor:** any of the four ports.

Lesson conventions: sonar on **port 1**, colour sensor on **port 2**, left sound sensor on **port 3**, right sound sensor on **port 4**.

---

## Extension: Colour Sensor

Requires the **`color sensor` extension**. The colour sensor only works in Upload mode.

- `color sensor [port ▾] [R ▾] value` — The amount of light the sensor detects in one channel. Dropdown: `R`, `G`, `B`, `H`, `S`, `V`.
- `color sensor [port ▾] detects [white ▾]` — Boolean. True when the sensor classifies what it sees as the named colour. Dropdown: `white`, `black`, `red`, `green`, `blue`, `yellow`, `purple`, `orange`, `pink`, plus others.
- `color sensor [port ▾] set fill light LED to [on ▾]` — Switches the sensor's own white illumination LEDs on or off. Dropdown: `on`, `off`.

---

## Extension: Light & Sound

Requires the **`light sound` extension**.

- `sound sensor [port ▾] loudness` — The current sound level at an external Makeblock sound sensor. Higher values mean louder. Dropdown: ports **3 and 4 only**.
- `light sensor [port ▾] light intensity` — Ambient light level from an external light sensor on the chosen port. Higher values mean more light.
- `RGB LED [port ▾] lights up [all ▾] with color [color] for (n) secs` — External RGB LED module.
- `RGB LED [port ▾] lights up [all ▾] with color [color]` — External RGB LED module, continuous.
- `RGB LED [port ▾] lights up [all ▾] with color red (n) green (n) blue (n)` — External RGB LED module with explicit RGB values.
