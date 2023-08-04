#!/usr/bin/env python3
"""A function that checks if an object is an instance of,
or if the object is an instance of a class that inherited
from the specified class
"""

def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of,
    or if the object is an instance of a class 
    that inherited from the specified class
    
    Args:
        obj: object of a class
        a_class: specified class
    
    Returns:
        bool: True if object is an instance of the class, False otherwise
    """
    return isinstance(obj, a_class)