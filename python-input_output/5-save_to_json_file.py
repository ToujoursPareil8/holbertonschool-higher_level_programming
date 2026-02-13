#!/usr/bin/python3
"""5 save to JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """
        Function that writes an Object to
        a text file, using a JSON representation
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
