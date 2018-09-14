# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

# TODO: принимать в качестве второго аргумета название колонки, проверить и сортировать по нужной

input_data = [('Tom',19,80),('John',20,90),('Jony',17,91),('Jony',17,93),('Json',21,85)]


class Person(object):
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores


def sorted_by_name(Person):
    return person.name


def sorted_by_age(Person):
    return person.age


def sorted_by_scores(Person):
    return person.scores


a = sorted(input_data, key=sorted_by_name) #, sorted_by_age, sorted_by_scores)
print(a)
