# usr/bin/python3
# -*- coding: utf-8 -*-

# from __future__ import print_function

'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''


def analyzing_numbers():
    result = []
    for number in range(2222, 3001):
        (first, second, third, fourth) = [int(item) for item in str(number)]
        if first % 2 == 0 and second % 2 == 0 and third % 2 == 0 and fourth % 2 == 0:
            result.append(number)
    return result


print(*analyzing_numbers(), sep=', ')
