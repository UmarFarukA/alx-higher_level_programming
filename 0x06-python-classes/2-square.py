#!/usr/bin/python3


"""Defines a class Square"""


class Square:
    """Represents a class square"""

    def __init__(self, size=0):
        """Initialize a new sqaure
            Args:
                size: (int) optional & defaullt to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
