#!/usr/bin/python3
"""Defines a function for checking instances"""


def is_kind_of_class(obj, a_class):
    """A function that checks instance of obj ofa a_class
    Args:
        obj: The object to check for an instance
        a_class: a class to check of obj of.
    Returns: True if obj is instance of a_class
        ortherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
