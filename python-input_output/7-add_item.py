#!/usr/bin/python3
"""
Adds all command line arguments to a list,
then saves this list to a JSON file.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Assigne le nom du fichier JSON à une variable
filename = "add_item.json"

# Tente de charger le contenu du fichier JSON existant dans 'items'
try:
    # Charge les données si le fichier existe
    items = load_from_json_file(filename)
except FileNotFoundError:
    # Si le fichier n'existe pas, initialise une liste vide
    items = []

# Ajoute les nouveaux arguments (en excluant le nom du script) à la liste
items.extend(sys.argv[1:])

# Sauvegarde la liste mise à jour dans le fichier JSON
save_to_json_file(items, filename)
