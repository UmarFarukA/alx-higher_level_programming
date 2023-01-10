#!/usr/bin/python3
"""Defines a function for inserting a line in file"""


def append_after(filename="", search_string="", new_string=""):
    """Function that replace new_string after serach_string
    Args:
        filename: The file to search for seaerech_string
        search_string (str): The string we want tosearch
        new_string (str): The string we replace
    """
    words = ""
    with open(filename, encoding="utf-8") as fr:
        for word in fr:
            words += word
            if search_string in word:
                words += new_string
    with open(filename, "w", encoding="utf-8") as fw:
        fw.write(words)
