#!/usr/bin/python3
'''function for serialization of an object'''


import json


def class_to_json(obj):
    '''obj is an instance of a Class
    Prototype: def class_to_json(obj)'''

    result = obj.__dict__
    return result

