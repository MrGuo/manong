import json
from flask import  make_response

class Json:
    def __init__(self, api):
        self.api = api

    def load(self):
        self.api.representations = {
            'application/json': self.output_json,
        }

    def output_json(self, data, code, headers=None):
        resp = make_response(json.dumps(data), code)
        resp.headers.extend(headers or {})
        return resp
