#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import ConfigParser
import os
import time
import getpass

def get_dump():
    print "Enter user:"
    user = "root"

    print "Password will not be visible:"
    password = "root"

    print "Enter host:"
    host = "10.0.3.200"

    print "Enter database name:"
    #database = raw_input()
    database = "mysql"


    filestamp = time.strftime('%Y-%m-%d-%I:%M')
    os.popen("mysqldump -h%s -u%s -p%s -e --opt -c %s | gzip -c > %s.gz" % (host,user,password,database,database+"_"+filestamp))

    print "\n-- блеать "+database+"_"+filestamp+".gz --"

if __name__=="__main__":
    get_dump()
