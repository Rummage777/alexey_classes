# !usr/bin/python3
# -*- coding:utf-8 -*-


'''
Define a function that can receive two intenger numbers in string form
and compute their sum and then print it in console.
'''


def compute_integers(number1, number2):
    return int(number1) + int(number2)


print(compute_integers('56', '44'))


def test_compute():
    result = compute_integers('5', '10')
    if result != 15:
        print("Test #1 failed")


test_compute()
