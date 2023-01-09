#!/usr/bin/python3
def add_integer(a, b=98):
    """Returns the additon of two integers
    Args:
        a (int/floats): The first operand
        b (int/floats): The second operand, default 98
    Raise:
        TypeError - if not an int or float
    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(a, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
