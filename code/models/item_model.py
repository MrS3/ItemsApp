from database import manageItem, selectItem

class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def manageItem(self , item):
        manageItem("INSERT INTO items VALUES(?,?)", (item['name'], item['price']))

    
    def find_by_ItemName(self, name):
        item = selectItem("SELECT * FROM items WHERE name=?", name)
        return item if item else None