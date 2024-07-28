#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for first in matrix:
        for second in first:
            print(second, end=' ')
        print()
