#!/usr/bin/env python3
"""BaseGeometry: A base class for any shape"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents object as a rectangle"""
    
    def __init__(self, width, height):
        """Initializes with height and width"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
