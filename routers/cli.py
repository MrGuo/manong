from flask_script import Manager
from flask_script import Command
from config import command 

class Cli:
    def __init__(self, api):
        self.api = api
        self.routers = command.router_conf

    def load(self):
        for item in self.routers:
            name = item.get('name')
            fromName = "app.scripts.%s" % (item.get('path').replace('/', '.'))
            tmpModule = __import__(fromName, globals(), locals(), 'R')
            self.api.add_command(name, tmpModule.R)
