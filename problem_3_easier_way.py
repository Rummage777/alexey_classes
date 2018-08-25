# !usr/bin/python
# -*- coding: utf-8 -*-

"""
Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the
alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""

chars = 'abcdefghijklmnopqrstuvwxyz'

alphabet = set(chars)


def pangram(sentense):
    print(sentense)
    sentense = set(sentense)
    if len(alphabet&sentense) == 26:
        return print('This is Pangram')

    else:
        return print('This is not Pangram')


pangram('The quick brown fox jumps over the lazy dog')


pangram(input("Print your own sentence "))
