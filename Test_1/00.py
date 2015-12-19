#!/usr/bin/python
# coding=utf-8

#Найти сумму целых чисел от 21 до 110
#print sum(range(21,111))


#Найти сумму вещественных чисел от 10.1 до 20.1 с шагом 0.05
# summ = 0
# start = 10.1
# finish = 20.1
# step = 0.05
# while start <= finish:
#     summ += start
#     start += step
#
# print summ



#Дан список L. Вернуть предпоследний элемент списка.
# L=[1,2,3,4]
# print L[-2]


"""
Написать функцию получающую на вход 2 целых числа и возвращающую 1, если первое число больше второго,
 -1 - если второе число больше первого и 0 в случае их равества.
"""
# def returning(num_1, num_2):
#     result = 0
#     if num_1 > num_2:
#         result = 1
#     elif num_1 < num_2:
#         result = -1
#
#     return result
#
# print returning(2, 2)


#Дан словарь D. Узнать, есть ли в нем хоть одно совпадение ключа и его значения
# D = {1:2, 2:3, 3:3}
#
# for key, value in D.iteritems():
#     if key == value:
#         print "GOTTA"


#Дан список целых чисел. Написать код, который конвертирует входной список в список строк, созданных из этих чисел.
# L1 = [1,2,3]
# L2 = []
# for i in L1:
#     L2 += str(i)
#
# print L2

# Написать функцию, которая получает на вход 2 строковых параметра: input_string и suffix. Если input_string
# заканчивается на строку suffix, функция должна возвращать True, иначе - False.
# def substring(input_string, suffix):
#     result = False
#
#     if input_string.endswith(suffix):
#         result = True
#
#     return result
#
# print substring('asdf', 'dfa')

#Подсчитать количество пустых строк в файле с именем file_name.

# summ = 0
# for line in open(file_name):
#   if line.strip() == '':
#       summ += 1