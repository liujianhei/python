# -*- coding: cp936 -*-
import pymssql
import os
from xml.dom.minidom import Document
conn = pymssql.connect(host='222.44.124.120', user='sa', password='kpsoft',database='autocap_szf', as_dict=True)
cu = conn.cursor()
cu.execute("select * from programinfo where delmarker = 1")
results = cu.fetchall()

cu.execute("select name from syscolumns where id=object_id('programinfo')")
colname = cu.fetchall()
fplog = open('C:\\xml\log.txt', 'a')
for res in results:
    fp1 = open('D:\\' + res['filename'], 'w')
    fp1.write('aaa')
    fp1.close()
    if os.path.isfile('D:\\' + res['filename']):
        fplog.write('find file ' + 'D:\\' + res['filename'] + '\n')
        cmdline = 'copy ' + 'D:\\' + res['filename'] + ' ' + 'C:\\xml\\' + res['filename'] + ' /-Y'
        print cmdline
        os.system(cmdline)
        fplog.write(cmdline +'\n' + 'move file ' + 'D:\\' + res['filename'] + ' successfull!\n')

        doc = Document()
        doc.createElement('programinfo')
        programinfo = doc.createElement('programinfo')
        doc.appendChild(programinfo)
        for i in range(len(colname)):
            cname = doc.createElement(colname[i][0])
            programinfo.appendChild(cname)
            if res[colname[i][0]] == None:
                res[colname[i][0]] = 'None'
            cnametext = doc.createTextNode(str(res[colname[i][0]]))
            cname.appendChild(cnametext)

    #print doc.toxml()
        fp = open('C:\\xml\\' + res['filename'].split('.')[0] + '.xml', 'w')
        print 'create ' + 'C:\\xml\\' + res['filename'].split('.')[0] + '.xml'
        fp.write(doc.toxml())
        fp.close()
        fplog.write('create ' + 'C:\\xml\\' + res['filename'].split('.')[0] + '.xml\n')

    elif os.path.isfile('C:\\xml\\' + res['filename']):
        fplog.write('find file ' + 'C:\\xml\\' + res['filename'])
        doc = Document()
        doc.createElement('programinfo')
        programinfo = doc.createElement('programinfo')
        doc.appendChild(programinfo)
        for i in range(len(colname)):
            cname = doc.createElement(colname[i][0])
            programinfo.appendChild(cname)
            if res[colname[i][0]] == None:
                res[colname[i][0]] = 'None'
            cnametext = doc.createTextNode(str(res[colname[i][0]]))
            cname.appendChild(cnametext)
    #print doc.toxml()
        print 'C:\\xml\\' + res['filename'].split('.')[0] + '.xml'
        fp = open('C:\\xml\\' + res['filename'].split('.')[0] + '.xml', 'w')
        print 'create ' + 'C:\\xml\\' + res['filename'].split('.')[0] + '.xml'
        fp.write(doc.toxml())
        fp.close()
        fplog.write('create ' + 'C:\\xml\\' + res['filename'].split('.')[0] + '.xml\n')
    else:	
        print 'cannot find file ' + res['filename']
        fplog.write('cannot find file ' + res['filename'] + '\n')
fplog.close()
