#!/usr/bin/python3
import pickle


class CustomObject:
    """
    A class to represent a custom object with attributes and methods
    for serialization and deserialization.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object in a formatted string.
        """

        print("Name: {}\nAge: {}\nIs Student: {}"
              .format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file using pickle.
        """

        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Loads a serialized object from a file.
        """

        with open(filename, "rb") as file:
            loaded_data = pickle.load(file)
        return loaded_data
