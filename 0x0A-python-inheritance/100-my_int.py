#!/usr/bin/python3
"""Defines a MyInt class"""


class MyInt(int):
    """Represents MyInt class that inherits from int"""
    def __eq__(self, value):
        """Change == with != operator
        Args:
            value: value to be change
        """
        self.real != value

    def __ne__(self, value):
        """change != behaviour with ==
        Args:
            value: operand to be chnage
        """
        self.real == value
