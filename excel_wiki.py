#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyExcelerator import *

file="/home/lscm/Documents/web部署位置.xls"
#file="/home/lscm/Documents/ServerList.xls"

sheet = parse_xls(file)

#===============================================================================
# for j in range(1,102):
#     if sheet[0][1][(j,7)] == 'A12':
#         print sheet[0][1][(j,6)], "," ,sheet[0][1][(j,2)], "," ,sheet[0][1][(j,3)], "," ,sheet[0][1][(j,4)], "," 
#===============================================================================

#===============================================================================
# for j in range(1, 104):
#     for i in range(1, 8):
#         print "|", sheet[0][1][(j,i)],
#     print "|"
#===============================================================================
def getvalue(m, n):
#    print sheet[3][1][(m,n)]
    try:
        return sheet[0][1][(m,n)]
    except:
        return "-"
        
    
#print getvalue(0, 0)

for j in range(83, 92):
    for i in range(0, 5):
        print "|", getvalue(j, i),
    print "|"

