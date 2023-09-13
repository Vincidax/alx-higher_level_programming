#!/usr/bin/python3
''' a class with a method that retrieves data with attrs'''


class Student:
    '''class with a method that retrieves data with attrs'''
    def __init__(self, first_name, last_name, age):
        '''Initializes inputs'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''A function that retrieves a dictionary representation'''
        result = {}

        if attrs is None:
            '''If attrs is None, return all attributes'''
            return self.__dict__
        else:
            '''Retrieve data based on attrs'''
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
