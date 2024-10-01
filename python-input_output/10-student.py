#!/usr/bin/python3
"""class Student with public attributes"""


class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a JSON representation of the Student instance.
        &
        Filters the instance attributes based on the provided list.
        """
        # Verif if attrs is a list
        if not isinstance(attrs, list):
            return self.__dict__

        filter = {}

        for items in attrs:  # boucle dans attrs
            #  Vérifie si l'élément bouclé dans attrs est bien une string
            #  Et vérifie si l'élément est bien un attribut de l'instance
            if isinstance(items, str) and hasattr(self, items):
                filter[items] = getattr(self, items)

        return filter
