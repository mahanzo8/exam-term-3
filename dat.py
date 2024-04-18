from sqlite3 import *
class Data_base:
    def __init__(self,db):
        self.con = connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Contacts (id INTEGER PRIMARY KEY,
                name text,fname text,course text,password text )''')
        self.con.commit()
    def insert(self,name,fname,course,password):
        self.cur.execute('''INSERT INTO Contacts VALUES(NULL,?,?,?,?)'''
            ,(name,fname,course,password))
        self.con.commit()
    def fetch(self):
        self.cur.execute('SELECT * FROM Contacts')
        rows = self.cur.fetchall()    
        return rows