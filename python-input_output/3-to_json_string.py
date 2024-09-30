#!/usr/bin/python3
import json
""" Function taht returns the JSON representation of an object """


def to_json_string(my_obj):
    """Return the json representation of my_obj"""
    return json.dumps(my_obj)
