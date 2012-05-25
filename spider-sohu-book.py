import urllib2
import sys
import re

def getPage(url, offset='295'):
    realurl = "%s%s%s" % (url, offset, '.html')
    print realurl
    resp = urllib2.urlopen(realurl)
    content = resp.read()

    p = re.compile('<[^>]+>')

    rematch = re.compile(r'(<h1.*</h1>)')
    h1 = rematch.findall(content)
    try:
        h1content = p.sub("", h1[0])
    except Exception,e:
        print str(e)
        return
    fp = open(r'chuangyebaodian.txt', 'a')
    print h1content
    fp.write(h1content + '\n')
    fp.flush()

    content = content.replace('\r', '')
    content = content.replace('\n', '')
    content = content.replace(' ', '')
    content = content.replace('	', '')
    cont = re.search('<divclass="txtC"id="txtBg">(.*)</p></div><divclass="boxA">', content)
    words = cont.group()
    p = re.compile('<[^>]+>')
    contTxt = p.sub("", words)

    fp.write(contTxt + '\n')
    fp.flush()
    fp.close()

def getBook(url, startOffset, endOffset):
    while startOffset < endOffset:
        getPage(url, offset=str(startOffset))
        startOffset += 1

if __name__ == '__main__':
    getBook(url = 'http://lz.book.sohu.com/chapter-22299-118041', startOffset=687, endOffset=740)
