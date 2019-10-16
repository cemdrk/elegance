from tornado import ioloop
from tornado import options
from tornado import httpserver
from tornado import web


class Server(httpserver.HTTPServer):
    pass


class Application(web.Application):
    pass


class BaseHandler(web.RequestHandler):
    pass


class MainHandler(BaseHandler):
    async def get(self):
        self.write({'message': 'Hello, world'})


def make_app():
    return Application([
        (r"/", MainHandler),
    ])


def main():
    app = make_app()
    server = Server(app)

    options.options.define("host", default='127.0.0.1', help="run on the given address", type=str)
    options.options.define("port", default=8888, help="run on the given port", type=int)
    options.options.define("core", default=1, help="running core num", type=int)

    options.options.parse_config_file('elegance.conf')
    options.options.parse_command_line()

    server.bind(port=options.options.port, address=options.options.host)

    server.start(options.options.core)  # Forks multiple sub-processes

    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
