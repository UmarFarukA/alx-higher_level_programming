#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            i = k ** k
            matrix[j][k] = i
    return matrix
