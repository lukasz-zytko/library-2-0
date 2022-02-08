from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData
from sqlite3 import Error

engine = create_engine('sqlite:///library.db', connect_args={'check_same_thread': False})
metadata = MetaData()


class SQLite:
    def __init__(self):
        self.conn = None
        try:          
            self.conn = engine.connect()
        except Error as e:
            print(e)

    def get_table(self,table_name):
        self.conn = engine.connect() 
        self.table_name = table_name
        table = Table(self.table_name, metadata, autoload=True, autoload_with=engine)
        with self.conn as conn:
            result = conn.execute(table.select()).fetchall()
        return result
    
    def add(self,table_name,data):
        self.table_name = table_name
        self.data = data
        self.conn = engine.connect()
        data.pop("csrf_token")
        table = Table(self.table_name, metadata, autoload=True, autoload_with=engine)
        if table_name == "book":
            ins = table.insert().values(title=data["title"], series = data["series"], pages = data["pages"], author_id = data["author_id"])
        elif table_name == "author":
            ins = table.insert().values(name=data["name"], origin = data["origin"])
        elif table_name == "borrow":
            ins = table.insert().values(book_id=data["book_id"], status = data["status"], date = data["date"])    
        
        with self.conn as conn:
            conn.execute(ins)
        return str(ins)
        

    
table = SQLite()