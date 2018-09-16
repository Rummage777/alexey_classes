# !usr/bin/python3
# -*- coding:utf-8 -*-


'''
Define a function which can compute the sum of two numbers.
'''


def compute_sum(number1, number2):
    ''' Takes 2 arguments and return a sum of them'''
    return number1 + number2


print(compute_sum(7, 14.5))


def test_sum():
    result = compute_sum(1, 2)
    if result != 3:
        print('Test #1 failed')


test_sum()
