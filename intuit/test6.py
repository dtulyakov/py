#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys
try:
	res = int(open('a.txt').read()) / int(open('c.txt').read())
	print res
except IOError:
	print "Ошибка ввода-вывода"
except ZeroDivisionError:
	print "Деление на 0"
except KeyboardInterrupt:
	print "Прерывание с клавиатуры"
except:
	print "Ошибка"
