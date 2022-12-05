#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            print("{:d}".format(matrix[i][j]))
            if i != (len(matrix[j]) - 1):
                print(" ", end="")
        print("")
