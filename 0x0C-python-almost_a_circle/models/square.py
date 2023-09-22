#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class deals with the properties of a square."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
