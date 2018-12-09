from app.model.dao.base import baseModel

class sourceModel(baseModel):

    __table__ = "t_manong_source"
    __connection__ = "manong"
    
    def __init__(self):
        pass

    def get_by_section(self, section):
        sql = "select id, url, title from " + self.__table__ + " where section=%s"
        data = self.read(sql, (section,))
        return data
