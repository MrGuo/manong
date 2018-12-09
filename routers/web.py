from flask_restful import Api
from config import router

class Web:
    def __init__(self, api):
        self.api = api
        self.routers = router.router_conf

    def load(self):
        for item in self.routers:
            fromName = "app.controllers.%s" % (item.replace('/', '.'))
            tmpModule = __import__(fromName, globals(), locals(), 'Api')
            urlPath = "/%s" % (item)
            self.api.add_resource(tmpModule.Api, urlPath, endpoint="api.%s" % (item.replace('/', '.')))

