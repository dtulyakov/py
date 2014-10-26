#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys
for i in (False, True):
	for j in (False, True):
		print i, j, ":", i and j, i or j, not i
