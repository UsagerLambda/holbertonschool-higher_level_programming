#!/usr/bin/python3
"""
Module defining the BaseGeometry class
for basic geometric shape operations.
"""


class BaseGeometry():
    """
    A class to represent basic geometric shapes.

    Methods
    -------
    area():
        Raises an Exception indicating that the area method is not implemented.

    interger_validator(name: str, value, int)
        Validate that value is a positive integer, if not raise an Exception
    """
    def area(self):
        """
        Public method that raise an Exception

        Raises:
            Exception: "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Parameters:
            name (str): The name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from the BaseGeometry class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(width, height): Initializes a new rectangle
        with the given width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with a specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
