# !usr/bin/python3
# -*- coding: utf-8 -*-

import random

'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''

# TODO: переделать цикл с генератором. Переделать еще раз


n = random.randint(250, 500)
result = []


class GenerateNumbers:

    def __init__(self, n):
        self.n = n

    def iter_numbers(self, n):
        for item in range(1, n+1):
            if item % 7 == 0:
                yield item

    def __iter__(self):
        return self.iter_numbers(self.n)


for item in GenerateNumbers(n):
    print(item, end=" ")
