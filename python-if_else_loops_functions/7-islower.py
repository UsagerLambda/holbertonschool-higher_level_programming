#!/usr/bin/python3
def islower(c):
    i = 0
    for i in range(97, 123):
        if c == chr(i):
            return True
    return False
