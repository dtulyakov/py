#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys
try:
	D = {}
	D[1], D[2], D[3] = "ABB"
	D[0], D[1] = "AB"
	print len(D)
except:
	print "При выполнении программы возникла проблема!"
