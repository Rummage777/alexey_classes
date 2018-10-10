# !usr/bin/python3
# -*- coding:utf-8 -*-

'''
Question:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
'''

given = (1,2,3,4,5,6,7,8,9,10)

def is_even(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


print(*is_even(given))
