#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for first in matrix:
        for i, second in enumerate(first):
            if i > 0:
                print(" ", end='')
            print("{:d}".format(second), end='')
        print()  # Move to the next line after each row
