#!/usr/bin/python3
"""Defines a class Base"""
import json


class Base:
    """Represents the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class
        Args:
            id (int): Id to use defaultto None
        """
        if id not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that writes JSON string list_objs
        to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                lst = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON strong representations"""
        if json_string is None:
            return ("[]")
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Function that return all attributes instance set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Function for returning list of instances"""
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename, "r", encoding="utf-8") as fr:
                instances = cls.from_json_string(fr.read())
            for i, dct in enumerate(instances):
                instance_list.append(cls.create(**instances[i]))
        except:
            pass
        return instance_list
