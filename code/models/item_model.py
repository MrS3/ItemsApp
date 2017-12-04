from database import manageItem, selectItem

class ItemModel:
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
    def deleteItem(cls, name):
        manageItem("DELETE FROM items WHERE name=?", (name,))
        return {'message': 'Item deleted'}, 400

    @classmethod
    def find_by_ItemName(cls, name):
        row = selectItem("SELECT * FROM items WHERE name=?", name)
        return cls(*row) if row else None

