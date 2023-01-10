#!/usr/bin/python3
"""Definese function for JSON representation"""


import json


def from_json_string(my_str):
    """Function for return json representation"""
    return json.loads(my_str)
