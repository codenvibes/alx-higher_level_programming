#!/usr/bin/python3
# Auth: codenvibes
"""
This module defines a Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle with width, height, and position.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): The unique identifier for the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner of
            the rectangle.
            y (int, optional): The y-coordinate of the top-left corner of
            the rectangle.
            id (int, optional): The unique identifier for the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        int: The x-coordinate of the top-left corner of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        int: The y-coordinate of the top-left corner of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle, which is the product of its
            width and height.
        """
        return (self.width * self.height)

    def display(self):
        """
        Display the rectangle by printing it to the console.

        The rectangle is represented using '#' characters. The 'x' and 'y'
        attributes determine the offset from the top-left corner where the
        rectangle is drawn.

        Example:
            If 'x' is 2 and 'y' is 1, the rectangle will be indented by 2
            spaces horizontally and 1 space vertically before printing.

        Returns:
            None
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        The string includes information about the rectangle's ID, position
        (x, y), and dimensions (width, height).

        Returns:
            str: A string representation of the Rectangle instance.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance.

        This method allows you to update the attributes of the Rectangle
        instance using either positional arguments or keyword arguments.

        Args:
            *args: Positional arguments that can be used to update the
            attributes in the following order: id, width, height, x, y.
            **kwargs: Keyword arguments that can be used to update the
            attributes using attribute names as keys.

        Example:
            To update the width and height of a rectangle using positional
            arguments:
            >>> r = Rectangle(10, 20)
            >>> r.update(30, 40)
            >>> print(r)
            [Rectangle] (30) 0/0 - 10/20

            To update the x and y position of a rectangle using keyword
            arguments:
            >>> r = Rectangle(10, 20)
            >>> r.update(x=5, y=8)
            >>> print(r)
            [Rectangle] (1) 5/8 - 10/20

        Returns:
            None
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
