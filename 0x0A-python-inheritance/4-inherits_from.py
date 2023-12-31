#!/usr/bin/python3
""" a function that checks an instance of a class that inherited
    (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """
    a function that returns True if the object is an instance of
    a class that inherited (directly or indirectly) from the specified
    class ; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
