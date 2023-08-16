#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    all_keys = list(a_dictionary.keys())
    for x in all_keys:
        if key == x:
            del a_dictionary[key]
    return a_dictionary
