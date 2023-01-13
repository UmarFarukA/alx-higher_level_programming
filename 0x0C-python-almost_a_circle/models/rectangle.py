#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle(Base):
    """Represents the Rectangle class
    Args:
        width (int): Width of Rectangle
        height (int): Height of Rectangle
        x (int): The x
        y (int): The y
        id (int): THe id of Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle Class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Return the Rectangle width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets new value fo rectangle width
        Args:
            value (int): Newrectangle width
        """
        if type(value) != int:
            raise TypeError("width must be an Integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of height"""
        return (self.__height)

    @width.setter
    def height(self, value):
        """Set new value for Rectangle height
        Args:
            height (int): New value for rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set new value for x"""
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """set new value for y"""
        if value <= 0:
            raise ValueError("y's value must be integer")
        self.__y = y

    def area(self):
        """Function that calculate Area of Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Display Rectangle instance with #"""
        for y in range(self.y):
            print("")
        for j in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for k in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Returns string representation of REctangle"""
        string = "[" + "("+str(self.id)+")"
        string += str(self.__x) + "/" + str(self.__y) + "-"
        string += str(self.__width) + "/" + str(sself.__height) + "]"
        return string

    def update(self, *args, **kwargs):
        """Represents an update function to REctangle
        Args:
            *args: A variable no key-word arguments
            **kwargs: A variable key-word arguments
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                if args[i] == 0:
                    self.id = args[i]
                elif args[i] == None:
                    self.__init__(self.width, self.height, self.x, self.y)
                    self.width = args[i]
                    self.height = args[i + 1]
                    self.x = args[i + 2]
                    self.y = args[i + 3]
                    break
                elif args[i] == 1:
                    self.width = args[i]
                elif args[i] == 2:
                    self.height = args[i]
                elif args[i] == 3:
                    self.x = args[i]
                elif args[i] == 4:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        seld.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
