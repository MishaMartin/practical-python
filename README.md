# practical-python

Practical Python Project
Intro
This project is tied to the course entitled “Practical Python for Beginners” on Pluralsight. You can view the course here:

https://app.pluralsight.com/library/courses/practical-python-beginners/table-of-contents

The purpose of the exercise is to make sure that you have been able to be hands-on with the course content, and also to build upon the course content to create a new program.

Setup
Create a new Github repository called practical-python and get set up to be able to commit code locally on your machine to the repository.

Part 1: Course Demos
Ensure you have replicated all demos contained in the Practical Python course on Pluralsight. For each demo, create a new file with a name that makes it clear which demo the file pertains to. Make sure you have code for each of the following demos:

Create a Tax Calculator Script

Strings, Input, and Output

Create an Age Calculator

Rock Paper Scissors Game

Sum Expenses

Loan Payment Calculator

Create a Movie Schedule Dictionary

Parse a Nested Contracts Dictionary

Use the Open Weather Map API

Create a Dice Rolling Game

Add Functions to Weather.py

You do NOT need files for the following demos:

Install Python

Create a Python Virtual Environment

When you are finished, add, commit, and push all demo files to your Github repo.

Part 2: Guessing Game
Create a new file called game.py. In it, write a Python program that that allows the user to play the classic number guessing game. The game will work like this:

The computer will choose a random number between 1–100 and ask the user to guess the number

Once the user guesses, the computer will tell the user if their guess was too high or too low

The game is over once the user guesses the computer’s number. When the game is over, the computer the total number of guesses the user made before getting the right answer.

Here’s the terminal output for an example game:

$ python3 game.py
Howdy, what's your name?
(type in your name) Jessica
Jessica, I'm thinking of a number between 1 and 100.
Try to guess my number.
Your guess? 50
Your guess is too low, try again.
Your guess? 80
Your guess is too high, try again.
Your guess? 60
Your guess is too low, try again.
Your guess? 70
Your guess is too high, try again.
Your guess? 63
Your guess is too low, try again.
Your guess? 64
Your guess is too low, try again.
Your guess? 67
Your guess is too low, try again.
Your guess? 69
Your guess is too high, try again.
Your guess? 68
Well done, Jessica! You found my number in 9 tries!
Here’s a rough pseudocode outline of the program that gave this output:

greet player
get player name
choose random number between 1 and 100
repeat forever:
    get guess
    if guess is incorrect:
        give hint
        increase number of guesses
    else:
        congratulate player
When you are finished, add, commit, and push your game to your Github repo.