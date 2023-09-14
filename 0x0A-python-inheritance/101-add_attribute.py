#!/usr/bin/python3
# Auth: codenvibes
"""101-add_attribute.py

This module defines a function for adding attributes to objects.
"""


def add_attribute(obj, att, value):
    """
    Add an attribute to an object.

    This function adds a new attribute, specified by 'att', with the given 'value'
    to the provided object 'obj'. It checks whether the object supports attribute
    assignment by verifying the presence of the '__dict__' attribute.

    Args:
        obj (object): The object to which the attribute will be added.
        att (str): The name of the attribute to be added.
        value (any): The value to be assigned to the new attribute.

    Raises:
        TypeError: If the provided object does not support attribute assignment.

    Example:
        >>> class ExampleObject:
        ...     pass
        >>> my_object = ExampleObject()
        >>> add_attribute(my_object, 'name', 'John')
        >>> print(my_object.name)
        John
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
