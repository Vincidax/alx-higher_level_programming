#!/usr/bin/python3


import json


class Base:
    """Base class for managing instances."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance with an optional ID."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
