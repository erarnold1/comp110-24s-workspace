"""Splitting a dictionary into two lists."""
__author__ = "730469865"


def get_keys(dictionary: dict[str, int]) -> list[str]:
    """Creates a list with all the key values."""
    key_list: list[str] = list()
    if dictionary == dict():
        return list()
    for key in dictionary:
        key_list.append(key)
    return key_list


def get_values(dictionary2: dict[str, int]) -> list[int]:
    """Creates a list with all the value from the dictionary."""
    value_list = list()
    if dictionary2 == dict():
        return list()
    for key in dictionary2:
        value_list.append(dictionary2[key])
    return value_list