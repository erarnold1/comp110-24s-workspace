"""Some functions for my garden plan!"""
__author__ = "730469865"

plants_by_kind: dict[str, list[str]] = {"flower": ['marigold', 'zinnia'], "vegetable": ['carrots']}

plant: str = 'apple'
plant_kind: str = 'fruit'


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_type: str, plant: str) -> None:
    """Will add an additional plant of the same kind to the end of a list inside a dict."""
    if plant_type in plants_by_kind:
        plants_by_kind[plant_type].append(plant)
    else:
        plants_by_kind[plant_type] = [plant]


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Will add a plant to a list of plants for a certain month inside a dict."""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = [plant]


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """Will return plants that are of the same kind specified and can be planted in the month specificed."""
    assert plant_kind in plants_by_kind
    assert month in plants_by_date
    # Look up the list of plants of 'plant kind'
    list_of_plants_by_kind: list[str] = plants_by_kind[plant_kind]
    # Look up the list of plants from 'month'
    list_of_plants_by_date: list[str] = plants_by_date[month]
    combined: list[str] = []
    for plant in list_of_plants_by_kind:
        for other_plant in list_of_plants_by_date:
            if plant == other_plant:
                combined.append(other_plant)
    if len(combined) > 0:
        return f"{plant_kind}s to plant in {month}: {combined}"
    elif len(combined) == 0:
        return f"No {plant_kind}s to plant in {month}"