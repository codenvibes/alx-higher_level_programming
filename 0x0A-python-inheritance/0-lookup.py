#!/usr/bin/python3
# Auth: Terrence M.K
# File: 0-lookup.py
"""
This module provides a function for looking up the attributes and methods
of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return (dir(obj))
