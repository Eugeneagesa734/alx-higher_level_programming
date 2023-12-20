#!/usr/bin/python3
"""
The "square" module.

A simple class with an initial size is provided in this module
Size is set to 0 by default. if a size input is incorrect, raise an error
Squares area is returned by the method area
"""


class Square:
    """A class that calculates area and specifies a square by size"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
