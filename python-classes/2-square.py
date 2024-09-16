#!/usr/bin/python3

""" Class square with private instance attribute 'size' """


class Square():
    """ Class that define a square """
    def __init__(self, size=0):
        """
        'size' for the size of the square to initialize.
        The size is store as a private attribute.
        """
        self.__size = size  # Private Attribute ("__")
        if not isinstance(size, int):
            raise TypeError("size must be a integer")
        if size < 0:
            raise ValueError("size must be >= 0")
