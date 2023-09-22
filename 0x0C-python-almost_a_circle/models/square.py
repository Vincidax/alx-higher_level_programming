#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    """This class deals with the properties of a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square."""
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}"

    # Private instance attribute for size
    @property
    def size(self):
        """Getter method for the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value
        self.width = value
        self.height = value

    # Private instance attribute for x
    @property
    def x(self):
        """Getter method for the x-coordinate of the square."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x-coordinate of the square."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Private instance attribute for y
    @property
    def y(self):
        """Getter method for the y-coordinate of the square."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y-coordinate of the square."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square instance."""
        if args:
            arg_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

