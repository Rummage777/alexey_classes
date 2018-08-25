# !usr/bin/python
# -*- coding: utf-8 -*-

"""
Write a Python program to find the list in a list
of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
"""


def highest(sample_lists):
    maxsimum_sum = (max(sample_lists, key=sum))
    return maxsimum_sum


highest([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]])


def test_highest():
    passed = True
    result = highest([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]])
    if result != [10, 11, 12]:
        passed = False
        print('Test #1 failed')

    result = highest([[1, 2, 3], [4, 5, 6], [2, 111, 12], [7, 8, 9]])
    if result != [2, 111, 12]:
        passed = False
        print('Test #2 failed')

    result = highest([[13, 13], [4, 5, 6], [1, 2, 3], [7, 8, 9]])
    if result != [13, 13]:
        passed = False
        print('Test #3 failed')
    if passed:
        print('Test is passed')


test_highest()
