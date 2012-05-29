# -*- coding: cp936 -*-
import pymssql
from xml.dom.minidom import Document
conn = pymssql.connect(host='222.44.124.120', user='sa', password='kpsoft',database='autocap_szf', as_dict=True)
cu = conn.cursor()
cu.execute("select * from programinfo where delmarker = 1")
results = cu.fetchall()

cu.execute("select name from syscolumns where id=object_id('programinfo')")
re = cu.fetchall()


doc = Document()
doc.createElement('item')
item = doc.createElement('item')
doc.appendChild(item)
for i in range(34):
    cname = doc.createElement(re[i][0])
    item.appendChild(cname)
    if results[0][re[i][0]] == None:
        results[0][re[i][0]] = 'None'
    cnametext = doc.createTextNode(str(results[0][re[i][0]]))
    cname.appendChild(cnametext)

print doc.toxml()
