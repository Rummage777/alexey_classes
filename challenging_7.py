# !usr/bin/python
# -*- coding: utf-8 -*-


'''
Write a program which takes 2 digits, X,Y as input and generates
a 2-dimensional array. The element value in the i-th row
and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''
# Замечания
# переписать используя распаковку списка в переменные (list unpacking)
# использовать переменные для задания границ циклов


def making_array(data):
    array = []
    widht, height = list(map(int, data.split(',')))
    for i in range(widht):
        array.append([])
        for j in range(height):
            array[i].append(i * j)
    return(array)


print(making_array('3,5'))
