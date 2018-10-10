# !usr/bin/python3
# -*- coding:utf-8 -*-

'''
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
'''

given = ['21', 54, {'1': "yes"}, 'yes']

def is_yes(data):
    if data == 'yes' or data == 'Yes' or data == 'YES':
        return 'Yes'
    else:
        return 'No'

for i in given:
    print(is_yes(i))
