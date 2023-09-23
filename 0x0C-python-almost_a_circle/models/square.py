#!/usr/bin/python3
# Auth: codenvibes
"""
This script defines a Square class that inherits from the Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class represents a square and inherits from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size (side length) of the square.
            x (int, optional): The x-coordinate of the square's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
            Defaults to 0.
            id (int, optional): The unique identifier of the square.
            Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets the size (side length) of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size (side length) of the square.

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string in the format "[Square] (id) x/y width".
        """
        return ("[Square] ({}) {}/{} {}".format(self.id, self.x, self.y,
                                                self.width))

    def update(self, *args, **kwargs):
        """
        Updates the Square object with new attributes.

        This method allows updating the attributes of the Square object
        using either positional arguments or keyword arguments. If using
        positional arguments, the order should be: id, size, x, and y.

        Args:
            *args: Variable-length argument list.
                If provided, should be in the order: id, size, x, y.
            **kwargs: Arbitrary keyword arguments.
                Accepts the following keyword arguments:
                - id (int): The new unique identifier of the square.
                - size (int): The new size (side length) of the square.
                - x (int): The new x-coordinate of the square's position.
                - y (int): The new y-coordinate of the square's position.

        Example usage:
            square = Square(2, 0, 0, 1)
            square.update(2, 3, 1, 1)
            # or
            square.update(size=3, x=1, y=1)

        Returns:
            None
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square object.

        This method creates and returns a dictionary containing the attributes
        of the Square object in the following format:
        {
            "id": (int) The unique identifier of the square,
            "size": (int) The size (side length) of the square,
            "x": (int) The x-coordinate of the square's position,
            "y": (int) The y-coordinate of the square's position
        }

        Returns:
            dict: A dictionary representation of the Square object.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
