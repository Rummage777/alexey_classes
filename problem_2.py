# !usr/bin/python
# -*- coding: utf-8 -*-

"""
Write module that create a new list with unique elements of the existed list.
Print both lists into console.
Sample List : [1, 2, 3, 3, 3, 3, 4, 5, 5, 5]
Unique List : [1, 2, 3, 4, 5]
"""


sample_list = [1, 2, 3, 3, 3, 3, 4, 5, 5, 5]
unique_list = list(set(sample_list))
print ('Sample List : {}'.format(sample_list))
print ('Unique List : {}'.format(unique_list))
