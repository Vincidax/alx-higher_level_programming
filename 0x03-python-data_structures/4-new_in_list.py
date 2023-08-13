#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """A function that replaces an element of a list at a specific position
    without modifying the original list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[:idx] + [element] + my_list[idx+1:]
    return new_list
