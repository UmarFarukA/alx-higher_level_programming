#!/usr/bin/python3
"""Defines function for writing object to text files"""


import json


def save_to_json_file(my_obj, filename):
    """Represent function for saving objectt to file
    Args:
        my_obj: The object to be save
        filename: Name of file
    """
    with open(filename, "w", encoding="utf-8") as fw:
        fw.write(my_obj)
