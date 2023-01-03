#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """Represents a LockedClass that prevents User
    from dynamicallycreating new instance attribute
    """
    __slots__ = ["first_name"]
