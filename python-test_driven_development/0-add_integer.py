#!/usr/bin/python3

"""Module for adding intergers

Check if 'a' and 'b' are integer or float
if not raise a TypeError
else if 'a' or 'b' is a float
convert them into integers and add them """


def add_integer(a, b=98):

    """ Adds to numbers ('a' and 'b')
    after conversion into integers """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
