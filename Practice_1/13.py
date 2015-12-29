#!/usr/bin/python
# coding=utf-8

"""
Задача про tuple

Дан кортеж(tuple) с целыми числами. Написать функцию, которая удаляет из кортежа все
нечетные числа и возвращает результат в виде кортежа.
"""

def print_even(many_numbers):
    result_evens = []
    for i in many_numbers:
        if (i % 2) == 0 and i != 0:
            result_evens += str(i)

    return tuple(result_evens)

print print_even((1,2,3,4,5,6))