#!/usr/bin/python
# coding=utf-8

"""
Задача на функцию с переменным числом аргументов

Написать функцию, которая принимает на вход произвольное количество целых
чисел(используем *args).  Функция должна считать сумму цифр переданных чисел и
возвращать в качестве результата эту сумму.
"""

def vars(*args):
    return sum(args)

print vars(1,2,3)