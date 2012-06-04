# -*- coding: cp936 -*-
import Tkinter
import pymssql
import os
from xml.dom.minidom import Document

sourDir = 'D:'
destDir = 'C:\\xml\\'

conn = pymssql.connect(host='*', user='sa', password='*',database='*', as_dict=True)
cu = conn.cursor()
cu.execute("select * from programinfo where bak1 = 1")
results = cu.fetchall()

cu.execute("select name from syscolumns where id=object_id('programinfo')")
colname = cu.fetchall()
fplog = open(destDir + 'log.txt', 'a')

def createxml(res):
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
    fp = open(destDir + res['filename'].split('.')[0] + '.xml', 'w')
    print 'create ' + destDir + res['filename'].split('.')[0] + '.xml'
    fplog.write('create ' + destDir + res['filename'].split('.')[0] + '.xml\n')
    fp.write(doc.toxml())
    fp.close()

def main():
    for res in results:
        fp1 = open(sourDir + res['filename'], 'w')
        fp1.write('aaa')
        fp1.close()
        if os.path.isfile(sourDir + res['filename']):
            fplog.write('find file ' + sourDir + res['filename'] + '\n')
            cmdline = 'move ' +  '/-Y '+sourDir + res['filename'] + ' ' + destDir + res['filename']
            print cmdline
            mvflag = os.system(cmdline)
            print mvflag
            fplog.write(cmdline +'\n' + 'move file ' + sourDir + res['filename'] + ' successfull!\n')
            print 'move file ' + sourDir + res['filename'] + ' successfull!\n'
            createxml(res)
            cu.execute("update programinfo set  bak1 = 2 where filename = " + "'" + res['filename'] + "'" )
            conn.commit()

        elif os.path.isfile(destDir + res['filename']):
            print 'find file ' + destDir + res['filename']
            fplog.write('find file ' + destDir + res['filename'])
            createxml(res)
            print "update programinfo set  bak1 = 2 where filename = " + "'" + res['filename'] + "'"
            cu.execute("update programinfo set  bak1 = 2 where filename = " + "'" + res['filename'] + "'" )
            conn.commit()
        else:	
            print 'cannot find file ' + res['filename']
            fplog.write('cannot find file ' + res['filename'] + '\n')
    fplog.close()
    conn.close()

if __name__ == '__main__':
    top = Tkinter.Tk()
    move = Tkinter.Button(top, width=10, height=5, text='move', command=main)
    quit = Tkinter.Button(top, width=10, height=5, text='quit', command=top.quit)
    move.pack({"side": "left"})
    quit.pack({"side": "right"})
    Tkinter.mainloop()
