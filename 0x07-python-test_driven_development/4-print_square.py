#!/usr/bin/python3
"""Defines a function that prints a square"""


def print_square(size):
    """Print square with a # character
    Args:
        size (int): The size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for j in range(size):
        for i in range(size):
            print("#", end="")
        print("")
