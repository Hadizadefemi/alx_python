#!/usr/bin/env python3
"""BaseGeometry: A base class for any shape"""


class RemoveInitSubClassMeta(type):
    """overrides the dir attribute"""
    def __dir__(self):
        """removes __init_subclass from its attribute"""
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']
    
class BaseGeometry(metaclass=RemoveInitSubClassMeta):
    """Base class for any shape"""
    def __dir__(self):
        """removes __init_subclass from its attribute"""
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']
    
    def area(self):
        """Not implemented"""
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        """Checks if value is a positive integer"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        

class Rectangle(BaseGeometry):
    """Represents object as a rectangle"""
    
    def __init__(self, width, height):
        """Initializes with height and width"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height