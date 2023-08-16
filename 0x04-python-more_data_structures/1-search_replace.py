#!/usr/bin/python3

def search_replace(my_list, search, replace):
    result = []
    for x in range(len(my_list)):
        if my_list[x] != search:
            result.append(my_list[x])
        elif my_list[x] == search:
            result.append(replace)
    return result
