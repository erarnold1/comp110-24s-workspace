"""EX01 - Simple Battleship - A Cute Step Towards Battleship."""
__author__ = """730469865"""


player1_input: int = int(input("Pick a secret boat location between 1 and 4: "))

# player 1 number check
if player1_input < 1:
    print("Error! " + str(player1_input) + " too low!")
    exit()
if player1_input > 4:
    print("Error! " + str(player1_input) + " too high!")
    exit()

player2_input: int = int(input("Guess a number between 1 and 4:"))

# player 2 number checks
if player2_input < 1:
    print("Error! " + str(player2_input) + " too low!")
    exit()
if player2_input > 4:
    print("Error! " + str(player2_input) + " too high!")
    exit()

# same number check
if player2_input == player1_input:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")

# box colors
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# special boxes
guess_box: str = " "
if player2_input == player1_input:
    guess_box = RED_BOX
else:
    guess_box = WHITE_BOX

# checking each box
result_box: str = " "
if player2_input == 1:
    result_box = result_box + guess_box
else:
    result_box = result_box + BLUE_BOX

if player2_input == 2:
    result_box = result_box + guess_box
else:
    result_box = result_box + BLUE_BOX

if player2_input == 3:
    result_box = result_box + guess_box
else:
    result_box = result_box + BLUE_BOX

if player2_input == 4:
    result_box = result_box + guess_box
else:
    result_box = result_box + BLUE_BOX

print(result_box)