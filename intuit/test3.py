#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys
try:
	f = open("file.txt", "r")
	while f:
		l = f.readline()
		if not l:
			break
		if len(l) > 5:
			print l
	f.close()	
except:
	print "При выполнении программы возникла проблема!"
