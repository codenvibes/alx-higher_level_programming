#!/usr/bin/python3
# Auth: codenvibes
"""10-square.py

This module defines a class called "Square" that inherits from the
"Rectangle" class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a specific type of
    rectangle with equal side lengths.

    Methods:
        __init__(self, size): Initializes a new Square instance with
        a given size.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance with the specified size.

        Args:
            size (int): The size (side length) of the square.

        Raises:
            ValueError: If the size is not a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
