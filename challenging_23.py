# !usr/bin/python3
# -*- coding:utf-8 -*-


'''
Question:
Write a method which can calculate square value of number
'''


def data_square(data):
    return data ** 2


print(data_square(7))


def func_test():
    result = data_square(3)
    if result != 9:
        print('Test #1 failed!')
    result = data_square(0)
    if result != 0:
        print('Test #2 failed!')


func_test()
