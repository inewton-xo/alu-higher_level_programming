#!/usr/bin/python3
"""Module that defines MyList, a list that can print itself sorted."""


class MyList(list):
    """A list with a method that prints its items in ascending order."""

    def print_sorted(self):
        """Print the list sorted in ascending order.

        The list itself is not modified.
        """
        print(sorted(self))
