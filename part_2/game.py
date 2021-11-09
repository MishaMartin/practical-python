import random

# number = random.randint(1,100)
number = 15

name = input("Howdy, what's your name?\n")
guess = int(input(name + ", I'm thinking of a number between 1 and 100.\nTry to guess my number.\n"))
guess_count = 1

def wrong_guess():
    new = int(input("Your guess?\n"))
    global guess
    guess = new 
    global guess_count
    guess_count += 1
    print(guess_count)
    guesses()

def guesses():
    if guess == number:
        print(F"Well done {name}! You found my number in {guess_count} tries!")
        
    elif guess > number:
        print("Your guess is too high, try again.")
        wrong_guess()
    else:
        print("Your guess is too low, try again.")
        wrong_guess()

guesses()