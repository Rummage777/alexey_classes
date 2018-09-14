# !usr/bin/python
# -*- coding: utf-8 -*-

"""
Write a Python function that prints out the first n rows of Pascal's triangle.
Note : Pascal's triangle is an arithmetic and geometric figure first
imagined by Blaise Pascal.
"""


def current_row(row):
    new_row = []
    for i in range(row):
        if i == 0 or i == row - 1:
            new_row.append(1)
        else:
            prev_row = current_row(row - 1)
            new_row.append(prev_row[i - 1] + prev_row[i])
    return new_row


def triangle(n):
    result = []
    for item in range(n):
        result.append(current_row(item + 1))
        print(result[item])
    return result


triangle(5)
