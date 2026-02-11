#!/usr/bin/python3
"""
    Demonstration of mixins with a Dragon class
"""


class SwimMixin:
    """ Mixin that adds swimming capability """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """ Mixin that adds flying capability """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """ Dragon that can swim and fly using mixins """

    def roar(self):
        print("The dragon roars!")
