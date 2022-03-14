import sqlite3
class MetaSingleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
    
class Database(metaclass = MetaSingleton):
    connection = None
    def connect(self):
        if not self.connection:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj
    

db1 = Database().connect()
db2 = Database().connect()

print("Database Object DB1:", db1)
print("Database Object DB2:", db2)

print(db1 is db2)