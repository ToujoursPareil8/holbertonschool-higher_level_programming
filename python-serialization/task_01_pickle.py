#!/usr/bin/python3
"""
    Module for serializing and deserializing custom objects using pickle.
"""
import pickle


class CustomObject:
    """A custom class to demonstrate pickle serialization."""

    def __init__(self, name, age, is_student):
        """
            Initializes the CustomObject instance.

            Args:
                name (str): The name of the person.
                age (int): The age of the person.
                is_student (bool): Whether the person is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file.

        Args:
            filename (str): The name of the file to save to
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file.

        Args:
            filename (str): The name of the file to load from

        Returns:
            CustomObject: The deserialized object, or None if an error occurs
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
