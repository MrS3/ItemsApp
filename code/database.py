import sqlite3

def selectItem(query, *args):
     connection = sqlite3.connect('data.db')
     cursor = connection.cursor()
     result = cursor.execute(query, args)
     row = result.fetchone()
     connection.close()
     return row


def insertItem(query, args):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute(query, args)
    connection.commit()
    connection.close()