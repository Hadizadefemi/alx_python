#!/usr/bin/env python3
""""""


class RemoveInitSubClassMeta(type):
    """overrides the dir attribute"""
    def __dir__(self):
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']
    
class BaseGeometry(metaclass=RemoveInitSubClassMeta):
    """removes __init_subclass from its attribute"""
    def __dir__(self):
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']
    
    def area(self):
        """Not implemented"""
        raise Exception('area() is not implemeted')