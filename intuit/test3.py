#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys
try:
	file = open("file.txt", "r")
	while file:
		line = file.readline()
		if not line:
			break
		if len(line) > 5:
			print line
	file.close()
except:
	print "При выполнении программы возникла проблема!"
