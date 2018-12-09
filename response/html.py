import json
from flask import  make_response

class Html:
    def __init__(self, api):
        self.api = api

    def load(self):
        self.api.representations = {
            'text/html': output_html,
        }

    def output_html(self, data, code, headers=None):
        resp = make_response(json.dumps(data), code)
        resp.headers.extend(headers or {})
        return resp
