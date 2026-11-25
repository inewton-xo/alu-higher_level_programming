#!/usr/bin/python3
"""Module that defines a Student class that can be saved and reloaded."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student.

        Args:
            first_name (str): the first name.
            last_name (str): the last name.
            age (int): the age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the student.

        Args:
            attrs (list): if it is a list of strings, only the attributes
                whose names are in this list are returned. Otherwise, all
                the attributes are returned.
        """
        if isinstance(attrs, list) and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the attributes of the student from a dictionary.

        Args:
            json (dict): the keys are the public attribute names and the
                values are the new values of those attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
