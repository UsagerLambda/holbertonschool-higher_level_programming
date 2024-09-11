#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    skip = False
    for i in range(len(text)):
        if text[i] == ' ' and skip:
            continue
        new_text += text[i]
        skip = False
        if text[i] in ".?:":
            new_text += "\n\n"
            skip = True
        else:
            skip = False
    print(new_text)
