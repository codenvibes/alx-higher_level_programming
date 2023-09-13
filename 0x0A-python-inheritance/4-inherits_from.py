#!/usr/bin/python3
"""
Module: inheritance_utils.py

This module contains a utility function called "inherits_from" that
checks if an object inherits from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specified class.

    This function takes an object "obj" and a class "a_class" as input
    and checks if "obj" is a subclass of "a_class" while ensuring it
    is not the same as "a_class."

    Args:
        obj: The object to check for inheritance.
        a_class: The class to compare against.

    Returns:
        bool: True if "obj" inherits from "a_class" and is not the
        same as "a_class," False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
