#!/usr/bin/python3
""" Function that create an Object from a Json file"""
import json


def load_from_json_file(filename):
    """ Function that create an Object from a Json file"""
    with open(filename, "r") as file:
        return json.load(file)
