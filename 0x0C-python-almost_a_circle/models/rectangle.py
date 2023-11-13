#!/usr/bin/python3

""" class Rectangle that inherits from superclass Base"""

from models.base import Base

class Rectangle(Base):
    """subclass of superclass Base"""

def __init__(self, width, height, x=0, y=0, id=None):
    """Initialize instances for class rectangle"""
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    super().__init__(id)

@property
def width(self):
    """Retrive attribute"""
    return self.__width

@width.setter
def width(self, value):
    """settling and validate width"""
    if type(value) is not int:
        reaise TypeError("width should be an integer")
    if value <= 0:
        raise ValueError("width should be > 0")
    self.__width = value

@property
def height(self):
    """retive height"""
    return self.__height

@height.setter
def height(self,value):
    """set and validate height"""
    if type(value) is not int:
        raise TypeError("Height should be an integer")
    if value <= 0:
        raise ValueError("Height should be > 0")
    self.__height = value

@property
def x(self):
    """retreive x"""
    return self.___x

    @x.setter
    def x(self, value):
        """setting and validating x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting and validating y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
