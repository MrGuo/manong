from app.model.dao.source_model import sourceModel
import json

class sourceService:

    def __init__(self, section):
        self.section = section

    def exec(self):
        model = sourceModel()
        self.data = model.get_by_section(self.section)

    def res(self):
        return self.data
