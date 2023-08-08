#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new = abs(number)
mod = new % 10
if (number < 0):
    print(f'Last digit of {number} is -{mod} and is less than 6 and not 0')
else:
    if (new % 10) > 5:
        print(f'Last digit of {number} is {mod} and is greater than 5')
    elif (new % 10) == 0:
        print(f'Last digit of {number} is {mod} and is 0')
    else:
        print(f'Last digit of {number} is {mod} and is less than 6 and not 0')
