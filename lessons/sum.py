"""Summing the elements of a list using different loops."""
__author__ = "730469865"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of a list of floats."""
    if vals == []:
        return 0.0
    counter = 0
    sum = 0.0
    while counter < len(vals):
        sum += vals[counter]
        counter += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns the sum of a list of floats."""
    sum = 0.0
    for element in vals:
        sum += element
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of a list of floats."""
    sum = 0.0
    for index in range(0, len(vals)):
        sum += vals[index]
    return sum