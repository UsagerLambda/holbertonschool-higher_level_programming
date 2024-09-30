#!/usr/bin/python3
"""print the content of a file define by filename"""


def read_file(filename=""):
    """ Open and print in UTF-8 the file named by the variable filename. """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
