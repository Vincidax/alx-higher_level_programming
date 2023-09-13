#!/usr/bin/python3
'''a function that creates an Object from a “JSON file”'''


def load_from_json_file(filename):
    '''Write a function that creates an Object from a “JSON file”
    Args:
        filename: a json file used to create an object
    '''

    import json
    with open(filename) as json_file:
        return json.loads(json_file.read())
