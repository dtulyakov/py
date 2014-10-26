#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys
try:
	def cena(rub, kop=0):
		return "%i руб. %i коп." % (rub, kop)

	print cena(8, 50)
	print cena(7)
	print cena(rub=23, kop=70)
except:
	print "При выполнении программы возникла проблема!"
