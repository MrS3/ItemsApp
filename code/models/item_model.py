from database import insertItem, selectItem, selectAllItems
from database import db

class ItemModel(db.Model):

    __tablename__ = items
    id = db.Columnt(db.Integer, 'primary_key=True')
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name' : self.name, 'price' : self.price}

    def insertItem(self):
         manageItem("INSERT INTO items VALUES(?,?)", (self.name, self.price))

    def updateItem(self, price):
        manageItem("UPDATE items SET price=? WHERE name=?", (price, self.name)) 
    
    @classmethod
    def fetchAllItems(self):
        return selectAllItems("SELECT * FROM items") , 200

    @classmethod    
    def deleteItem(cls, name):
        manageItem("DELETE FROM items WHERE name=?", (name,))
        return {'message': 'Item deleted'}, 400

    @classmethod
    def find_by_ItemName(cls, name):
        row = selectItem("SELECT * FROM items WHERE name=?", name)
        return cls(*row) if row else None

