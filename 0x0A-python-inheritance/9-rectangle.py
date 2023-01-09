#!/usr/bin/python3
"""Defines a rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
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

    def area(self):
        """Implements area of rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """Returns the string representation of Rectangle"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.width) + "/" + str(self.height)
        return string
