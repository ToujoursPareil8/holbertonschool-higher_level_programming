#!/usr/bin/python3
"""
    Docstring pour task_02_verboselist
"""


class VerboseList(list):
    """
        Liste qui affiche des messages lors des modifications
    """

    def append(self, el):
        """ Ajoute un élément et affiche un message """
        super().append(el)
        print(f"Added [{el}] to the list.")

    def extend(self, els):
        """ Étend la liste avec plusieurs éléments """
        super().extend(els)
        print(f"Extended the list with [{len(els)}] items.")

    def remove(self, el):
        """ Retire un élément de la liste """
        print(f"Removed [{el}] from the list.")
        super().remove(el)

    def pop(self, index=-1):
        """ Récupère l'élément avant de le retirer """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
