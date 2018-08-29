# !usr/bin/python# -*- coding: utf-8 -*-from math import pifrom math import efrom math import sqrt"""Question:Write a program which can compute the factorial of a given numbers.\The results should be printed in a comma-separated sequence on a single line.\Suppose the following input is supplied to the program: 8 \Then, the output should be:40320"""def factorial(given_number):    '''calculating factorial using loop'''    result = 1    for number in range(1, given_number + 1):        result = result * number    return resultdef factorial2(given_number):    '''calculating factorial using James Stirling formula with habr modifier'''    habr_modifier = 1.0 + 1.0/(11.943*given_number)    result = int(sqrt(2.0*pi*given_number) * ((given_number/e)**                 given_number) * habr_modifier)    return resultprint('Loop calculation method = ', factorial(8))print('Stirling formula method = ', factorial2(8))