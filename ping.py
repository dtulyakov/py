#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys
import subprocessimport
import time
"""IP list tu ping"""
iplist = ['172.0.0.1', '192.168.88.1']
"""Chek time. If time from 7 to 18 then chek every minute, else every hour"""
def checkTime():
    cmdtime = int(time.strftime('%H'))
    if (cmdtime >= 7 and cmdtime <= 18):
        return time.sleep(60)
    else:
        return time.sleep(600)

def pingProcess(ip):
    pingTest = "ping -c 1 " + ip  process = subprocess.Popen(        pingTest, shell=True, stdout=subprocess.PIPE)
    process.wait()
    returnCodeTotal = process.returncode    if returnCodeTotal == 0:
        pass    else:
        return os.system('logger "Alarm "' + ip + ' is Down')

def cykle():
    for i in iplist:
        pingProcess(i)
counter = 1
while counter == 1:
    checkTime()
    cykle()
