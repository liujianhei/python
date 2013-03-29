from pyExcelerator import *
#import glob

file="/home/lscm/Documents/ServerList.xls"

sheet = parse_xls(file)

fp = open('wiki.txt', 'w')
#print sheet
for j in range(84):
    for i in range(1,7):
        fp.write("|"+sheet[0][1][(j,i)])
        print "|", sheet[0][1][(j,i)],
    fp.write("|\n")
    print "|"
fp.close()

