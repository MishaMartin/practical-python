import random

number = random.randint(1,100)

name = input("Howdy, what's your name?\n")
guess = name + ", I'm thinking of a number between 1 and 100.\n Try to guess my number."
print(guess)