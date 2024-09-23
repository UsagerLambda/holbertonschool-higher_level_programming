#!/usr/bin/python3
"""
function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance or inherits from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class or a parent class to compare against.

    Returns:
        True if obj is an instance of a_class
        or a class that inherited from it,
        otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
