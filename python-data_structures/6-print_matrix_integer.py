#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    nb_lines = len(matrix)
    for i in range(nb_lines):
        print(" ".join(map(str, matrix[i])))
