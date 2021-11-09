#this is a module in the python standard library
import random

roll = random.randint(1,6)

guess = int(input("Guess the diceroll:\n"))

if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print("Wrong! They rolled a " + str(roll))