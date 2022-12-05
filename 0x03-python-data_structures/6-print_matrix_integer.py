#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            print("{:d} {:d}".format(i, j))
