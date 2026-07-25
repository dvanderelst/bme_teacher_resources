# Introduction to Programming


## Materials

| Item | Description |
| :--- | :--- |
| Printed programming blocks | These are the paper stubs used during the Cheese Sandwich Factory game. |

## What is programming

In a next guide, we will introduce mBlock, the programming language we will be using to program the robot. However, before starting with the mBlock programming language, it is useful to define programming. This unit aims to introduce students to programming in an abstract sense before they start working with the robot.

Programming is writing step-by-step instructions for a machine, such as a computer or a robot, which is essentially a computer plus some sensors and motors. The set of instructions you can pick from when writing the program is a programming language. In this lesson, the programming language will be mBlock. mBlock provides the instructions the robot understands.

Before delving into programming the robot, explore the challenges programmers face through the following simple (made-up) example. Engage students with the scenario pictured below.

> You are an engineer hired to program a mobile robot to reach the house's front door (indicated with an arrow) when the bell rings. The robot should be able to get to the front door from any location in the house.
> 

![This image depicts the layout of an imaginary building. The building is serviced by a robot, and we want to program it to answer the door when the doorbell rings.](images/introduction-to-programming-b71247e9.png)

Discuss the following with students. In solving the problem, programmers are faced with two different challenges.

- Challenge 1: Understanding how to solve the problem in principle. Programmers need to understand the problem to formulate how they might solve it. Programmers will ask themselves the following kinds of questions. What are the main difficulties in solving the problem? What are possible solutions? How can the problem be simplified? How can the larger problem be broken into smaller steps? In brief, the first challenge for a programmer is to analyze the problem. The outcome of addressing Challenge 1 is an algorithm: a method for addressing the problem.
- Challenge 2: Translating the algorithm into a set of programming language instructions. Once a problem has been analyzed and solutions proposed, it needs to be translated into a set of programming language instructions. This is the implementation problem: how do you string together a set of instructions so that they implement your algorithm?

## Activity: Cheese Sandwich Factory Game

Above, we discussed that programmers typically address two challenges when programming robots. To convey this message more clearly to students, we have developed a game in which the students are asked to write a program for a hypothetical robot. This game aims to help students experience the two challenges that occur when programming. First, students need to understand how a cheese sandwich can be built, in principle. Second, students need to shoehorn their intuition into the commands provided by the programming language. This requires understanding the commands. This exercise encourages students to perform a problem analysis before they start coding when programming robots.

### Problem description

Imagine you are an engineer hired to write the program controlling a robot arm in a cheese sandwich factory. The image below shows that the robot arm can reach three locations labeled 1-3. You are asked to write a program for the robot such that it makes complete cheese sandwiches. A complete sandwich consists of a slice of bread, a slice of cheese, and another slice of bread.

![Image of the challenge faced in the Cheese Sandwich Maker game. Students are asked to program the robot arm to use the materials delivered on the conveyor belt (at location 1) to build cheese sandwiches on the loading deck of a truck (location 3). Unneeded materials (bread and cheese) can be discarded on another conveyor belt (location 2).](images/introduction-to-programming-0aeb7e34.png)

1. Location 1 corresponds to the end of a conveyor belt. This conveyor belt delivers slices of bread and cheese. **However, and this is important, the order is random.** You do not know in advance what the following item will be. It can be either bread or cheese.
2. Location 2 corresponds to the start of a second conveyor belt. This conveyor belt leads to additional robot arms in the factory. This conveyor belt can be used to drop off items that are not needed by the robot. For example, if the conveyor belt 1 delivers a run of bread, the superfluous slices of bread can be dropped onto conveyor belt two.
3. Location 3 corresponds to a place where cheese sandwiches are assembled. For the purpose of this game, we assume that the truck can only carry one cheese sandwich. Whenever a complete sandwich is assembled on the truck's back, it drives off, and another truck takes its place. For this game, a completed sandwich consists of a slice of cheese between two slices of bread.

### Robot programming language

For the purpose of the game, we imagine that the robot arm comes with a simple programming language that only consists of four possible commands. These are given below.

![](images/introduction-to-programming-8607b09d.png)

This instruction tells the robot to go to locations 1, 2, or 3. Students can fill in the location’s number in the space provided by the dashes. Each instruction in a program can get a number. This number can be written next to the pointing finger.

![](images/introduction-to-programming-9b5c7cb1.png)

