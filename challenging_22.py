# !usr/bin/python3
# -*- coding: utf-8 -*-

from collections import defaultdict

'''
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1
'''

input_data = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'


# Defalt Dict в Colections.

def calculate_words(input_data):
    result = defaultdict(int)
    for item in input_data.split(' '):
        result[item] += 1
    return result


result = calculate_words(input_data)
print(type(result))
for item in sorted(result.keys()):
    print('{}:{}'.format(item, result[item]))
