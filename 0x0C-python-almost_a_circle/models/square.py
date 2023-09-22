#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class deals with the properties of a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter method for the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size of the square."""
        self.width = value
        self.height = value

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

