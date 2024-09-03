#!/usr/bin/python3
def pow(a, b):
    if b == 0: # si b = 0 retourne 1 car a^0 = 1
        return 1
    elif b > 0:
        result = 1 # initialise 'result' à 1
        for _ in range(b):
            result *= a # On multiplie 'result' par 'a', 'b' fois
        return result
    else:  # si b est négatif
        positive_b = -b 
        result = 1
        for _ in range(positive_b):
            result *= a
        return 1 / result # retourne l'inverse de result

