# !usr/bin/python3
# -*- coding:utf-8 -*-

from __future__ import print_function

'''
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
'''

numbers = 20


def create_dict(n):
    new_dict = {}
    for item in range(1, n+1):
        new_dict[item] = item ** 2
        print(item, end=' ')
    return new_dict


create_dict(numbers)
