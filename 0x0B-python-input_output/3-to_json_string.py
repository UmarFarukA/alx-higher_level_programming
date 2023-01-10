#!/usr/bin/python3
"""Definese function for JSON representation"""


import json


def to_json_string(my_obj):
    """Function for return json representation"""
    return json.dump(my_obj)
