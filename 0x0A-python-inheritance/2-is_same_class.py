#!/usr/bin/python3
def is_same_class((obj, a_class):
        """Defines function for checking instance of a class
        Args:
            obj: The object to check if an instance of a class
            a_class: The class use 
        """
        if not isinstance(obj, a_class):
            return False
        return True
