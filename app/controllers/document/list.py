from flask_restful import reqparse, abort, Api, Resource
from app.repositories.source_service import sourceService
from flask import render_template, current_app

class Api(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('section', type=int, help='invalid argument')
        parser.add_argument('key', type=str, help='invalid argument')
        args = parser.parse_args()
        current_app.logger.error('parameters %s', args.key)

        service = sourceService(38)
        service.exec()
        return service.res(), 200
