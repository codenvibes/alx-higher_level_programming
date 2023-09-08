#!/usr/bin/python3
# Auth: Terrence M.K
# File: 0-add_integer.py

"""This script defines a function for integer addition."""


def add_integer(a, b=98):
    """Return the integer sum of 'a' and 'b'.

    If 'a' or 'b' are floating-point numbers, they will
    be converted to integers before the addition.

    Raises:
        TypeError: If either 'a' or 'b' is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
