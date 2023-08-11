#!/usr/bin/env python3
"""This module defines a base class named Base."""


class Base:
    """A base class for other classes.
    
    Attributes:
        id (int): The unique identifier for the object.
        __nb_objects (int): A private class attribute to keep track of the number
        of instances created.
    """
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initialize a new Base instance with an optional id.
        
        Args:
            id (int, optional): The id to assign to the instance. If not provided,
            a new id is generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
