# !usr/bin/python
# -*- coding: utf-8 -*-


'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''


class StringMethods:
    """Input & Output String methods """
    def __init__(self):
        self.data = ''

    def getString(self):
        self.data = input('Enter the string: ')

    def printString(self):
        print(self.data.upper())


data_object = StringMethods()

data_object.getString()
data_object.printString()
