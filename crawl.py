import os
import urlparse, urllib
class Retriever():
    __init__(self, url):
        self.url = url
        self.file = self.filename()
    def filename(self, deffile='index.html'):
        urltuple = urlparse.urlparse(self.url)
	path = urltuple[1] + urltuple[2]
	ext = os.path.splitext(path)
	if ext = '':
	    if path[-1] == '/':
	        path += '/' +deffile
	    else:
                path += deffile
	ldir = os.path.dirname(path)


	
	        
	     
