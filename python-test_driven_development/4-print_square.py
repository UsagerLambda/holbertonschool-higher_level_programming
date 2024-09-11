#!/usr/bin/python3

"""Module that provides a function to print
a square of `#` characters with the given size."""


def print_square(size):

    """ Prints a square of `#` characters with the given size.

    @size: The size of the square (number of rows and columns). """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
