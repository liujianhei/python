#!/usr/bin/env python
#encoding=utf-8
#Author Jianhei Liu

import os
hostnet = "10.10.100."
hostsip = range(19, 29) + range(36, 56) + range(56,61)
live = []
for sip in hostsip:
    response = os.system("ping -c 1 " + hostnet + str(sip))
#and then check the response...
    if response == 0:
        live.append(sip)
print live