#!/usr/bin/python3


"""Defines class Square"""


class Square:
    """Represent class square"""

    def __init__(self, size=0):
        """Initiallize a new square
            Args:
                size: (int) default to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the sqaure area
            Args: Nothing
            Return:
                square of size
        """
        return self.__size ** 2
