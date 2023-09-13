#!/usr/bin/python3
'''function for serialization of an object'''


import json


def class_to_json(obj):
    '''obj is an instance of a Class
    Prototype: def class_to_json(obj)'''

    if not hasattr(obj, '__class__'):
        raise ValueError("Input object must be an instance of a class")

    serializable_types = (list, dict, str, int, bool)
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, serializable_types):
            result[key] = value
        else:
            raise ValueError(f"Attribute '{key}' is not serializable")

    return result
