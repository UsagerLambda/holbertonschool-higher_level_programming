#!/usr/bin/python3
import pickle


def serialize_and_save_to_file(data, filename):
    """
    Serializes the given data and saves it to a file.
    """
    with open(filename, "wb") as file:
        pickle.dump(data, file)

def load_and_deserialize(filename):
    """
    Loads and deserializes data from a file.
    """
    with open(filename, "rb") as file:
        loaded_data = pickle.load(file)
    return loaded_data
