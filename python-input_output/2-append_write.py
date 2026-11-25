#!/usr/bin/python3
"""Module that defines a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF8 text file.

    The file is created if it does not exist.

    Args:
        filename (str): the name of the file to append to.
        text (str): the string to append.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
