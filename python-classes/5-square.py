#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Initialises the sqaure with the setter"""
        self.size = size
    @property
    def size(self):
        """Retrieves the size (getter)"""
        return self.__size
    @size.setter
    def size(self, value):
        "Sets the size with validation (setter)"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """ returns the area of the square """
        return self.__size ** 2
    def my_print(self):
        """prints the square to stdout with #"""
        if self.size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
