import os, time

timeused = []
resolution = ['400x320', '720x576']
stream = ['100k', '350k', '500k']

for res in resolution:
    for stre in stream:
        cmdline = 'ffmpeg -i  293s.mpg   -f 3gp -acodec libopencore_amrnb -ab 12K -ac 1 -ar 8000 -vcodec mpeg4 -r 25 -b ' + stre + ' -g  75  -s ' + res + ' 293_'+ stre + res +'.3gp'
        starttime = time.time()
        os.system(cmdline)
        endtime = time.time()
        timeused.append(endtime-starttime)
print  "time used: ", timeused
input()
