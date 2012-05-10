"""
Fetch an arbitrary file by FTP. Anonymous FTP unless you pass a
user=(name, pswd) tuple. Self-test FTPs a test file and site.
"""
from ftplib import FTP     # socket-based FTP tools
from os.path import exists # file existence test

def getfile(file, site, dir, user=(), *, verbose=True, refetch=False):
    """
    fetch a file by ftp from a site/directory
    anonymous or real login, binary transfer
    """
    if exists(file) and not refetch:
        if verbose: print(file, 'already fetched')
    else:
        if verbose: print('Downloading', file)
	local = open(file, 'wb')
	try:
	    remote = FTP(site)
	    remote.login(*user)
	    remote.cwd(dir)
	    remote.retrbinary('RETR ' + file, local.write, 1024)
	    remote.quit()
	finally:
	    local.close()
	if verbose: print('Download done.')
