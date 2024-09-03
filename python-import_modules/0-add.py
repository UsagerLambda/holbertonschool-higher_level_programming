#!/usr/bin/python3

from add_0 import add  # Importe la fonction (def) add de add_0

a = 1
b = 2

if __name__ == "__main__":  # Vérifie si le script est executé directement
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
