#!/usr/bin/python3
"""Defines a function that display attributes"""


def lookup(obj):
    """Returns the list of obj
    Args:
        obj: A class
    Returns:
        Collection of attributes and Methods
    """
    return (dir(obj))
