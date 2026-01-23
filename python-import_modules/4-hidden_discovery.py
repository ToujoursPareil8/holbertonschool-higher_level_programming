#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Récupérer tous les noms définis dans le module
    names = dir(hidden_4)
    
    # Trier par ordre alphabétique
    names.sort()
    
    # Filtrer et afficher les noms qui ne commencent pas par "__"
    for name in names:
        if not name.startswith("__"):
            print(name)
