#!/usr/bin/python3
"""Module that defines a function to check for a strict subclass."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    Instances of a_class itself do not count.

    Args:
        obj: the object to check.
        a_class: the class to compare with.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
