# usr/bin/python
# -*- coding: utf-8 -*-


'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''


def compute_value(data):
    result = int(data) + int(str(data) * 2) + int(str(data) * 3) + \
             int(str(data) * 4)
    return result


print(compute_value(9))
