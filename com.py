# -*- coding: utf-8 -*-
import time
f = open('/tmp/test.txt')
time.sleep(3)
line = f.readline()
    while line:
    print (line),
    line = f.readline()
    f.close()

#myfile = open("/tmp/test.txt", "rU") #чтение из файла
#for line in myfile.xreadlines(): #построчно читаем файл и выводим на экран
#    print line
