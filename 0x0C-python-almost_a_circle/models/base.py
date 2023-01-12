#!/usr/bin/python3
"""Defines a class Base"""


class Base:
    """Represents the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class
        Args:
            id (int): Id to use defaultto None
        """
        Base.__nb_objects += 1
        id = Base.__nb_objects
