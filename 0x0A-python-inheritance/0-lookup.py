#!/usr/bin/python3

def lookup(obj):
    """
    This function returns the list of available attributes and
    methods of an object
    """
    list = dir(obj)
    return list