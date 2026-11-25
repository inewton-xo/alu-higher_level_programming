#!/usr/bin/python3
"""Module that defines a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file, overwriting it if it exists.

    Args:
        filename (str): the name of the file to write.
        text (str): the string to write.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
