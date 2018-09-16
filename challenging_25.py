# !usr/bin/python3
# -*- coding:utf-8 -*-


'''
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define a instance parameter, need add it in __init__ method
You can init a object with construct parameter or set the value later
'''


class MyClass(object):

    data = 'My Class parameter'

    def __init__(self):
        self.data = 'An instance of MyClass parameter'


class_obj1 = MyClass()
print(MyClass.data, class_obj1.data)

class_obj2 = MyClass()
class_obj2.data = "Changed an instance parameter"
print(MyClass.data, class_obj2.data)
