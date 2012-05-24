#!/usr/bin/env python
import urllib2
import re

def downURL(url, filename):
    print url
    print filename
    try:
        fp = urllib2.urlopen(url)
    except:
        print 'download exception'
        return 0
    op = open(filename, 'wb')
    while 1:
        s = fp.read()
        if not s:
            break
        op.write(s)
        fp.close()
        op.close()
        return 1
