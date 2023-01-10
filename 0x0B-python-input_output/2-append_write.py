#!/usr/bin/python3
"""Definese a function for File opereation"""


def append_write(filename="", text=""):
    """Function for appending to file
    Args:
        filename (str): Name of the file to write to
        text (str): Data for be written to filename
    Returns:
        Number of characters written to filename
    """
    with open(filename, "a", encoding="utf-8") as fw:
        return fw.write(text)
