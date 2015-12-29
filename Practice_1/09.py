#!/usr/bin/python
# coding=utf-8

"""
Задача на форматирование строки

Дан список целых чисел. Вывести на консоль строки вида “An even number: 2” для четных
числе, и “An odd number: 3” для нечетных чисел. Код оформить в виде функции,
принимающей один аргумент(список) и ничего не возвращающей.
"""
def odd_even(input_numbers):
    for i in input_numbers:
        if (i % 2) == 0 and i != 0:
            print "An even number: %d" % i
        elif (i % 2) != 0 and i != 0:
            print "An odd number: %d" % i

odd_even ([1,2,3,4])
