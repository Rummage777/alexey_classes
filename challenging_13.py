# usr/bin/python
# -*- coding: utf-8 -*-

'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''


def calculation_letters(input_data):
    letters = 0
    for item in input_data:
        if item.isalpha():
            letters += 1
    return letters


def calculation_digits(input_data):
    digits = 0
    for item in input_data:
        if item.isdigit():
            digits += 1
    return digits


print("LETTERS", calculation_letters('hello world! 123'))
print("DIGITS", calculation_digits('hello world! 123'))
