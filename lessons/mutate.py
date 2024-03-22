"""Mutating functions."""
__author__ = "730469865"


def manual_append(my_list: list[int], x: int) -> None:
    """Appends a number to the end of a list."""
    my_list.append(x)


a: list[int] = [1, 2, 3]
manual_append(a, 3)
print(a)


def double(new_list: list[int]) -> None:
    """Doubles each number in a list."""
    counter = 0
    while counter <= len(new_list) - 1:
        new_list[counter] *= 2
        counter += 1


b: list[int] = [10, 20, 30]
double(b)
print(b)