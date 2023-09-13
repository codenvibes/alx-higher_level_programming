#!/usr/bin/python3
# Auth: Terrence M.K
"""3-is_kind_of_class

This module defines a function called 'is_kind_of_class' that checks if
an object is an instance of a specified class or a subclass of
that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or a
    subclass of that class.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to check against.

    Returns:
        bool: True if 'obj' is an instance of 'a_class' or a subclass
        of 'a_class', otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False
