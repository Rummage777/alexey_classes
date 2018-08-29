# !usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from math import sqrt

'''
Question:
Write a program that calculates and prints the value according to the given
formula: Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given
to the program:
100,150,180
The output of the program should be:
18,22,24
'''


def calculation(input_data):
    Q = []
    C = 50
    H = 30
    D = input_data.split(',')
    for number in D:
        Q.append(int(sqrt((2 * C * int(number)) / H)))
    print(*Q, sep=',')


calculation('100,150,180')
