#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in ".?:":
            new_text += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print(new_text)
