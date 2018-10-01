# !usr/bin/python3
# -*- coding:utf-8 -*-

'''
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
'''


def compare_strings(string1, string2):

    if len(string1) > len(string2):
        return string1
    elif len(string1) == len(string2):
        return string1 + '\n' + string2
    else:
        return string2


print(compare_strings('Hello', 'Dolly'))
