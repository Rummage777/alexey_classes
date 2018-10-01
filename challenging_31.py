# !usr/bin/python3
# -*- coding:utf-8 -*-

import random

'''
Define a function that can accept an integer number as input and print
the "It is an even number" if the number is even, otherwise print
"It is an odd number".
'''

lenght = random.randint(5, 10)
source_data = random.sample(range(50000), lenght)


def check_even_and_odds(data):
    if data % 2 == 0:
        return True
    else:
        return False


def try_numbers(sequence):
    for item in sequence:
        result = check_even_and_odds(item)
        if result:
            print("Number {} is even".format(item))
        else:
            print("Number {} is odd".format(item))


try_numbers(source_data)
