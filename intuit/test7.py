#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys
print 3 < 4 < 6, "3 < 4 < 6"
print 3 >= 5, "3 >= 5"
print 4 == 4, "4 == 4"
print 4 != 4, "4 != 4"
for i, j in (0, 0), (0, 1), (1, 0), (1, 1):
	print i, j, ":", i & j, i | j, i ^ j
pi = 3.1415926535897931
print pi ** 40
