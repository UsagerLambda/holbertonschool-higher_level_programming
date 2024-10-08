#!/usr/bin/python3

"""Module that provides a function to divide all elements
of a matrix by a given number."""


def matrix_divided(matrix, div):

    """ Divides all elements of a matrix by a given number.

    @matrix: A matrix (list of lists) where each element
    is an integer or float.
    @div: The number by which each element of the matrix will be divided.

    Returns: The matrix """

    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(type_error)

    for line in matrix:
        if not isinstance(line, list):
            raise TypeError(type_error)

    for line in matrix:
        for item in line:
            if not isinstance(item, (int, float)):
                raise TypeError(type_error)

    first_line = len(matrix[0])
    for line in matrix:
        if len(line) != first_line:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0 or div == float('inf') or div != div:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for line in matrix:
        new_line = []
        for item in line:
            new_line.append(round(item / div, 2))
        new_matrix.append(new_line)

    return new_matrix
