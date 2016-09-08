#/usr/bin/env python3

import random

def get_random():
    return random.randint(1, 100) 

def get_guess():
    try:
        return int(input("Guess: "))
    except ValueError:
        print("Numbers only Please! Try again!")
        return get_guess()

def main():
    number = random.randint(1, 100)
    guess = get_guess()
    while guess != number:
        if guess > number:
            print('Lower')
        elif guess < number:
            print('Higher')
        guess = get_guess()
    print('Correct!')
    pa()

def pa():
    play_again = input("Would you like to play again? y/n: ")
    if play_again == "y":
        return main()
    else:
        print('Good Bye!')
        

if __name__ == '__main__':
    main()
