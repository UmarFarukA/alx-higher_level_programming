#!/usr/bin/python3


"""Defines a class Rectangle"""


class Rectangle:
    """Represent a rectangle class
    Attributes:
        number_of_instances (int): The number of instances
        print_symbol (any): The symbol for printing
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle class
        Args:
            width: (int) width of rectangle (default, 0)
            height: (int) height of rectangle (default, 0)
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        """Returns rectangle with size==width==height
        Args:
            size (int): width and height of new Rectangle
        """
        return(cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles
        Args:
            rect_1(Rectangle): First instance
            rect_2(Rectangle): Second Instance
        Raises:
            TypeError: If either is not an instance of Rectangle
        Return:
            Biggest or equla
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

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
            [rec.append(str(self.print_symbol)) for i in range(w)]
            if j != h - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """Returns string representation of rectangle"""
        rec = "Rectangle(" + str(self.width)
        rec += ", " + str(self.height) + ")"
        return (rec)

    def __del__(self):
        """print a message after deletion rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
