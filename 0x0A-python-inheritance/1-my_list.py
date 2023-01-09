#!/usr/bin/python3
"""Class that print sorted list"""


class MyList(list):
    """Class that print sorted list"""

    def print_sorted(self):
        """Function that prints sorted list"""
        print("{}".format(sorted(self)))
