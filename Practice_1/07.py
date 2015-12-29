#!/usr/bin/python
# coding=utf-8

# Задача на простую функцию

# Написать функцию, которая принимает 2 параметра: вес конфет в кг(вещественное
# число) и стоимость 1 кг конфет в BYR(целое число).  Функция должна возвращать
# суммарную стоимость конфет, округленную до целого числа. Для округления использем
# функцию round.

###  7  ###

sweets_cost = 2
sweets_weight = 2.234

def summary(cost, weight):
    return int(round(cost * weight))

print(summary(sweets_cost, sweets_weight))