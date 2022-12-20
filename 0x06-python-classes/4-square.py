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

    @property
    def size(self):
        """Retrieve the size property
            Return: size (int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the new value to size
            Args: value (int)
        """
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("sie must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the sqaure area
            Args: Nothing
            Return:
                square of size
        """
        return self.__size ** 2
