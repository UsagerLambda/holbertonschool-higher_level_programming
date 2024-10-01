import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    # Crée l'élément racine
    # Crée l'élément racine du document XML
    root = ET.Element("data")

    # Itère sur les paires clé-valeur du dictionnaire
    for key, value in dictionary.items():
        # Crée un sous-élément sous la racine pour chaque clé
        item_element = ET.SubElement(root, key)
        # Convertit la valeur en chaîne de caractères et l'assigne à l'élément
        item_element.text = str(value)

    # Crée un arbre XML à partir de l'élément racine
    tree = ET.ElementTree(root)
    # Écrit l'arbre XML dans le fichier spécifié
    tree.write(filename)


def deserialize_from_xml(filename):
    # Analyse le fichier XML et obtient l'arbre
    tree = ET.parse(filename)
    # Obtient l'élément racine de l'arbre
    root = tree.getroot()

    # Initialise un dictionnaire vide pour stocker les résultats
    result = {}

    # Itère sur les sous-éléments de la racine
    for item in root:
        # La clé est le nom de l'élément XML
        key = item.tag
        # La valeur est le texte contenu dans l'élément
        value = item.text
        # Ajoute la paire clé-valeur dans le dictionnaire
        result[key] = value

    return result
