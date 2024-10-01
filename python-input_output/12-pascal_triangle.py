#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Generates the Pascal's triangle up to the n-th row."""
    if n <= 0:
        return ()

    # initialise une liste avec la première ligne du triangle de Pascal
    triangle = [[1]]

    # boucle qui va de 1 à n-1 (on ne start pas à 0 car la ligne existe déja)
    for i in range(1, n):
        # pour chaque lignes on ajoute le premier élément qui est toujours 1
        row = [1]
        # deuxieme boucle qui itere de 1 à i-1
        for j in range(1, i):
            # ajoute l'élément correspondant à la valeur des deux éléments
            # correspondants de la ligne précédente
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # ajoute 1 car chaque ligne du triangle se termine par 1
        row.append(1)
        # on ajoute la ligne fini à triangle
        triangle.append(row)
    return triangle
