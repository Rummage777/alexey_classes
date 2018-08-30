# !usr/bin/python
# -*- coding: utf-8 -*-

'''
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001 / 4, 3, 10, 9
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
input_data = '0100,0011,1010,1001'


def divisible_by(data):
    result = []
    sequence = data.split(',')
    for number in sequence:
        if int(number, 2) % 5 == 0:
            result.append(number)
    return result


print(','.join(divisible_by(input_data)))


def test_result():
    passed = True
    result = divisible_by(input_data)
    if result != ['1010']:
        passed = False
        print('Test #1 failed')
    if len(result) != 1:
        passed = False
        print('Test #2 failed')
    if passed:
        print('Tests are passed')


test_result()
