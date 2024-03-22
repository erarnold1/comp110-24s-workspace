"""Functions that either mutate a list or don't"""

def remove_first(input_list: list[str]) -> None:
    """Remove first element of input list."""
    input_list.pop(0)

def get_first(input_list: list[str]) -> str:
    """Returns the first element of a list."""
    return input_list[0]

def get_and_remove_first(input_list: list[str]) -> str:
    """Return first element and remove it."""
    elem: str = input_list[0]
    input_list.pop(0)
    return elem