#!/usr/bin/python3
"""
Function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class ;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj: The object to check.
        a_class: type: (bool): The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited
        from a_class (excluding a direct instance of a_class).
        Otherwise, False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
