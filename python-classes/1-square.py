#!/usr/bin/python3
"""Module that defines a Square class with a private size."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size: size of the square.
        """
        self.__size = size
