#!/usr/bin/python
# coding=utf-8

"""
Задача про dict

Дан словарь с текстовым представлением цифр вида {1: "one", 2: "two", ..., 9: "nine", 0:
"zero"}. Написать функцию, которая принимает целое число и возвращает названия цифр
числа в виде строки.
Вход:
59
Выход:
"five nine"
"""

def print_numbers(full_number):
    result = ''

    for i in str(full_number):
        result = result + D[int(i)] + " "
    return result.strip()

D = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0:"zero"}

print print_numbers(123)