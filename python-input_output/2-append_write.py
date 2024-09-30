#!/usr/bin/python3
"""function that append a string to a text file
and returns the number of characters written"""


def append_write(filename="", text=""):
    """
    Return the number of char in the file in the variable filename
    """
    with open(filename, "a", encoding="utf-8") as f:
        content = f.write(text)
        return content
