# !usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import re
import string

'''
Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
# DONE: Убрать passed и использовать continue
# Переделать через set
# Добавить кейсы в тесты, когда все условия правильные, кроме одного 

# Hint: Use function any()


def check_password(data):
    result = []
    sequence = data.split(',')
    ABC = 'abcdefghijklmnopqrstuvwxyz'

    for password in sequence:
        if len(password) <= 6 or len(password) >= 12:
            continue
        if set(password) & set('$#@') == set():
            continue
        if set(password) & set(ABC) == set():
            continue
        if set(password) & set(ABC.upper()) == set():
            continue
        if set(password) & set("0123456789") == set():
            continue
        result.append(password)
    return result


print(*check_password('ABd1234@1,a F1#,2w3E*,2We3345, rtTty$'))


def test_1():
    '''Тестируем условие 1. At least 1 letter between [a-z]'''
    print('Tests set #1 started!')
    passed = True
    result = '0A@$#a'
    if set(result) & set('abc') != {'a'}:
        print('Failed Test #1')
        passed = False
    if set(result) & set(string.ascii_lowercase) != {'a'}:
        print('Failed Test #2')
        passed = False
    if set(result) & set('bcd') != set():
        print('Failed Test #3', set(result) & set('bcd'))
        passed = False
    if not re.search("[a-z]", result):
        print('Failed Test #4')
        passed = False
    if passed:
        print('Tests set #1 finished successfully')
    return passed


def test_2():
    '''Тестируем условие 2. At least 1 number between [0-9]'''
    print('Tests set #2 started!')
    passed = True
    result = '0A@$#a'
    if set(result) & set('0123456789') != {'0'}:
        print('Failed Test #1')
        passed = False
    if set(result) & set(string.digits) != {'0'}:
        print('Failed Test #2')
        passed = False
    if set(result) & set('123456789') != set():
        print('Failed Test #3')
        passed = False
    if not re.search("[0-9]", result):
        print('Failed Test #4')
        passed = False
    if passed:
        print('Tests set #2 finished successfully')
    return passed


def test_3():
    '''Тестируем условие 3. At least 1 letter between [A-Z]'''
    print('Tests set #3 started!')
    passed = True
    result = '0A@$#a'
    if set(result) & set('ABC') != {'A'}:
        print('Failed Test #1')
        passed = False
    if set(result) & set(string.ascii_uppercase) != {'A'}:
        print('Failed Test #2')
        passed = False
    if set(result) & set('BCD') != set():
        print('Failed Test #3')
        passed = False
    if not re.search("[A-Z]", result):
        print('Failed Test #4')
        passed = False
    if passed:
        print('Tests set #3 finished successfully')
    return passed


def test_4():
    '''Тестируем условие 4. At least 1 character from [$#@]'''
    print('Tests set #4 started!')
    passed = True
    result = '0A@$#a'
    if set(result) & set('$#@') != {'#', '$', '@'}:
        print('Failed Test #1')
        passed = False
    if set(result) & set('* !()') != set():
        print('Failed Test #2')
        passed = False
    if passed:
        print('Tests set #4 finished successfully')
    return passed


def test_5():
    '''Тестируем условие 5. Minimum length of transaction password: 6'''
    print('Tests set #5 started!')
    passed = True
    result = '0A@$#a'
    if len(result) < 6:
        print('Failed Test #1')
        passed = False
    if passed:
        print('Tests set #5 finished successfully')
    return passed


def test_6():
    '''Тестируем условие 6. Maximum length of transaction password: 12'''
    print('Tests set #6 started!')
    passed = True
    result = '0A@$#a0A@$#'
    if len(result) > 12:
        print('Failed Test #1')
        passed = False
    if passed:
        print('Tests set #6 finished successfully')
    return passed


def tests():
    if test_1() + test_2() + test_3() + test_4() + test_5() + test_6() == 6:
        print('All tests passed successfully')


tests()
