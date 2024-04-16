"""File to define River class."""
__author__ = "730469865"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Creates a River class with day, list of fish, and list of bears."""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and bears, removes if necessary."""
        # checks bears ages
        new_bears: list[Bear] = []
        for x in self.bears:
            if x.age <= 5:
                new_bears.append(x)
        self.bears = new_bears
        # checks fish ages
        new_fish: list[Fish] = []
        for x in self.fish:
            if x.age <= 3:
                new_fish.append(x)
        self.fish = new_fish
        return None
    
    def remove_fish(self, amount: int):
        """Removes the frontmost amount of fish from the list."""
        for x in range(0, amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Simulates a bear eating fish."""
        for x in self.bears:
            if len(self.fish) >= 5:
                x.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Removes a bear from the river if its hunger score is too low."""
        new_bears: list[Bear] = []
        for x in self.bears:
            if x.hunger_score >= 0:
                new_bears.append(x)
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """Repopulates the number of fish."""
        n = len(self.fish)
        num_to_add = (n // 2) * 4
        for x in range(0, num_to_add):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulates the number of bears."""
        n = len(self.bears)
        num_to_add = n // 2
        for x in range(0, num_to_add):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Prints the day and number of fish and bears."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week of the life of a river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None      