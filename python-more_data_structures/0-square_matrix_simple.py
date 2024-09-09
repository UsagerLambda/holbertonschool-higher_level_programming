#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for line in matrix:
        power = [i ** 2 for i in line]
        new_matrix.append(power)
    return new_matrix
