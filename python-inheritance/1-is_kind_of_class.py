#!/usr/bin/env python3
"""A function that checks if an object is an instance of,
or if the object is indirectly a subclass of the class
"""

def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of,
    or if the object is indirectly a subclass of the class
    
    Args:
        obj: object of a class
        a_class: specified class
    
    Returns:
        bool: True if object is an instance of the class, False otherwise
    """
    return isinstance(obj, a_class)
