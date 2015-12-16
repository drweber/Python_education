#!/usr/bin/python
# coding=utf-8

"""
Задача на if­else

Даны три числа. Найти сумму двух наибольших из них. Результат вывести на консоль
функцией print.
"""

###   1   ###
a = 2
b = 3
c = 6
x = a + b
y = c + b
z = a + c

if  x > y and x > z:
   print x
elif y > x and y > z:
   print y
else:
   print z
