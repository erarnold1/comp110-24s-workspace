"""File to define Bear class."""


class Bear:
    """Creates a Bear class, with an age and hunger score."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """Creates a new bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Increases the age of a bear by one."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increasesa bear's hunger score by the number of fish it eats."""
        self.hunger_score += num_fish
        return None