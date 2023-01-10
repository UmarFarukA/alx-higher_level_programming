#!/usr/bin/python3
"""Definese a function for File opereation"""


def write_file(filename="", text=""):
    """Function for writing to file
    Args:
        filename (str): Name of the file to write to
        text (str): Data for be written to filename
    """
    with open(filename, "w", encoding="utf-8") as fw:
        fw.write(text)
