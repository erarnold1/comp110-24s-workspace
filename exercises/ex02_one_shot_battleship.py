"""Exercise 2 – More Advanced Battleship."""
__author__ = "730469865"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

# row input
row_input: int = int(input("Guess a row: "))
if row_input > grid_size:
    while row_input > grid_size:
        row_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
if row_input < 0:
    while row_input < 0:
        row_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# column input
column_input: int = int(input("Guess a column: "))
if column_input > grid_size:
    while column_input > grid_size:
        column_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
if column_input < 0:
    while column_input < 0:
        column_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# box colors
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# result boxes
result_box: str = ""
if column_input == secret_column and row_input == secret_row:
    result_box = RED_BOX
else:
    result_box = WHITE_BOX

row_counter: int = 1

# formatting the grids
while row_counter <= grid_size:
    row_str: str = " "
    column_counter: int = 1
    if row_input == row_counter:
        while column_counter <= grid_size:
            if column_input == column_counter:
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

# user feedback
if row_input == secret_row and column_input == secret_column:
    print("Hit!")
elif row_input == secret_row:
    print("Close! Correct row, wrong column.")
elif column_input == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")
