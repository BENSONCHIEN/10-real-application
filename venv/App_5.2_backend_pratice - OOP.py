import sqlite3

class Database:
    #each function need add self parameter
    #do not need to first two lines in each function (init have it)
    def __init__(self,db):
        self.conn = sqlite3.connect("books.db")
        self.cur = conn.cursor() # can go to all function
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text,author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()


    def view(self): #都要加self
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title =? OR author =? OR year =? OR isbn = ?",(title, author, year, isbn))
        rows = self.cur.fetchall
        return rows

    def delete(self,id):  # refer id
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()

    def update(self,id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title =?, author =?, year =?, isbn = ? WHERE id = ?",(title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
#多打了OR,所有一直不行


