from flask import Flask
from flask_restful import Api
from routers.web import Web
from response.json import Json
import logging

app = Flask(__name__)

handler = logging.FileHandler('/home/work/logs/flask.log')
app.logger.addHandler(handler)

api = Api(app)

router = Web(api)
router.load()

response = Json(api)
response.load()
