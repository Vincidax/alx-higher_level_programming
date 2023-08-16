#!/usr/bin/python3

def common_elements(set_1, set_2):
    set_3 = set()
    for s_1 in set_1:
        for s_2 in set_2:
            if s_1 == s_2:
                set_3.add(s_1)
    return set_3
