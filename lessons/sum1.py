"""Sum all elements in a list."""

def sum(elements: list[int]) -> int:
    """Sums all elements in elements."""
    total: int = 0
    for elem in elements:
        total += elem
    return total