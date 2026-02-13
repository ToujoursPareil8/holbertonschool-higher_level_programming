#!/usr/bin/python3
"""
    function that writes a text file
"""


def write_file(filename="", text=""):
    """
        Uses 'with' to open a file and write to it
    """
    with open(filename, 'w', encoding='utf-8') as f:
        """
            Writes a string to a text file and
            returns the number of characters written
        """
        return f.write(text)
