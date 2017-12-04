from database import selectItem

class UserModel:
    
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