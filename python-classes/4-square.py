#!/usr/bin/env python3
"""Defines a class Square"""

class Square:
    """Represents an object as a Square
    
    Private instance attribute: size
    """

    def __init__(self, size=0):
        """Initialize square object with default size 0"""
        self.__size = size

    @property
    def size(self):
        """returns the size of the square object"""
        return self.__size
    
    @size.setter
    def size(self, size=0):
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
    
    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()