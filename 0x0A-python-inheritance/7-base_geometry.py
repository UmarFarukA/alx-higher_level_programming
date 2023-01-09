#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Represents a class base geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer
        Args:
            name (string): name use
            value (int): The value to validates
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
