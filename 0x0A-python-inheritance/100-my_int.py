#!/usr/bin/python3
# Auth: Terrence M.K
"""100-my_int.py

This module defines a custom integer class called MyInt, which inherits
from the built-in int class.
"""


class MyInt(int):
    """
    Custom integer class that overrides equality and inequality comparisons.
    """
    def __eq__(self, value):
        """
        Custom equality comparison (__eq__) method.

        Args:
            value (int): The value to compare with.

        Returns:
            bool: True if the real part of this MyInt is not equal to the given value, False otherwise.
        """
        return self.real != value
    
    def __ne__(self, value):
        """
        Custom inequality comparison (__ne__) method.

        Args:
            value (int): The value to compare with.

        Returns:
            bool: True if the real part of this MyInt is equal to the given value, False otherwise.
        """
        return self.real == value
