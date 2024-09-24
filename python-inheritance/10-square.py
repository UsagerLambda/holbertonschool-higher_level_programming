#!/usr/bin/python3
"""
Module defining the BaseGeometry class
for basic geometric shape operations.
"""


Rectangle = __import__('9-rectangle').Rectangle


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
        self.integer_validator('size', size)
        self.__size = size
        # super() appelle __init__ de la classe parent (Rectangle)
        # et lui donne size pour width & height
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Call the function area from the parent class

        Returns:
            The area of the square.
        """
        return super().area()
