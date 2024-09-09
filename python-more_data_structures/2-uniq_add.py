#!/usr/bin/python3

def uniq_add(my_list=[]):
    output = []
    for x in my_list:
        if x not in output:
            output.append(x)
    result = 0
    for i in output:
        result += i
    return result
