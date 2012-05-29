# -*- coding: cp936 -*-
import pymssql
import os
from xml.dom.minidom import Document
conn = pymssql.connect(host='192.168.100.197', user='sa', password='kpsoft',database='autocap_szf', as_dict=True)
cu = conn.cursor()
cu.execute("select * from programinfo where delmarker = 1")
results = cu.fetchall()

cu.execute("select name from syscolumns where id=object_id('programinfo')")
colname = cu.fetchall()
for res in results:
    if os.path.isfile('D:\\' + res['filename']):
        cmdline = 'move ' + 'D:\\' + res['filename'] + ' ' + 'C:\\xml\\' + res['filename']
        print cmdline
        os.system(cmdline)

        doc = Document()
        doc.createElement('item')
        item = doc.createElement('item')
        doc.appendChild(item)
        for i in range(len(colname)):
            cname = doc.createElement(colname[i][0])
            item.appendChild(cname)
            if res[colname[i][0]] == None:
                res[colname[i][0]] = 'None'
            cnametext = doc.createTextNode(str(res[colname[i][0]]))
            cname.appendChild(cnametext)

    #print doc.toxml()
        print 'C:\\xml\\' + res['filename'][:-3] + 'xml'
        fp = open('C:\\xml\\' + res['filename'][:-3] + 'xml', 'w')
        print 'create ' + 'C:\\xml\\' + res['filename'][:-3] + 'xml'
        fp.write(doc.toxml())
        fp.close()
    else:
        print 'cannot find file ' + 'D:\\' + res['filename']

