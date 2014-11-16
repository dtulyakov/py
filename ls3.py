#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile
from os.path import join as joinpath

mypath = "."
for i in listdir(mypath):
    if isfile(joinpath(mypath,i)):
        print i
#
##http://программисту.рф/python/python-spisok-faylov-v-papke/
#EOF
