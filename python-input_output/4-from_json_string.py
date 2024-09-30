#!/usr/bin/python3
""" Function taht returns the object representation of an Json strings """
import json


def from_json_string(my_str):
    """ Return the object representation of a json strings """
    return json.loads(my_str)
