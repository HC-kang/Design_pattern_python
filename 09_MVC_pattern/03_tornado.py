import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute("create table if not exists task (id INTEGER PRIMARY KEY, name TEXT, status NUMERIC)")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        query = "select * from task"
        todos = cur.execute(query)
        print(todos)
        self.render('index.html', todos=todos)


class NewHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name', None)
        query = "create table if not exists task (id INTEGER \
                 PRIMARY KEY, name TEXT, status NUMERIC) "
        cur.execute(query)
        query = f"insert into task (name, status) \
                 values ('{name}', {1})"
        cur.execute(query)
        self.redirect('/')

    def get(self):
        self.render('new.html')


class UpdateHandler(tornado.web.RequestHandler):
    def get(self, id, status):
        query = f"update task set status={int(status)} where \
                 id={id}"
        cur.execute(query)
        self.redirect('/')


class DeleteHandler(tornado.web.RequestHandler):
    def get(self, id):
        query = f"delete from task where id={id}"
        cur.execute(query)
        self.redirect('/')


class RunApp(tornado.web.Application):
    def __init__(self):
        Handlers = [
            (r'/', IndexHandler),
            (r'/todo/new', NewHandler),
            (r'/todo/update/(\d+)/status/(\d+)', UpdateHandler),
            (r'/todo/delete/(\d+)', DeleteHandler),
        ]
        settings = dict(
            debug=True,
            template_path='templates',
            static_path='static'
        )
        tornado.web.Application.__init__(self, Handlers, **settings)


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(3333)
    tornado.ioloop.IOLoop.instance().start()