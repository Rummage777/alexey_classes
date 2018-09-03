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


def calculate_items(input_data, str_method):
    counter = 0
    for item in input_data:
        if str_method(item):
            counter += 1
    return counter


print("LETTERS", calculate_items('hello world! 123', str.isalpha))
print("DIGITS", calculate_items('hello world! 123', str.isdigit))
