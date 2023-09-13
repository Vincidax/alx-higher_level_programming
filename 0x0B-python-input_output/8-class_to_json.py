#!/usr/bin/python3
'''function for serialization of an object'''


def class_to_json(obj):
    """
    Serialize an instance of a class with serializable
    attributes into a dictionary.

    Args:
        obj: An instance of a user-defined class with
        serializable attributes.

    Returns:
        dict: A dictionary representation of the serializable
        attributes of the object.

    Raises:
        ValueError: If the input object is not an instance of
        a user-defined class.
                    If any attribute is not serializable
                    (not of types list, dict, str, int, or bool).
    """
    
    result = {}
    for key, value in obj.__dict__.items():
        result[key] = value
        
    return result
