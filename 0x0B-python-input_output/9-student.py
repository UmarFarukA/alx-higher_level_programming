#!/usr/bin/python3
"""Defines class students"""


class Student:
    """Represents a class students"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student class
        Args:
            first_name (str): Student first name
            last_name (str): Student last name
            age(int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict representation"""
        return self.__dict__
