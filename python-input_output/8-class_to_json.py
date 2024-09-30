#!/usr/bin/python3
"""Module that contains the class_to_json function."""

import json


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization."""
    return obj.__dict__
