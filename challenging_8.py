# !usr/bin/python
# -*- coding: utf-8 -*-

'''
Question:
Write a program that accepts a comma separated sequence of \
words as input and prints the words in a comma-separated \
sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''


def alphabetical_sorting(sequence):
    result = sequence.split(',')
    result.sort()
    print(','.join(result))


alphabetical_sorting('without,hello,bag,world')
