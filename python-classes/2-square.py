#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Represents an object as a Square
    
    Private instance attribute: size
    """
    
    def __init__(self, size=0):
        """Initialize square object with default size 0"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        
        self.__size = size
        
    def area(self):
        """calculates the area the square object
        
        Returns:
            The area of the square
        """
        return self.__size ** 2
        