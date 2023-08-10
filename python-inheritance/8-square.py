#!/usr/bin/env python3
"""Square: A class representing a square"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Represents an object as a Square"""
    
    def __init__(self, size):
        """Initializes with the size of the square object"""
        super().integer_validator("size", size)
        self.__size = size
        
    def area(self):
        """calculates and returns the area of the square object"""
        return self.__size ** 2
    
    def __str__(self):
        """represents the square object with its size"""
        return f"[Rectangle] {self.__size}/{self.__size}"