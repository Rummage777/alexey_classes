# !usr/bin/python3
# -*- coding: utf-8 -*-


'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''


class GenerateNumbers(object):

    def __init__(self):
        pass

    def iter_numbers(n):
        result = []
        for item in range(n):
            if item % 7 == 0 and item != 0:
                result.append(str(item))
        print(', '.join(result))
        return result


a = GenerateNumbers.iter_numbers(250)
