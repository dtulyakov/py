#!/usr/bin/python
# -*- coding: utf-8 -*-
myfile = open("/tmp/test.txt", "rU") #чтение из файла
for line in myfile.xreadlines(): #построчно читаем файл и выводим на экран
    print line
##http://программисту.рф/python/postrochnoe-chtenie-iz-faila-python/
#EOF
