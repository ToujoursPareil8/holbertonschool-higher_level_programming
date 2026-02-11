#!/usr/bin/python3
"""
    Iterator that counts the number of items iterated
"""


class CountedIterator:
    """
        Wraps an iterator and tracks iteration count
    """

    def __init__(self, _iterable):
        """ Convertit l'itérable en itérateur """
        self.iterator = iter(_iterable)
        self.count = 0

    def get_count(self):
        """ Retourne le nombre d'éléments itérés """
        return self.count

    def __next__(self):
        """ Récupère l'élément suivant et incrémente le compteur """
        item = next(self.iterator)
        self.count += 1
        return item
