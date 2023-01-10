#!/usr/bin/python3
"""Defines a functioin that returns dictionary repre"""


import json

def class_to_json(obj):
    """Represents class to JSON"""
    return obj.__dict__
