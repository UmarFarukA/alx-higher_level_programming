#!/usr/bin/python3
"""Function that checks for instance of a class"""


def inherits_from(obj, a_class):
    """This function checks if obj is an instance of a class
    Args:
        obj: Object if is an instance of a class
        a_class: The class to check
    Returns: True if obj is an instance of a class
        otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
