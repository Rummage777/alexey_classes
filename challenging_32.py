# !usr/bin/python3
# -*- coding:utf-8 -*-

'''
Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
'''
numbers = 3

#  TODO: переписать генератор словарей

def create_dict(n):
    new_dict = {item:item**2 for item in range(1, n+1)}
    return new_dict


print(create_dict(numbers))
