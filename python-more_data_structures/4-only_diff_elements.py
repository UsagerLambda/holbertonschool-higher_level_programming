#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    output = []
    for x in set_1:
        if x not in set_2:
            output.append(x)
        else:
            pass
    for k in set_2:
        if k not in set_1:
            output.append(k)
        else:
            pass
    return output
