#!/usr/bin/python
# coding=utf-8

"""
Задача на цикл while

Дано вещественное число — цена 1 кг конфет. Вывести на консоль стоимость 1.2,
1.4, . . . , 2 кг конфет.
"""


###   3   ###
x = 1.234
massa = 1
while massa < 11:
    print massa * x
    massa += 1

