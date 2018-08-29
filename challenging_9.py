# !usr/bin/python
# -*- coding: utf-8 -*-

'''
Question:
Write a program that accepts sequence of lines as input and \
prints the lines after making all characters in the sentence \
capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''


def string_capitalazier(data):
    print(data.upper())


string_capitalazier('Hello world')
string_capitalazier('Practice makes perfect')
