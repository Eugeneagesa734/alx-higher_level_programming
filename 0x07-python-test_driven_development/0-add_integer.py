#!/usr/bin/python3
"""Defines an integer addition function"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a (int or float): 1st number
    b (int or float): 2nd number. Default value 98.

    Returns:
    int: sumation of a and b.

    Raises:
    TypeError: if a or b is neither an integer nor float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
