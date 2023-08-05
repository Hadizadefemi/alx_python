#!/usr/bin/env python3
"""BaseGeometry: contains a method area that is not implemented"""


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
        