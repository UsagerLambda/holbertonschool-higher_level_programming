#!/usr/bin/python3

def text_indentation(text):

    """
    Prints a text with two new lines after each of the following characters: `.`, `?`, and `:`.

    Parameters:
    text (str): The string to be processed.

    Returns:
    None

    Raises:
    TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    spec = {".", "?", ":"}
    start = 0
    for i in range(len(text)):
        if text[i] in spec:
            new_text = text[start:i + 1] + "\n\n"
            start = i + 1
            stripped = new_text.strip(" ")
            print("{}".format(stripped), end="")
    if start < len(text):
        remain = text[start:].strip()
        print("{}".format(remain), end="")
