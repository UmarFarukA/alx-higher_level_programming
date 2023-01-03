#!/usr/bin/python3
"""Defines a function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Prints first_name last_name
    Args:
        first_name (string): First name of user
        last_name (string): Last name of user
    Raises:
        TypeError: If either is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
