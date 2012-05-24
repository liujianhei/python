import os, web, time
import sqlite3 as db

urls = (
    '/', 'hello',
    '/add', 'add',
    )
render = web.template.render('templates/')

class hello:
    def GET(self):
        s = ""
        sdb = sqldb()
        rec = sdb.cu.execute("""select * from msgs""")
        dbre = sdb.cu.fetchall()
        web.header("Content-Type", "text/html; charset=utf-8")
        return render.index(dbre)

class add:
    def POST(self):
        i = web.input('content')
        n = web.input('uname')
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sdb = sqldb()
        rec = sdb.cu.execute("""select * from msgs""")
        dbre = sdb.cu.fetchall()
        for k in dbre:
            j = k[0]+1
        t = (j, n.uname, date, i.content)
        sdb.cu.execute('insert into msgs values(?,?,?,?)', t)
        sdb.conn.commit()
        return web.seeother('/')

class sqldb:
    def __init__(self):
        if os.path.exists("msg.db"):
            self.conn = db.connect("msg.db")
            self.cu = self.conn.cursor()
        else:
            self.conn = db.connect("msg.db")
            self.cu = self.conn.cursor()
            self.cu.execute("""create table msgs(
                id integer primary key,
                name text,
                date text,
                content text)""")
            self.cu.execute("""insert into msgs values(1, 'Ahai', '2012-05-24 22:52:00', 'Ahi alaws be ok!')""")
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
         
