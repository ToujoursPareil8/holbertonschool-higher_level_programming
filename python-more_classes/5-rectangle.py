#!/usr/bin/python3
"""
This is a class Rectangle that defines a rectangle by width and height.
"""


class Rectangle:
    """
    A class that defines a rectangle by its width and height.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle.
        If width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for _ in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle for eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when the rectangle is deleted."""
        print("Bye rectangle...")
