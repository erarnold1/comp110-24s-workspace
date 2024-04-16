"""File to define Fish class."""


class Fish:
    """Creates a Fish class with an age."""

    age: int
    
    def __init__(self):
        """Creates a new fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increases the age of a fish by one."""
        self.age += 1
        return None