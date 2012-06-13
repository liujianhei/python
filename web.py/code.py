import web

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/add', 'add',
    '/input', 'input',
    '/.*', 'example',
)

app = web.application(urls, globals())

db = web.database(dbn='sqlite', db='todo.db')

class hello:
    def GET(self):
        return 'Hello, world!'
class redirect:
    def GET(self, path):
        web.seeother('/' + path)

class index:
    def GET(self):
        todos = db.select('todo')
        return render.index(todos)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')

class example:
    def GET(self):
        referer = web.ctx.env.get('HTTP_REFERER', 'http://google.com')
        print referer
        raise web.seeother(referer)

class input:
    def GET(self):
        user_data = web.input(id=[])
        return "<h1>" +",".join(user_data.id) + "</h1>"
if __name__ == "__main__": app.run()
