#!/usr/bin/python3

"""
Class square with private instance attribute 'size'

In def __init__
We check if size is a integer and not < 0

In def area
We return the area of the square

"""


class Square():
    """ Class that define a square """
    def __init__(self, size=0):
        """
        'size' for the size of the square to initialize.
        The size is store as a private attribute.

        The first condition check if size is a integer,
        if not raise a TypeError

        The second condition check if size not < 0,
        if not raise a ValueError
        """
        self.__size = size  # Private Attribute ("__")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        return the area of the square (size * size)
        """
        return self.__size * self.__size
