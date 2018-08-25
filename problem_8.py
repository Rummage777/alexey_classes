# !usr/bin/python
# -*- coding: utf-8 -*-

"""
Write a Python program that accepts a hyphen-separated sequence of words as
input and prints the words in a hyphen-separated sequence after sorting
them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow

Hint: builtin function sorted, str methods split and join
"""

sample_items = 'green-red-yellow-black-white'

print('-'.join(sorted(sample_items.split('-'))))
