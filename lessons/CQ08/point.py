"""Create a class named 'Point'."""
from __future__ import annotations
__author__ = "730469865"


class Point:
    """Creates a Point class, which creates x and y coordinates."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Creates a new point."""
        self.x = x_init
        self.y = y_init
        # it will return self.

    def scale_by(self, factor: int) -> None:
        """Scales the x and y coordinates by an inputed factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returns a new Point based on the scale of the given factor."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self):
        """Prints a prettier version of our point."""
        return f"({self.x}, {self.y})"
    
    def __mul__(self, factor: float) -> Point:
        return Point(self.x * factor, self.y * factor)
    
    def __getitem__(self, index: int) -> float:
        """Overlading subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else: 
            raise IndexError
    

a: Point = Point(1.0, 3.0)
b: Point = a * 3.0
print(b[1])
