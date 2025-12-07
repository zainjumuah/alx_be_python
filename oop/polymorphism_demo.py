#!/usr/bin/env python3

import math


class Shape:
    """Base class for shapes."""

    def area(self):
        raise NotImplementedError("Subclasses must implement the area method")


class Rectangle(Shape):
    """Rectangle shape class."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """Circle shape class."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
