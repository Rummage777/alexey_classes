# !usr/bin/python3
# -*- coding:utf-8 -*-


'''
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
'''

numbers = 20


def create_list(n):
    new_list = [x**2 for x in range(1, n+1)]
    return new_list


result = create_list(numbers)
print(result[5:])