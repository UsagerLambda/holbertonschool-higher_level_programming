#!/usr/bin/python3

""" Class square with private instance attribute 'size' """


class Square():
    """ Class that define a square """
    def __init__(self, size):
        """
        'size' for the size of the square to initialize.
        The size is store as a private attribute.
        """
        self.__size = size  # Private Attribute ("__")
