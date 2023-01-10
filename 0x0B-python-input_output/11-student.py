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

    def to_json(self, attrs=None):
        """Returns dict representation
        if attrs is list, attrs list must be retrieve
        """
        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of students
        Args:
            json (dict): key/value attributes
        """
        for k, v in json.items():
            setattr(self, k, v)
