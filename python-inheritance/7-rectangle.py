"""Rectangle: A child class of BaseGeometry representing a rectangle"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents object as a rectangle"""
    
    def __init__(self, width, height):
        """Initializes with height and width"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
        
    def area(self):
        """calculates and returns the area of the rectangle object"""
        return self.__width * self.__height
    
    def __str__(self):
        """prints rectangle object as its height and width"""
        return f"[Rectangle] {self.__width}/{self.__height}"