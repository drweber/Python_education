#!/usr/bin/python
# coding=utf-8

"""
Задача на continue

Дан список целых чисел. Вывести на консоль числа, которые делятся нацело на 13.
"""

###   5   ###
import random
list_of_number = random.sample(range(1, 200), 10)

print list_of_number
for i in list_of_number:
    if (i % 13) != 0:
        continue
    else:
        print i