""" Python Management Interface """

import http.server
import urllib.parse

class PyMXServer(http.server.HTTPServer):
    def __init__(self, get_registry, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_registry = get_registry

class PyMXHandler(http.server.BaseHTTPRequestHandler):
    def do_GET():
        #TODO: parse query string
        parsed_url = urllib.parse.urlparse(self.path)
        query_args = urllib.parse.parse_qs(parsed_url.query)
        self.server.get_registry[parsed_url.path](query_args)

class PyMX:
    def __init__(self, address="", port=8765):
        self.address = address
        self.port = port

        self.get_registry = {}

    def register_get(self, func, path):
        self.get_registry[path] = func

    def run(self):
        server = PyMXServer(self.get_registry, (self.address, self.port), PyMXHandler)
        server.serve_forever()

_pymx = PyMX()
_server_thread = None

def config(address, port):
    _pymx.address = address
    _pymx.port = port

def run():
    _pymx.run()

def start():
    _server_thread = thrading.Thread(target=run, daemon=True)
    _server_thread.start()

def pymx_get(func, path):
    # TODO: sanity check signature of func
    # register this function as a pymx method
    _pymx.register_get(func, path)
    return func
