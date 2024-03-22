"""Exercise 4, List Functions."""
__author__ = "730469865"


def all(my_list: list[int], num: int) -> bool:
    """Returns true or false if every value in a list equals some integer."""
    counter = 0
    if my_list == []:
        return False
    while counter <= len(my_list) - 1:
        if my_list[counter] == num:
            counter = counter + 1
        else:
            return False
    return True


def max(new_list: list[int]) -> int:
    """Returns the max number in a list."""
    if len(new_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_num = new_list[0]
    counter = 1
    while counter <= len(new_list) - 1:
        if new_list[counter] >= max_num:
            max_num = new_list[counter]
            counter += 1
        else:
            counter += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns true or false if every value at every index of two lists matches."""
    counter = 0
    if len(list1) != len(list2):
        return False
    while counter <= len(list1) - 1:
        if list1[counter] == list2[counter]:
            counter += 1
        else:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Appends one list onto another."""
    counter = 0
    while counter <= len(list2) - 1:
        list1.append(list2[counter])
        counter += 1