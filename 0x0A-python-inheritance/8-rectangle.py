#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle(BaeGeometry):
    """Represents a Rectangle class"""
    def __init__(self, width, height):
        """Initializes the rectangle class
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("Width", width)
        self.__width = width
        self.integer_validator("Height", height)
        self.__height = height

