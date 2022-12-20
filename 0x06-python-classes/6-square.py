#!/usr/bin/python3


"""Defines class Square"""


class Square:
    """Represent class square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initiallize a new square
            Args:
                size: (int) default to 0
                position: (tuple) default to 0, 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the size property"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the property"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the sqaure area
            Return:
                square of size
        """
        return self.__size ** 2

    def my_print(self):
        """Prints square based on size"""
        if self.__size == 0:
            print("")
            return
        for k in range(0, self.__position[1]):
            print("")
        for j in range(0, self__position[0]):
            print(" ", end="")
        for i in range(0, self.__size)):
            print("#", end="")
        print("")
