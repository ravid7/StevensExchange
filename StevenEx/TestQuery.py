import sqlite3

class Inject:

    def __init__(self, temp=False):
        self.connection = None
        if temp:
            self.connection = sqlite3.connect(":memory:")
        else:
            self.connection = sqlite3.connect("./databases/mem.db")
        self.cursor = self.connection.cursor()

    def create(self, query):
        self.cursor.execute(query)
        self.finalize()

    def insert(self, table, *items):
        result = self.cursor.execute("INSERT INTO {} VALUES {}".format(table, items))
        self.finalize()
        return result



    def finalize(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
