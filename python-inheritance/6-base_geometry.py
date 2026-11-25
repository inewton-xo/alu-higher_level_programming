#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """A geometry class with an unimplemented area method."""

    def area(self):
        """Raise an Exception, as area is not implemented here."""
        raise Exception("area() is not implemented")
