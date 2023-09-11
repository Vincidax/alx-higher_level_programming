class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
            AttributeError: If an attribute is accessed improperly.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        elif hasattr(self, name):
            raise AttributeError(
                "'{}' object has no attribute '{}'".format(
                    type(self).__name__, name
                )
            )


class Rectangle(BaseGeometry):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()  # Call the constructor of the base class
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """Return the area of given width and height"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

