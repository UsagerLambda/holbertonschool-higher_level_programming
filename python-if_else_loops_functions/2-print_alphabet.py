#!/usr/bin/python3
for i in range(97, 123):  # 97 = 'a' & 123 = '{' (z + 1 dans la table ASCII)
    print(chr(i), end='')  # chr convertit le code ASCII en caractère,
    # end='' évite le saut de ligne
