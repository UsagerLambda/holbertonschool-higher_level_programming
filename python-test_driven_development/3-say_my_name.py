#!/usr/bin/python3

"""
Module that provides a function to print a greeting with the given first and last name.
"""

def say_my_name(first_name, last_name=""):

    """
    Prints a greeting message with the provided first and last name.

    @first_name: The first name to be included in the greeting message.
    @last_name: The last name to be included in the greeting message. Defaults to an empty string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if (len(first_name) + len(last_name)) == 0:
        raise TypeError("say_my_name need arguments")

    print("My name is {} {}".format(first_name, last_name))
