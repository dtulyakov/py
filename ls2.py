#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import listdir
files = listdir(".")

mypy = filter(lambda x: x.endswith('.py'), files)
print (mypy)
#
##http://программисту.рф/python/python-spisok-faylov-v-papke/
#EOF
