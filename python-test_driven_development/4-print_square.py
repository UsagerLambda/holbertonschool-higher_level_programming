#!/usr/bin/python3

def print_square(size):

    """
    Prints a square of `#` characters with the given size.

    Parameters:
    size (int): The size of the square (number of rows and columns).

    Returns:
    None

    Raises:
    TypeError: If `size` is not an integer.
    ValueError: If `size` is a negative integer.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
