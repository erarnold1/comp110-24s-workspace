"""Number Guessing Game."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while correct == False:
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the number!")
        correct=True
    elif guess < SECRET:
        print("Your guess is too low. Guess again!")
    else:
        print("Your guess is too high. Guess again!")

