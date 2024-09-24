#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract class representing a geometric shape.
    Each subclass must implement the `area` and `perimeter` methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculates and returns the area of the shape.
        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates and returns the perimeter of the shape.
        This method must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    Represents a circle with a given radius.
    """

    def __init__(self, radius):
        """
        Initializes a new circle with the specified radius.
        :param radius: Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        :return: Area of the circle.
        """
        return pi * (self.radius * self.radius)

    def perimeter(self):
        """
        Calculates and returns the perimeter of the circle.
        :return: Perimeter of the circle.
        """
        return (2 * self.radius) * pi


class Rectangle(Shape):
    """
    Represents a rectangle with a given width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a new rectangle with the specified width and height.
        :param width: Width of the rectangle.
        :param height: Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        :return: Area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        :return: Perimeter of the rectangle.
        """
        return (self.width + self.height) * 2


def shape_info(shape):
    """
    Displays the shape's information: its area and perimeter.
    :param Shape: Instance of a shape (must inherit from the Shape class).
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
