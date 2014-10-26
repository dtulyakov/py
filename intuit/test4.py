#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys
try:
	min = 1
	max = 15
	for i in range(min, max):
		for j in range(min, max):
			print "%3i" % (i*j),
		print
except:
	print "При выполнении программы возникла проблема!"
