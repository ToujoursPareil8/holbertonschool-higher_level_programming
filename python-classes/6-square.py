#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialises the sqaure with the setter"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position (getter)"""
        return self.__position
    
    @position.setter
    def positon(self, value):
        """Sets the position with validation (setter)"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2
    
    def my_print(self):
        """prints the square to stdout with #"""
        if self.size == 0:
            print("")
            return
        [print("") for y in range(self.__position[1])]
        for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
