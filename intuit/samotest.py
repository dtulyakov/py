#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys
try:
	a = 1
	b = 2
	c = a + b
	print c
	c = 33
	assert c == a + b
	print c
except:
	print "При выполнении программы возникла проблема!"
finally:
	print "Debug EOF"
