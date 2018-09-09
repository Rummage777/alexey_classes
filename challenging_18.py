# !usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
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


def test_result(data):
    print('Tests  started!')
    sequence = data.split(',')
    passed = True
    for password in sequence:
        if len(password) <= 6: 
            print('Password "{}" is not valid. Length password must be at least 6 letters'.format(password))
            continue
        if len(password) >= 12:
            print('Password "{}" is not valid. Maximum length of transaction password must be 12'.format(password))
            continue
        if set(password) & set('$#@') == set():
            print('Password "{}" is not valid. Password must have at least 1 character from [$#@]'.format(password))
            continue
        if set(password) & set(string.ascii_lowercase) == set():
            print('Password "{}" is not valid. Password must have at least 1 letter between [a-z]'.format(password))
            continue
        if set(password) & set(string.ascii_uppercase) == set():
            print('Password "{}" is not valid. Password must have at least 1 letter between [A-Z]'.format(password))
            continue
        if set(password) & set(string.digits) == set():
            print('Password "{}" is  not valid. Password must have at least 1 number between [0-9]'.format(password))
            continue
        if passed:
            print('Password "{}" is  valid.'.format(password))

test_result('ABd1, ABd1234@1ABd1234@1, ABd1234 1, AB 1234@1,   d1234@1, ABd    @ , ABd1234@1')