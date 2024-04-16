"""Checks for correctness of Point.py."""

from lessons.CQ08.point import Point


test_point: Point = Point(10.0, 10.0)
test_point.scale_by(4)
print(test_point.x)
print(test_point.y)
print(test_point.scale(5))
