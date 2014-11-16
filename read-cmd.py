#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
abc = subprocess.check_output(["whois", "dtulyakov.org.ua"])
print abc
print subprocess.check_output(["fping", "xen0.pp.ua"])
##http://программисту.рф/python/primer-chteniya-iz-terminala-na-python/
#EOF
