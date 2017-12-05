import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

def selectAllItems(query):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    result = cursor.execute(query)
    items = []
    for row in result:
        print(row)
        items.append({'name' : row[0], 'price' : row[1]})
    connection.close()
    return items   