#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    skip = False
    for i in range(len(text)):
        if text[i] == ' ' and skip:
            continue
        skip = False
        new_text += text[i]
        if text[i] in ".?:":
            new_text += "\n\n"
            skip = True
    print(new_text)
