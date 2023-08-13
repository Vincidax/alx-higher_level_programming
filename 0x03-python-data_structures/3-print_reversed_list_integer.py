#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    'a function that prints all integers of a list, in reverse order.'
    if isinstance(my_list, list):
        my_list = my_list[::-1]
        for x in my_list:
            print("{:d}".format(x))
