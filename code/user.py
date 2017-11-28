
import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        return User.databaseQuery(cls, username, "SELECT * FROM users WHERE username=?")


    @classmethod
    def find_by_id(cls,_id):
        return User.databaseQuery(cls, _id, "SELECT * FROM users WHERE id=?")

    @classmethod
    def databaseQuery(objc = None, _id = None, username = None, query = None):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute(query,(username,)) if username else cursor.execute(query, (_id,))
        row = result.fetchone()
        connection.close()
        return objc(*row) if row else None  