import os, sys
import urlparse, urllib
from string import replace, find, lower
from htmllib import HTMLParser
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO

class Retriever():
    def __init__(self, url):
        self.url = url
        self.file = self.filename()

    def filename(self, deffile='index.html'):
        urltuple = urlparse.urlparse(self.url)
	path = urltuple[1] + urltuple[2]
	ext = os.path.splitext(path)
	if ext == '':
	    if path[-1] == '/':
	        path += '/' +deffile
	else:
            path += deffile
	ldir = os.path.dirname(path)
        if not os.path.isdir(ldir):
            if os.path.exists(ldir): unlink(ldir)
            os.makedirs(ldir)
        return path

    def download(self):
        try:
            retval = urllib.urlretrieve(self.url, self.file)
            print retval[0]
        except IOError:
            retval = ('*** ERROR: invalid URL "%s"' % self.url,)
            print retval
        return retval

    def parseAndGetLinks(self):
        self.parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO)))
        print self.file
        fp = open(self.file, 'r')
        self.parser.feed(fp.read())
        fp.close()
        self.parser.close()
        return self.parser.anchorlist

class Crawler():

    def __init__(self, url):
        self.q = [url]
        self.seen = []
        self.dom = urlparse.urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()
        print retval
        if retval[0] == '*':
            print retval, '...skiping parse'
            return
        print 'URL:', url
        print 'FILE:', r.file
        self.seen.append(url)

        links = r.parseAndGetLinks()
        for eachLink in links:
            if eachLink[:4] != 'http' and find(eachLink, '://') == -1:
                eachLink = urlparse.urljoin(url, eachLink)
            print '* ', eachLink,

            if find(lower(eachLink, 'mailto:')) != -1:
                print '... discarded, mailto link'
                continue
            if eachLink not in self.seen:
                if find(eachLink, self.dom) == -1:
                    print '... discarded, not in domain'
                else:
                    if eachLink not in self.q:
                         self.q.append(eachLink)
                         print '... new, added to Q'
                    else:
                        print '... discarded, already in Q'
            else:
                print '...discarded, already processed'

    def go(self):
        while self.q:
            url = self.q.pop()
            self.getPage(url)

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        try:
            url = raw_input('Enter starting URL:')
        except (KeyboardInterrupt, EOFError):
            url = ''
    if not url: return
    robot = Crawler(url)
    robot.go()

if __name__ == '__main__':
    main()
