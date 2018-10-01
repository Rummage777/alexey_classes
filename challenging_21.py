# !usr/bin/python3
# -*- coding: utf-8 -*-

from math import sqrt
import operator


'''
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5 DOWN 3 LEFT 3 RIGHT 2
The numbers after the direction are steps. Please write a program
to compute the distance from current position after a sequence
of movement and original point. If the distance is a float,
then just print the nearest integer.
Example:
If the following tuples are given as input to the program
then, the output of the program should be: 2
'''

commands = {'UP': 5, 'DOWN': 3, 'LEFT': 3, 'RIGHT': 2}
sorted_commands = sorted(commands.items(), key=operator.itemgetter(0))
print(sorted_commands)

# TODO: переделать на метод item так  сразу получаю пару в цикле. Использовать сортированный словарь или список значений)


def calculate_distance(data):
    distance = 0
    location = [0, 0]
    for item in data:
        if item == 'UP':
            location[1] += int(data[item])
        if item == 'DOWN':
            location[1] -= int(data[item])
        if item == 'RIGHT':
            location[0] += int(data[item])
        if item == 'LEFT':
            location[0] -= int(data[item])
    distance = int(round(sqrt(location[0]**2 + location[1]**2)))
    return distance


print(calculate_distance(commands))
