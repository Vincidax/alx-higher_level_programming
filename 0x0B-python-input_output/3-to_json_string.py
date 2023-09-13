#!/usr/bin/python3
''' a function that returns the JSON representation of an object '''


def to_json_string(my_obj):
    '''a function that returns the JSON representation of an object (string)
    Prototype: def to_json_string(my_obj):'''

    import json
    return json.dumps(my_obj)
