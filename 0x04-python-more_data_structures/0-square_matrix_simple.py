#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared_row = [x * x for x in row]
        result.append(squared_row)
    return result