This instruction tells the robot to jump to a different numbered instruction in the program. This instruction can be used to skip parts of the program or return to earlier parts.

![](images/introduction-to-programming-331392b1.jpg)

This instruction tells the robot to pick up or drop the object (bread or cheese) at its current location. Students can tell the robot to drop or pick up by ticking the appropriate box. 

![](images/introduction-to-programming-8dc64988.png)

This instruction is somewhat special. It can be used to execute specific parts of the program depending on which object the robot is currently holding and which object is available at its current location. Each of the blanks can be filled out with one of the following: Bread, Cheese, Not Bread, Not Cheese, Any, Nothing

The `If HOLDS ___ AND BELOW ___` instruction sometimes confuses students. Therefore, we provide some examples of how it can be used. The two blanks in the instruction can be filled with the following: Bread, Cheese, Not Bread, Not Cheese, Any, Nothing. Therefore, the following is a valid set of instructions.

```jsx
1 [If HOLDS BREAD AND BELOW CHEESE:]
2 		[Go To Location 3]
3 		[Drop]
4 [Go to Location 2]
```

This set of instructions makes the robot check whether it is currently holding bread and whether there is a slice of cheese at the current location. In this case, the robot would go to location 3 and drop whatever it is holding, in this case, bread. Next, the robot will move to location 2 (as this is the next instruction). If the robot, at the start of this snippet of code, does not hold bread or there is no cheese at its current location, it skips the instructions on lines 2 and 3 and directly executes the instruction on line 4 (going to location 2).

Below is a second example. This bit of code does the following. First, it moves the robot to location 3. Next, it checks whether the robot is holding a slice of cheese and whether there is bread at the current location. If this is so, it drops the cheese. Next, it checks whether it holds nothing, and either bread or cheese is below it. If so, it picks up the current object.

```jsx
1 [Go to location 3]
2 [If HOLDS CHEESE AND BELOW BREAD:]
3			[Drop]
4 [If HOLDS NOTHING AND BELOW ANY:]
5			[Pick Up]
```

This program is quite silly. If the robot holds cheese and there is bread below, it will drop the cheese only to pick it up again using lines 4 and 5.

> **Tip**
>
> If students think the example is not realistic, you can reassure them. Robots often come with a specific set of instructions, which is a specialized programming language for this particular robot. For example, the robot arms distributed by ST Robotics use a custom programming language called Roboforth. The brave could [consult this manual](https://strobotics.com/manuals/manual17.htm) for the RoboForth language.

### Playing the game

Below, we have linked two files that allow printing instructions on slips, particularly [Avery Template 16154 Tickets With Tear-Away Stubs](https://www.avery.com/templates/16154). We provide a file for printing on each sheet's front and back. Alternatively, the files can be printed on normal paper sheets and cut.

[Avery16154cheese_sandwich_front_windows.doc](files/Avery16154cheese_sandwich_front_windows.doc)

[Avery16154cheese_sandwich_back_windows.doc](files/Avery16154cheese_sandwich_back_windows.doc)

Providing the students with printed strips allows them to “write” a program by placing and moving the slips around on their desks. Each student (group) should receive one set of printed instructions (i.e., a front and a back version of the strips). This should be sufficient to construct a program for making the robot build cheese sandwiches. Make it clear to students they are not expected to use all the slips. Only as many as they think they need. Give students sufficient time to try to construct a program that solves the problem. Encourage them to check each other's work. 

### Possible Solution

There are different solutions to the game. The only way to test whether a solution provided by a student works is to step through the program and work out whether it results in cheese sandwiches being built. Here is one solution:

```jsx
Goto location 1
Pick up
Goto location 3
If holding cheese and below is bread:
		Drop
If holding bread and below is cheese:
		Drop
If holding bread and below is nothing:
    Drop
Goto location 2
		Drop
Go to step 1
```

This solution picks up whatever is presented at location 1. Next, it moves to location 3. The arm will only drop its load if whatever it is holding is not what is currently showing at location 3. Remember that whenever a complete sandwich is produced, the truck carries it away. Therefore, looking at the bread at location 3, we can assume it is a new sandwich's bottom (start). Finally, the robot moves to location 2. There, it drops whatever it is holding. It is possible that the robot is not holding anything. However, executing the drop command ensures the robot's arm is empty when moving back to location 1.

### Conclusion

After playing the game, ask students about their experiences. What difficulties did they encounter? Try to relate their experience to the two challenges programmers face (and they will face) when programming a robot.
