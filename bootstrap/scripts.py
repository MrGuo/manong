from flask_script import Manager
from flask import Flask
from routers.cli import Cli 

app = Manager(Flask(__name__))

router = Cli(app)
router.load()
