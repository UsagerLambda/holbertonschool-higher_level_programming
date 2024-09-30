#!/usr/bin/python3
"""function that write a string to a text file
and returns the number of characters written"""


def write_file(filename="", text=""):
    """
    Return the number of char in the file in the variable filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        content = f.write(text)
        return content
