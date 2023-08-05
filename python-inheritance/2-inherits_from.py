#!/usr/bin/env python
"""A function that checks if an object is an instance
of a class that inherits directly or indirectly
"""

def inherits_from(obj, a_class):
    """checks if an object is an instance of a 
    class that inherits directly or indirectly
    
    Args:
        obj: object/instance of a class
        a_class: the specified class
        
    Returns:
        bool: True if object is an instance of the class, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class