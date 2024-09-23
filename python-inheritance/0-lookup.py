#!/usr/bin/python3
"""
This script defines a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list containing the names of the object's
        available attributes and methods.
    """
    return dir(obj)
