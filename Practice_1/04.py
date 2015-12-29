#!/usr/bin/python
# coding=utf-8

"""
Задача на break

Дан список целых чисел. Вывести на консоль числа, количество цифр в которых меньше
3. Если в списке встретится число 42, прервать работу программы и вывести на консоль
строку “The Answer to the Ultimate Question of Life, the Universe, and Everything".
"""


###   4   ###
import random
list_of_number = random.sample(range(1, 200), 10)

print list_of_number

for i in list_of_number:
    if len(str(i)) > 2:
        continue
    elif i == 42:
        print "The Answer to the Ultimate Question of Life, the Universe, and Everything"
        break
    else:
        print i