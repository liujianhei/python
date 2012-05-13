#!/usr/bin/env python
"""
Store an arbitrary file by FTP in binary mode. Uses anonymous
ftp unless you pass in a user=(name, pswd) tuple of arguments.
"""

import ftplib    # socket-based FTP tools

def putfile(file, site, dir, user=(), *, verbose=True):
    """
    store a file by ftp to a site/directory
    anonymous or real login, binary transfer
    """
    if verbose: print('Uploading', file)
    local = open(file, 'rb')
    remote = ftplib.FTP(site)
    remote.login(*user)
    remote.cwd(dir)
    remote.storbinary('STOR ' + file, local, 1024)
    remote.quit()
    local.close()
    if verbose: print('Upload done.')

if __name__ == '__main__':
    site = '222.44.124.120'
    dir  = '.'
    import sys, getpass
    pswd = getpass.getpass(site + ' pswd?')
    putfile(sys.argv[1], site, dir, user=('btvav', pswd))
