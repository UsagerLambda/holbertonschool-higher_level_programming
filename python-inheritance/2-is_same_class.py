#!/usr/bin/python3
"""
Function that return "True" if the object is exactly an instance
of the specified class ; otherwise return "False".
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare the type of obj to.

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
