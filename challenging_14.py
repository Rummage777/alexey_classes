# !usr/bin/python
# -*- coding: utf-8 -*-

'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
# DONE: переделать в универсальную функцию с передачей метода


def count_cases(data, str_method):
    counter = 0
    for item in data:
        if str_method(item):
            counter += 1
    return counter


print("UPPER CASE", count_cases("Hello world!", str.isupper))
print("LOWER CASE", count_cases("Hello world!", str.islower))
