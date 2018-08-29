# !usr/bin/python
# -*- coding: utf-8 -*-

'''
Question:
Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''

# Using input from string not console
input_data = '34,67,55,33,12,98'


def list_converter(data):
    data_list = data.split(',')
    return data_list


def tuple_converter(data):
    data_tuple = tuple(list_converter(data))
    return data_tuple


print(list_converter(input_data))
print(tuple_converter(input_data))


def test_result():
    passed = True
    result = list_converter(input_data)
    if len(result) != 6:
        passed = False
        print('Test #1 failed')
    if result != ['34', '67', '55', '33', '12', '98']:
        passed = False
        print('Test #2 failed')
    number = tuple_converter(input_data)
    if len(number) != 6:
        passed = False
        print('Test #3 failed')
    if number != ('34', '67', '55', '33', '12', '98'):
        passed = False
        print('Test #4 failed')
    if passed:
        print('Tests are passed')


test_result()

