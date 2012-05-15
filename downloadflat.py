#!/bin/env python
"""
###########################################################################
use FTP to copy (download) all files from a single directory at a remote
site to a directory on the local machine; run me periodically to mirror
a flat FTP site directory to your ISP account; set user to 'anonymous'
to do anonymous FTP; we could use try to skip file failures, but the FTP
connection is likely closed if any files fail; we could also try to 
reconnect with a new FTP instance before each transfer: connects once now;
if failures, try setting nonpassive for active FTP, or disable firewalls;
this also depends on a working FTP server, and possibly its load policies.
############################################################################
"""

import os, sys, ftplib
from getpass import getpass
from mimetypes import guess_type

nonpassive = False
remotesite = '222.44.124.120'
remotedir  = '.'
remoteuser = 'btvav'
remotepass = getpass('Password for %s on %s: ' % (remoteuser, remotesite))
localdir   = (len(sys.argv) > 1 and sys.argv[1]) or '.'
cleanall   = input('Clean local directory first> ')[:1] in ['y', 'Y']

print('connecting...')
connection = ftplib.FTP(remotesite)
connection.login(remoteuser, remotepass)
connection.cwd(remotedir)
if nonpassive:
    connection.set_pasv(False)

if cleanall:
    for localname in os.listdir(localdir):
        try:
            print('deleting local', localname)
            os.remove(os.path.join(localdir, localname))
        except:
            print('cannot delete local', localname)

count = 0
remotefiles = connection.nlst()

for remotename in remotefiles:
    if remotename in ('.', '..'): continue
    mimetype, encoding = guess_type(remotename)
    mimetype = mimetype or '?/?'
    maintype = mimetype.split('/')[0]
    localpath = os.path.join(localdir, remotename)
    print('downloading', remotename, 'to', localpath, end=' ')
    print('as', maintype, encoding or '')

    if maintype == 'text' and encoding == None:
        # use ascii mode xfer and text file
        # use encoding compatible wth ftplib's
        localfile = open(localpath, 'w', encoding=connection.encoding)
        callback  = lambda line: localfile.write(line + '\n')
        connection.retrlines('RETR ' + remotename, callback)
    else:
        # use binary mode xfer and bytes file
        localfile = open(localpath, 'wb')
        connection.retrbinary('RETR ' + remotename, localfile.write)

    localfile.close()
    count += 1
    
connection.quit()
print('Done:', count, 'files downloaded.')
    
