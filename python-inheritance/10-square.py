#!/usr/bin/python3
"""
Module defining the BaseGeometry class
for basic geometric shape operations.
"""


class BaseGeometry:
    """
    A class to represent basic geometric shapes.
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
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from the BaseGeometry class.
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
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle in the format
            '[Rectangle] width/height'.
        """
        return '[{}] {}/{}'.format(__class__.__name__,
                                   self.__width, self.__height)

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            str: The area of the rectangle as a string.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    Represents a square, inheriting from the Rectangle class.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size (int): The length of a side of the square.
            Must be a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Call the function area from the parent class

        Returns:
            The area of the square.
        """
        return super().area()
