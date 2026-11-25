#!/usr/bin/python3
"""Module that defines a function to build Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Args:
        n (int): the number of rows. If n <= 0, an empty list is returned.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(n - 1):
        prev = triangle[-1]
        row = [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
        triangle.append(row)
    return triangle
