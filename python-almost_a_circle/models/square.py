#!/usr/bin/env python3
"""This module defines a Square class that inherits from Rectangle class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents objects as a square
    
    Attributes:
        size (int): The size of the square (width/height).
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square (width/height).
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): The id to assign to the instance. If not provided,
                                a new id is generated.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square (width/height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (width/height).

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            str: The formatted string representing the square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
