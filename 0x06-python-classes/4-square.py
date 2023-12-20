#!/usr/bin/python3
"""
module for "square"

An initialize size Square class is provided by this module.
Size is set to 0 by default. If a size input is incorrect, raise
Getter and Setter Methods prperties for size
size of area of square is returned by Methods
"""


class Square:
    """defines a square by size and computes the area"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
