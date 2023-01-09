#!/usr/bin/python3
"""Defines a class checking function"""


def is_same_class(obj, a_class):
    """Defines function for checking instance of a class
    Args:
        obj: The object to check if an instance of a class
        a_class: The class use
    Returns:
        True if obj is of type class ortherwise False
    """
    if type(obj) == a_class:
        return True
    return False
