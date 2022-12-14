#!/usr/bin/python3
"""Defines a function for creating Objects from JSON"""


import json


def load_from_json_file(filename):
    """Represents function for creating objects from JSON"""

    with open(filename, encoding="utf-8") as fr:
        return json.load(fr)
