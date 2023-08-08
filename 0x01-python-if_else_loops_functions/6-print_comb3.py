#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if x != y and y > x:
            if x == 8 and y == 9:
                print("89")
            else:
                print("{}{}".format(x, y), end=", ")
