# !usr/bin/python# -*- coding: utf-8 -*-from __future__ import print_function'''Question:Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.'''result = []start = 2000end = 3200print('-' * 15 + ' ' * 3 + 'First method' + ' ' * 3 + '-' * 15)for number in range(start, end + 1):    if number % 7 == 0 and number % 5 != 0:        print(number, end=', ')print()print()print('-' * 15 + ' ' * 3 + 'Second method' + ' ' * 3 + '-' * 15)for number in range(start, end + 1):    if number % 7 == 0 and number % 5 != 0:        result.append(number)print(*result, sep=', ')print()def test_result():    passed = True    count_results = len(result)    if count_results != 138:        passed = False        print('Test #1 failed')    maximum = max(result)    if maximum != 3199:        passed = False        print('Test #2 failed')    minimum = min(result)    if minimum != 2002:        passed = False        print('Test #3 failed')    if passed:        print('Tests are passed')test_result()