#!/usr/bin/python3
'''a function that writes an Object to a text file,
using a JSON representation'''

import sys
import json


def save_to_json_file(my_obj, filename):
    '''a function that writes an Object to a text file, using a JSON
    use the with statement'''

    import json
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)


def load_from_json_file(filename):
    '''Write a function that creates an Object from a “JSON file”
    Args:
        filename: a json file used to create an object
    '''

    import json
    with open(filename) as json_file:
        return json.loads(json_file.read())


'''Access command line arguments'''
script_name = sys.argv[0]
arguments = sys.argv[1:]
add_list = list(arguments)
'''load, add , save'''
filename = "add_item.json"
save_to_json_file(add_list, filename)
load_from_json_file(filename)
