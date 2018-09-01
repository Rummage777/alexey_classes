# usr/bin/python
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


def count_cases(data):
    result = {"upper_case": 0, "lower_case": 0}
    for item in data:
        if item.islower():
            result["lower_case"] += 1
        elif item.isupper():
            result["upper_case"] += 1
    print("UPPER CASE", result["upper_case"])
    print("LOWER CASE", result["lower_case"])
    return result


count_cases("Hello world!")
