import sqlite3

# FIXME: is it even needed.

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

    def get(self, table):
        result = self.cursor.execute('SELECT * FROM {}'.format(table))
        self.finalize()
        return result

    def drop(self, table):
        self.cursor.execute("DROP TABLE IF EXISTS {}".format(table))
        self.finalize()

    def finalize(self):
        self.connection.commit()

    def close(self):
        self.connection.close()


i = Inject()
i.drop("lov")
i.create("CREATE TABLE lov ( name text, email text, password text )")
i.insert("lov", "a", "d", "ds")
print(i.get("lov").fetchall())
i.close()
