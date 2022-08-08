from werkzeug.wrappers import Request
from flask import request


class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)

