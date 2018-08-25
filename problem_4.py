# !usr/bin/python
# -*- coding: utf-8 -*-

"""
Write a Python function that prints out the first n rows of Pascal's triangle.
Note : Pascal's triangle is an arithmetic and geometric figure first
imagined by Blaise Pascal.
"""


def pascal_triangle(rows):
    triangle = []
    for i in range(rows):
        triangle.append([])
        triangle[i].append(1)
        if(i == 0):
            print(triangle[i - 1])
        for j in range(1, i):
            triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        if(rows != 0):
            triangle[i].append(1)
        if(i != 0):
            print(triangle[i])
    print('')
    print(triangle)


pascal_triangle(10)
