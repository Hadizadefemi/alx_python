#!/usr/bin/env python3
"""A function that checks if an object is an instance of a class"""

def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class
    
    Args:
        obj: object of a class
        a_class: specified class
        
    Returns:
        bool: True if object is an instance of the class, False otherwise
    """
    return type(obj) == a_class