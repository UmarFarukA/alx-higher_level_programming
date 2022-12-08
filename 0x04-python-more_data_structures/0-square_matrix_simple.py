#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            i = matrix[j][k]
            matrix[j][k] = i * i
    return (matrix)
