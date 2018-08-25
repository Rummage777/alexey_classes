# !usr/bin/python
# -*- coding: utf-8 -*-

"""
Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the
alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v',
         'w', 'x', 'y', 'z']

alphabet = set(chars)


def pangram(sentense):
    print(sentense)
    sentense = sentense.lower()
    for junk_symbol in '.,/!@#$%^&*()-_=:;"[]|1234567890':
        sentense = sentense.replace(junk_symbol, '')
        sentense = sentense.replace(' ', '')
    unique_letters_in_sentense = set(sentense)

    if unique_letters_in_sentense == alphabet:
        return print('This is Pangram')
    else:
        return print('This is not Pangram')


pangram('The quick brown fox jumps over the lazy dog')


pangram(input("Print your own sentence "))
