#!/usr/bin/python3
def uppercase(str):
    string = ""  # Initialise une chaîne vide
    for i in str:  # 'i' parcourt la chaîne de caractères 's'
        if 'a' <= i <= 'z':  # Vérifie si 'i' est compris entre 'a' et 'z'
            string += chr(ord(i) - 32)  # ord(i) convertit 'i' en ASCII,
            # puis on soustrait 32 pour obtenir l'équivalent majuscule du char
            # Ensuite, on reconvertit le code ASCII en caractère (chr)
            # et on stocke ce caractère dans la variable 'string'
        else:
            string += i  # Si le caractère n'est pas une minuscule,
            # on l'ajoute tel quel dans la variable 'string'
    print(string)
