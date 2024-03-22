"""Test my garden functions."""
__author__ = "730469865"
from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date
import pytest


# Unit tests, add_by_kind
# Edge case
def test_kind_empty_dict() -> None:
    """Given an empty dict, this function should update with the new plant type."""
    test: dict = {}
    add_by_kind(test, "flower", "tulip")
    assert test['flower'] == ['tulip']


# Use case
def test_kind_add_existing_type() -> None:
    """Given a dict, when you add another item of the same key, the list should update."""
    test: dict = {'flower': ['tulip']}
    add_by_kind(test, 'flower', 'rose')
    assert test['flower'] == ['tulip', 'rose']


# Unit tests, add_by_date
# Edge case
def test_date_empty_dict() -> None:
    """Given an empty dict, this function should update with the new plant inside the given month."""
    test: dict = {}
    add_by_date(test, "March", "daisy")
    assert test['March'] == ['daisy']


# Use case
def test_date_existing_month() -> None:
    """Updates the list at with the same month key."""
    test: dict = {"March": ["daisy"]}
    add_by_date(test, "March", "peas")
    assert test["March"] == ["daisy", "peas"]


# Unit tests, lookup_by_kind_and_date
# Edge case
def test_lookup_not_in_dict() -> None:
    """If the function has 'plant_kind' or 'month' that isn't in the dictionary there will be an error."""
    with pytest.raises(AssertionError):
        test_kind: dict = {'flower': ['tulip']}
        test_date: dict = {'March': ['daisy']}
        lookup_by_kind_and_date(test_kind, test_date, 'flower', 'February')


# Use case
def test_lookup_basic_case() -> None:
    """Will tell you which plant to plant in a given month."""
    test_kind: dict = {'vegetable': ['peas', 'carrots', 'cucumber']}
    test_date: dict = {'March': ['peas'], 'April': ['daisy']}
    lookup_by_kind_and_date(test_kind, test_date, 'vegetable', 'March')
    assert "flowers to plant in March: peas"