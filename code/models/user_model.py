from database import selectItem
from datbase import db

class UserModel(db.Model):
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, 'primary_key=True')
    username = db.Column(db.String(100))
    password = db.Column(db.String(80))

    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        row = selectItem("SELECT * FROM users WHERE username=?", username)
        return cls(*row) if row else None

    @classmethod
    def find_by_id(cls,_id):
        row = selectItem("SELECT * FROM users WHERE id=?", _id)
        return cls(*row) if row else None