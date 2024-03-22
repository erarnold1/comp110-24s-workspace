"""Unit Tests that will test the functionality of dictionary functions."""
__author__ = "730469865"
from exercises.ex05.dictionary import invert
import pytest
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


# Unit tests for invert
def test_invert_str_int() -> None:
    """Invert should turn a dict of strings and ints into a dict of ints then strings."""
    test: dict[str, int] = {"A": 96, "B": 85, "C": 72}
    assert invert(test) == {96: "A", 85: "B", 72: "C"}


def test_invert_empty_dict() -> None:
    """Invert return an empty dict when given an empty dict."""
    test: dict[str, int] = {}
    assert invert(test) == {}


def test_invert_list_error() -> None:
    """Should return a dict with two lists, with the second list as the key now."""
    with pytest.raises(KeyError):
        my_dictionary = {'A': [96, 98, 94], 'B': [85, 87, 81]}
        invert(my_dictionary)


# Unit tests for favorite color
def test_str_int() -> None:
    """Tests when key is an int and the value is a string."""
    test: dict[str, str] = {1: "pink", 2: "blue", 3: "green", 4: "pink"}
    assert favorite_color(test) == "pink"


def test_tie_color() -> None:
    """Tests that first value is returned in event of a tie."""
    test: dict[str, str] = {"Ellis": "pink", "Evan": "blue", "Avery": "blue", "Ella": "pink"}
    assert favorite_color(test) == "pink"


def test_empty_dict() -> None:
    """An empty dictionary input should output an empty dictionary."""
    test: dict = {}
    assert favorite_color(test) == {}


# Unit tests for count
def test_empty_dict_count() -> None:
    """An empty list input should output an empty dictionary."""
    test: list = []
    assert count(test) == {}


def test_count_str() -> None:
    """Should return the name with how many times it appears in a list."""
    test: list[str] = ["Ellis", "Evan", "Arnold", "Arnold"]
    assert count(test) == {"Ellis": 1, "Evan": 1, "Arnold": 2}


def test_count_mixed_types() -> None:
    """Function works correctly with mixed types inside the given list."""
    test: list[int] = ["hello", 2, 3, 3, "world", 3, 2, 1]
    assert count(test) == {"hello": 1, 2: 2, 3: 3, 1: 1, "world": 1}


# Unit tests for alphabetizer
def test_alphabetizer_empty_list() -> None:
    """When given an empty list, it should return an empty dictionary."""
    test: list = []
    assert alphabetizer(test) == {}


def test_alphabetizer_str_list() -> None:
    """Testing a simple case of a list on unique strings."""
    test: list[str] = ["boy", "girl", "baseball", "sun", "grass", "cloud"]
    assert alphabetizer(test) == {'b': ['boy', 'baseball'], 'g': ['girl', 'grass'], 's': ['sun'], 'c': ['cloud']}


def test_alphabetizer_str_case_errors() -> None:
    """Testing function works correctly when there are case errors."""
    test: list[str] = ['Boy', 'girl', 'baseball', 'Sun', 'Grass']
    assert alphabetizer(test) == {'b': ['Boy', 'baseball'], 'g': ['girl', 'Grass'], 's': ['Sun']}


# Unit tests for update_attendance
def test_update_one_day_dict() -> None:
    """Should return same day and new student given a one day dict to start."""
    test: dict = {"Wednesday": ["Evan"]}
    update_attendance(test, "Wednesday", "Ellis")
    assert test["Wednesday"] == ['Evan', 'Ellis']


def test_update_new_day_dict() -> None:
    """Should return new day and new student given a one day dict to start."""
    test: dict = {"Wednesday": ["Evan"]}
    update_attendance(test, "Thursday", "Ellis")
    assert test["Thursday"] == ['Ellis']


def test_update_case_errors() -> None:
    """Should return the same day with list of names with simple case error."""
    test: dict = {"Wednesday": ['Evan']}
    update_attendance(test, "wednesday", 'Ellis')
    assert test["Wednesday"] == ['Evan', 'Ellis']