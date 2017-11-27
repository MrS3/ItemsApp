from user import User

users = [
    User(1, "Piotr", "asdf")
]

username_mapping = { item.username: item for item in users }
userid_mapping = { item.id: item for item in users }



def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)