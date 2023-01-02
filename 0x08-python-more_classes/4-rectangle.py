#!/usr/bin/python3


"""Defines a class Rectangle"""


class Rectangle:
    """Represent a rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle class
        Args:
            width: (int) width of rectangle (default, 0)
            height: (int) height of rectangle (default, 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """Computes the perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.height + self.width))

    def __str__(self):
        """Prints representation of rectangle
        using the #
        """
        if self.width == 0 or self.height == 0:
            return ("")
        w = self.width
        h = self.height
        rec = []
        for j in range(h):
            [rec.append("#") for i in range(w)]
            if j != h - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """Returns string representation of rectangle"""
        rec = "Rectangle(" + str(self.width)
        rec += "," +str(self.height) + ")"
        return (rec)
