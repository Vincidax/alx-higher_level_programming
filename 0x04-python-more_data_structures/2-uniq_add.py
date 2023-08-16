#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = set()
    for x in my_list:
        result.add(x)
    return sum(result)
