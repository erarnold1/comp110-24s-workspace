"""Exercise 5, working with dictionaries."""
__author__ = "730469865"


def invert(beginning_dict: dict) -> dict:
    """Will invert the order of dictionary values."""
    new_dict = dict()
    list_of_values = list(beginning_dict.values())
    idx = 0
    while idx < len(list_of_values) - 1:
        if list_of_values[idx] == list_of_values[idx + 1]:
            raise KeyError("Please make sure your values are different.")
        idx += 1
    for key in beginning_dict:
        if type(beginning_dict[key]) is list:
            raise KeyError("Please make sure your values are not lists.")
    for key, value in beginning_dict.items():
        new_dict[value] = key
    return new_dict
# print(invert({'a':'b', 'c':'d'}))


def favorite_color(info_dict: dict[str, str]) -> str:
    """Will return the color that is most popular in a dictionary."""
    if info_dict == {}:
        return {}
    result_dict: dict[str, int] = dict()
    colors_list = info_dict.values()
    for value in colors_list:
        if value in result_dict:
            result_dict[value] += 1
        else:
            result_dict[value] = 1
    sorted_result_dict = sorted(result_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_result_dict[0][0]

# print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def count(list1: list[str]) -> dict[str, int]:
    """Will return the name and number of times an item appears in a list."""
    result_dict: dict[str, int] = dict()
    for item in list1:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict
# print(count(["Ellis", "Evan", "Arnold", "Arnold"]))


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary with the letter as key and list of words that begin with that letter as a list."""
    new_dict: dict[str, list[str]] = dict()
    for element in word_list:
        if element[0].lower() in new_dict:
            new_dict[element[0].lower()] += [element]
        else:
            new_dict[element[0].lower()] = [element]
    return new_dict

# print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))
    

def update_attendance(attendance: dict[str, list[str]], dow: str, student: str) -> None:
    """Updates an attendance log with new days and student information."""
    dow = dow.capitalize()
    if dow in attendance:
        attendance[dow].append(student)
    else:
        attendance[dow] = [student]
    attendance[dow] = list(set(attendance[dow]))
    return None