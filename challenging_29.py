# !usr/bin/python3
# -*- coding:utf-8 -*-


'''
Define a function that can accept two strings as input
and concatenate them and then print it in console.
'''


def compute_strings(*args, sep=" "):
    return sep.join(args)


print(compute_strings('Define', 'a', 'function', 'that', 'can', 'accept', 'strings', 'and', 'concatenate', 'them', '.'))
