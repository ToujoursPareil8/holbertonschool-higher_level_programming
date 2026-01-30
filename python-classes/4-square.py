#!/usr/bin/python3
"""
This is class Square that defines a square by size.
"""


class Square:
    """
    A class that defines a square by its size.
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
