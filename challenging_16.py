# usr/bin/python
# -*- coding: utf-8 -*-

'''
Question:
Use a list comprehension to exclude each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''


def exclude_adds(data):
    result = []
    sequence = data.split(',')
    for number in sequence:
        if int(number) % 2 != 0:
            result.append(number)
    return result


print(*exclude_adds('1,2,3,4,5,6,7,8,9'), sep=',')
