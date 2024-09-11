#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints a greeting message with the provided first and last name.

    Parameters:
    first_name (str): The first name to be included in the greeting message.
    last_name (str, optional): The last name to be included in the greeting message. Defaults to an empty string.

    Returns:
    None

    Raises:
    TypeError: If `first_name` or `last_name` is not a string, or if both `first_name` and `last_name` are empty.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if (len(first_name) + len(last_name)) == 0:
        raise TypeError("say_my_name need arguments")

    print("My name is {} {}".format(first_name, last_name))
