# !usr/bin/python3
# -*- coding: utf-8 -*-

import random

'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''

# TODO: переделать цикл с генератором


n = random.randint(250, 500)
result = []


class GenerateNumbers(object):

    def __init__(self):
        pass

    def check_numbers(number):
        if number % 7 == 0:
                return True
        else:
            return False

    def iter_numbers(max):
        number = 0
        while number < max:
            number += 1
            if GenerateNumbers.check_numbers(number):
                yield number


divisible_by_7 = GenerateNumbers.iter_numbers(n)

for item in divisible_by_7:
    result.append(item)
print(result)
