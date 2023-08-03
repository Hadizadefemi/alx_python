#!/usr/bin/env python3
"""Defines a class Square"""

class Square:
    """Represents an instance as a Square
    
    Private instance attribute: size
    """
    
    def __init__(self, size=0):
        """Initialize square object with size"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must >= 0')

        self.__size = size