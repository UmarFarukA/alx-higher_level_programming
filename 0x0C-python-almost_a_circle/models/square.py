#!/usr/bin/python3
"""Defines a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class, Sqaure"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Sqaure class
        Args:
            size (int): Square size
            x (int): The x coordinate of square
            y (int): The y coordinate of square
            id (int): Square id, default to None
        """
        super().__init__(id, size, size, x, y)

    @property
    def size(self):
        """Return the size of Square"""
        return self.size

    @size.setter
    def size(self, value):
        """Set new value for square width & height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """A function for update the square properties
        Args:
            args: A variable no key-word arguments
                  which are in order.
            kwargs: A variable key-word arguments that
                    are in order.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    
    def to_dictionary(self):
        """Returns dictionary representation of square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }
