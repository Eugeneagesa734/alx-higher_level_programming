#!/usr/bin/python3
"""
class rectangle is defined by width and height
"""

class Rectangle:
    """rectangle representation"""
    def __init__(self, width=0, height=0):
        """The initializer rectangle class

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """int: The width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            """Setter for the private instance of class width."""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """int: The height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """setter for the private instance of the attribute height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.height__ = value

