from flask_restful import reqparse, abort, Api, Resource
from app.repositories.source_service import sourceService
from flask import render_template

class Api(Resource):

    def get(self):
        name = 'cguo'
        return render_template('hello.html', name=name)
