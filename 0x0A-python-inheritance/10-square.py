#!/usr/bin/python3
"""Defines a square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square class"""
    def __init__(self, size):
        """Initializes the square class
        Args:
            size (int): size of square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Implements area of size"""
        return (self.__size ** 2)
