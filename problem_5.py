# !usr/bin/python
# -*- coding: utf-8 -*-

"""
Write a Python program to compute the similarity between two lists.
Sample data: ["red", "orange", "green", "blue", "white"],
["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
"""

Color1 = ["red", "orange", "green", "blue", "white"]
Color2 = ["black", "yellow", "green", "blue"]

print('Color1-Color2: {}'.format(sorted(list(set(Color1) - set(Color2)))))
print('Color2-Color1: {}'.format(sorted(list(set(Color2) - set(Color1)))))
