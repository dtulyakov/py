#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import commands, os, string
#program = raw_input("Введите имя программы для проверки: ")
program = 'cron'
try:
    #выполняем команду 'ps' и присваиваем результат списку
#    output = commands.getoutput("ps -f|grep " + program)
    output = commands.getoutput("ps -f|grep zsh")
    proginfo = string.split(output)
    #выводим результат
#    print "\n\
#    Путь:\t\t", proginfo[5], "\n\
#    Владелец:\t\t\t", proginfo[0], "\n\
#    ID процесса:\t\t", proginfo[1], "\n\
#    ID родительского процесса:\t", proginfo[2], "\n\
#    Время запуска:\t\t", proginfo[4], "\n\
    print "\n\
    ALL:0\t\t", proginfo[0], "\n\
    ALL:1\t\t", proginfo[1], "\n\
    ALL:2\t\t", proginfo[2], "\n\
    ALL:3\t\t", proginfo[3], "\n\
    ALL:4\t\t", proginfo[4], "\n\
    ALL:5\t\t", proginfo[5], "\n\
    ALL:6\t\t", proginfo[6], "\n\
    ALL:7\t\t", proginfo[7], "\n\
    ALL:8\t\t", proginfo[8], "\n\
    ALL:9\t\t", proginfo[9], "\n\
    ALL:10\t\t", proginfo[10], "\n\
    ALL:11\t\t", proginfo[11],
except:
    print "При выполнении программы возникла проблема!"
