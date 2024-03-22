"""Exercise 3,  Functional Battleship."""
__author__ = "730469865"
import random 


# takes the users input 
def input_guess(grid_size: int, r_or_c: str) -> int:
    """Generalized function for user's secre grid."""
    assert r_or_c == "row" or r_or_c == "column"
    user_input: int = int(input(f"Guess a {r_or_c}: "))
    if user_input > grid_size:
        while user_input > grid_size:
            user_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    elif user_input <= 0:
        while user_input <= 0:
            user_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return user_input


# box colors
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


# prints the grid depending on size and guesses
def print_grid(grid_size: int, row_guess: int, column_guess: int, correct_guess: bool) -> None:
    """Function to print various grid sizes."""
    # result boxes
    result_box: str = ""
    if correct_guess is True:
        result_box = RED_BOX
    else:
        result_box = WHITE_BOX

    row_counter: int = 1
    # formatting the grids
    while row_counter <= grid_size:
        row_str: str = " "
        column_counter: int = 1
        if row_guess == row_counter:
            while column_counter <= grid_size:
                if column_guess == column_counter:
                    row_str = row_str + result_box
                else:
                    row_str += BLUE_BOX
                column_counter += 1
        else:  
            while column_counter <= grid_size:
                row_str = row_str + BLUE_BOX
                column_counter += 1
        print(row_str) 
        row_counter += 1


# was the guess a hit?
def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Checks the correctness of user's guess."""
    if row_guess == secret_row and column_guess == secret_column:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Puts the game all together."""
    # how many turns the user has taken
    turns: int = 1
    won_game: bool = False
    while turns <= 5 and won_game is False:
        print(f"=== Turn {turns}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        is_guess_correct = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, is_guess_correct)
        if is_guess_correct is True:
            print("Hit!")
            print(f"You won in {turns}/5 turns")
            won_game = True
        elif turns == 5 and won_game is False:
            print("X/5 - Better luck next time!")
            turns += 1
        else:
            print("Miss!")
            turns += 1


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))