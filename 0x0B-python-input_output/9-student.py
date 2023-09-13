#!/usr/bin/python3
''' a class with a method that retrieves data'''


class Student:
    '''class with a method that retrieves data'''
    def __init__(self, first_name, last_name, age):
        '''Initializes inputs'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''a function that retrieves a dictionary represantion'''
        result = {}
        for key, value in self.__dict__.items():
            result[key] = value

        return result
