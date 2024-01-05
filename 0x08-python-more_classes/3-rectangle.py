#!/usr/bin/python3
"""Class for rectangle is defined."""


class Rectangle:
    """A rectangle is represented."""

    def __init__(self, width=0, height=0):
        """Initialization of a new Rectangle.

        Args:
            width (int): Therectangles width.
            height (int): The rectangles height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """setter for the width of the Rectangle."""
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
        """Setter for the rectangles height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle is returned."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter of the rectangle is returned."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """The printiable representation of a rectangle is returned.

        A rectangle is represented by the hash character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
