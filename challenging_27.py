# !usr/bin/python3
# -*- coding:utf-8 -*-


'''
Define a function that can convert a integer into a string and print it in console.
'''


def convert_int_to_str(data):
    '''Takes integer as argument, returns a string'''
    return str(data)


var = convert_int_to_str(7865653)
print('Type or variable = {}, value = {}.'.format(type(var), var))


def test_convert():
    result = convert_int_to_str(564)
    if type(result) != str:
        print('Test #1 failed')


test_convert()
