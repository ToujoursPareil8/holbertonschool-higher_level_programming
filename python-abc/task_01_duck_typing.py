#!/usr/bin/python3
"""
    File class for multiple shapes using Abstract Base Classes.
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
        Abstract base class for geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
            Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
            Calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
        Represents a circle shape.
    """

    def __init__(self, radius):
        """
            Initialize a circle with the given radius.

            Args:
                radius: The radius of the circle.
        """
        self.__radius = radius

    def area(self):
        """
            Calculate the area of the circle.

            Returns:
                The area of the circle (π × r²).
        """
        return pi * self.__radius ** 2

    def perimeter(self):
        """
            Calculate the perimeter (circumference) of the circle.

            Returns:
                The perimeter of the circle (2 × π × r).
        """
        return 2 * pi * abs(self.__radius)


class Rectangle(Shape):
    """
        Represents a rectangle shape.
    """

    def __init__(self, width, height):
        """
            Initialize a rectangle with the given width and height.

            Args:
                width: The width of the rectangle.
                height: The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
            Calculate the area of the rectangle.

            Returns:
                The area of the rectangle (width × height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Calculate the perimeter of the rectangle.

            Returns:
                The perimeter of the rectangle (2 × (width + height)).
        """
        return (self.__width + self.__height) * 2


def shape_info(shape):
    """
        Display the area and perimeter of a shape using duck typing.

        Args:
            shape: An object that implements area() and perimeter() methods.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
