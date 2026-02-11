#!/usr/bin/python3
"""
    Demonstration of multiple inheritance with FlyingFish
"""


class Fish:
    """ Represents a fish that swims in water """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """ Represents a bird that flies in the sky """

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
        Flying fish that inherits from both Fish and Bird
        MRO: FlyingFish -> Fish -> Bird -> object
    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        """ Override pour résoudre le conflit entre Fish et Bird """
        print("The flying fish lives both in water and the sky!")
