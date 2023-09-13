#!/usr/bin/python3
'''a function that writes an Object to a text file,
using a JSON representation'''


def save_to_json_file(my_obj, filename):
    '''a function that writes an Object to a text file, using a JSON
    use the with statement'''

    import json
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)
