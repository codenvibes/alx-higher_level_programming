#1/usr/bin/python3
# Auth: Terrence M.K
"""2-is_same_class.py

This module defines a function to check if an object is an instance
of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to compare the object against.

    Returns:
        bool: True if the object is an instance of the specified class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
