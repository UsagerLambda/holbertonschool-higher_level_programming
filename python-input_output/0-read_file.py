#!/usr/bin/python3


def read_file(filename=""):
    """
    Open and print in UTF-8 the file named by the variable filename.

    Args:
        filename (str, optional): the name of the file to open.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f)
