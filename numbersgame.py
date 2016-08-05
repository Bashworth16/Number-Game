#/usr/bin/env python3
import random
number = random.randint(1, 100)
guess = int()
while (guess != number):

    guess = input("Guess a number between 1 and 100: ")

    if int(guess) > int(number):
        print("Lower...: ")
    if int(guess) < int(number):
        print("Higher...: ")
    if int(guess) == int(number):
        input("You're Right!")
        break

