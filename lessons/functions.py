"""Example functions to learn definition and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of 2 numbers"""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2
    

max_num: int = my_max(5,9)
other_max_num: int = my_max(100,3)
print(max_num)
print(other_max_num)