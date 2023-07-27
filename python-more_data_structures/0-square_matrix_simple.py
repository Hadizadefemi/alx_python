#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        each_list = []
        for i in row:
            each_list.append(i**2)

        new_matrix.append(each_list)

    return new_matrix
