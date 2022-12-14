#!/usr/bin/python3
"""Definese a function for File opereation"""


def write_file(filename="", text=""):
    """Function for writing to file
    Args:
        filename (str): Name of the file to write to
        text (str): Data for be written to filename
    Returns:
        Number of characters written to filename
    """
    with open(filename, "w", encoding="utf-8") as fw:
        fw.write(text)
    numChars = 0
    words = ""
    with open(filename, encoding="utf-8") as f:
        words = f.read()
    for word in words:
        for c in word:
            numChars += 1
    return (numChars)
