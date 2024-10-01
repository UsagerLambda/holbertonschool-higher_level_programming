#!/usr/bin/env python3
"""
Importation du module pickle qui permet la sérialisation
et la désérialisation d'objets Python.
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    Serializes the given data and saves it to a file.
    """
    with open(filename, "w") as file:
        pickle.dump(data, file)

def load_and_deserialize(filename):
    """
    Loads and deserializes data from a file.
    """
    with open(filename, "r") as file:
        loaded_data = pickle.load(file)
    return loaded_data
