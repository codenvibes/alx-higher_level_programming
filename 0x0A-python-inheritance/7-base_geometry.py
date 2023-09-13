#!/usr/bin/python3
"""7-base_geometry.py

This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    The BaseGeometry class defines basic geometric operations.
    """

    def area(self):
        """
        Placeholder method for calculating the area of a geometric shape.

        Raises:
            Exception: This exception is raised to indicate that the area()
                method is not implemented in the current subclass.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate if a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
