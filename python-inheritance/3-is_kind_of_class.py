#!/usr/bin/python3
"""Module that defines a function to check for a class or a subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass of it.

    Args:
        obj: the object to check.
        a_class: the class to compare with.
    """
    return isinstance(obj, a_class)
