#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes the given data to JSON format and saves it to a file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it back to a Python object.
    """
    with open(filename, 'r') as file:
        return json.load(file)
