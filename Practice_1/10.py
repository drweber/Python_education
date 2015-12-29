#!/usr/bin/python
# coding=utf-8

"""
Задача на разбор строки

Написать функцию, принимающей строку со словами, разделенными пробелами и
возвращающей список из строк, в каждой строке должно быть одно слово.
"""

def no_space(input_sentence):
    return input_sentence.split()

print no_space('Bla bla bla')