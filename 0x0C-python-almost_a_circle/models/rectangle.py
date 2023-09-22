#!/usr/bin/python3
"""This inherits from Base.py. This manipulates a rectangle"""


from models.base import Base


class Rectangle(Base):
    """
    This class deals with the properties of a rectangle
        Args:
            width: width of a rectangle
            height: height of a rectangle
            x
            y
    """

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
