# !usr/bin/python
# -*- coding: utf-8 -*-

'''
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''


def computes_amount(log):
    sequence = []
    result = {'Amount': 0}
    for transaction in log:
        sequence.append(transaction.split(' '))
    for item in sequence:
        key, value = (item[0], int(item[1]))
        if key == 'D':
            result['Amount'] += value
        if key == 'W':
            result['Amount'] -= value
    return result['Amount']


print(computes_amount(['D 300', 'D 300', 'W 200', 'D 100']))
