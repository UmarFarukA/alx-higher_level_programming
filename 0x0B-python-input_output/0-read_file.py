#!/usr/bin/python3
"""Defines a function for File operations"""


def read_file(filename=""):
    """Function for reading a file
    Args:
        filename (str): name of file to be read
    """
    with open(filename, encoding="utf-8") as fr:
        print(fr.read(), end="")
