from database import db

class ItemModel(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name' : self.name, 'price' : self.price}

    def save_to_database(self):
         db.session.add(self)
         db.session.commit()

    @classmethod
    def fetchAllItems(self):
        return selectAllItems("SELECT * FROM items") , 200

    @classmethod    
    def delete_from_database(cls):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_ItemName(cls, name):
        return cls.query.filter_by(name = name).first()
        
