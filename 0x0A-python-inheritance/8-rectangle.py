#!/usr/bin/python3
"""8-rectangle.py

This module defines the Rectangle class, which inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

        Raises:
        - TypeError: If either width or height is not an integer.
        - ValueError: If either width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
