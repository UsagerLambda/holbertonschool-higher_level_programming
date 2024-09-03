#!/usr/bin/python3
from add_0 import add  # Importe la fonction (def) add de add_0
if __name__ == "__main__":  # Vérifie si le script est executé directement
    a = 1
    b = 2
    result = add(a, b)  # result prend le resultat de l'appel de fonction 'add'
    print(f"{a} + {b} = {result}")
