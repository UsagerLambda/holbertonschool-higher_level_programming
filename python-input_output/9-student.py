#!/usr/bin/python3
"""class Student with public attributes"""


class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representing the student."""
        return self.__dict__
