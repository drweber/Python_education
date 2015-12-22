#!/usr/bin/python
# coding=utf-8

"""
Задача на datetime(*)

Написать скрипт, который принимает 2 аргумента командной строки: даты в формате
YYYY­mm­dd(год­месяц­дата, пример 2015­12­13). Скрипт должен преобразовывать
строки в тип datetime.date и печатать на консоль, сколько полных дней, часов, минут и
секунд укладывается в заданный временной интервал.
"""

import datetime

t1 = '2015-12-14'
t2 = '2014-12-13'

t1_formated = t1.split("-")
t2_formated = t2.split("-")

timestamp = datetime.date(int(t1_formated[0]),int(t1_formated[1]),int(t1_formated[2])) - datetime.date(int(t2_formated[0]),int(t2_formated[1]),int(t2_formated[2]))

print type(timestamp)

print "Total days %d" % round(timestamp.total_seconds()/60/60/24) #I know that this is not optimized
print "Total hours %d" % round(timestamp.total_seconds()/60/60) #I know that this is not optimized
print "Total seconds %d" % round(timestamp.total_seconds())
#atetime.date(2012, 1, 30)
