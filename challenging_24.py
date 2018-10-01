# !usr/bin/python3
# -*- coding:utf-8 -*-


'''
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
'''

def my_func():
    '''My function's docstring'''
    pass


print(help(abs))
print(help(int))
print(help(input))
print(help(my_func.__doc__))
