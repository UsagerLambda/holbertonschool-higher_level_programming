#!/usr/bin/python3

"""
This module defines a class named Rectangle.

The Rectangle class represents a rectangle with a specified width and height.
It includes methods to get and set these dimensions, ensuring that they are
non-negative integers.

The class includes the following methods:
    - __init__(self, width=0, height=0): Initializes the rectangle
    with the given width and height.
    - width(self): Getter for the width property.
    - width(self, value): Setter for the width property.
    - height(self): Getter for the height property.
    - height(self, value): Setter for the height property.
"""


class Rectangle():
    """
    A class used to represent a rectangle.

    Attributes:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        Returns the height of the rectangle.

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle, ensuring it is a
        non-negative integer.

        Args:
            value (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Return the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle, ensuring it is a non-negative integer.

        Args:
            value (int): The width of the rectangle

        Raises:
            TypeError: If width is not a integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns: float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns: float: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
