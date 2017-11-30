import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from database import selectItem, insertItem

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help="This field cannot be left blank"
    )

    #@jwt_required()
    def get(self, name):
        item = self.find_by_ItemName(name)
        return ({'items': {'name': item[0], 'price': item[1]}} , 200) if item else ({ 'message': 'Item not found'},404)


    def post(self, name):
        data = Item.parser.parse_args()
        
        if  self.find_by_ItemName(name):
            return {'message': 'Item already exist'}, 400

        insertItem("INSERT INTO items VALUES (?, ?)", (name, data['price']))
        item = {'name': name, 'price': data['price']}
        return item , 201
    
    def delete(self, name):
        global items
        items = list(filter(lambda item: item['name'] != name, items))
        return {'message': 'Item deleted'}, 400

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda item: item['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

    @classmethod
    def find_by_ItemName(cls, name):
        item = selectItem("SELECT * FROM items WHERE name=?", name)
        return item if item else None

class ItemList(Resource):
    def get(self):
        return {'items': items}, 200


