import pymysql


class baseModel:

    __connections = {}

    def __init__(self):
        self.__connections = {}

    def connection(self):
        if self.__connection__ not in self.__connections:
            self.__init_connection()
        return self.__connections[self.__connection__]

    def __init_connection(self):
        self.__connections[self.__connection__] = pymysql.connect("localhost", "root", "tab_123456", "manong")

    def write(self, sql, para):
        connection = self.connection()
        result = 0
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, para)
            connection.commit()
        finally:
            return result

    def read(self, sql, para):
        connection = self.connection()
        result = []
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql, para)
                result = cursor.fetchall()
        finally:
            return result
