# usr/bin/python
# -*- coding: utf-8 -*-


'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''


def analyzing_numbers():
    result = []
    for number in range(2222, 3001):
        passed = True
        (first, second, third, fourth) = [int(item) for item in str(number)]
        if first % 2 != 0:
            passed = False
        if second % 2 != 0:
            passed = False
        if third % 2 != 0:
            passed = False
        if fourth % 2 != 0:
            passed = False
        if passed:
            result.append(number)

    return result


print(*analyzing_numbers(), sep=', ')
