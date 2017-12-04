import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from database import selectItem, manageItem

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help="This field cannot be left blank"
    )

    @jwt_required()
    def get(self, name):
        try:
            item = self.find_by_ItemName(name)
        except:
            return { 'message' : "An error occurred inserting the item" }, 500

        return ({'items': {'name': item[0], 'price': item[1]}} , 200) if item else ({ 'message': 'Item not found'},404)

    def post(self, name):
        data = Item.parser.parse_args()
        
        if  self.find_by_ItemName(name):
            return {'message': 'Item already exist'}, 400

        item = {'name': name, 'price': data['price']}
        
        try:
            self.manageItem(item)
        except:
            return self.errorMessage()

        return item , 201
    
    def put(self, name):
        data = Item.parser.parse_args()
        updated_item = {'name': name, 'price': data['price']}
        item = self.find_by_ItemName(name)

        if item is None:
            try:
                self.manageItem(updated_item)
            except:
               return self.errorMessage()
        else:
            try: 
                manageItem("UPDATE items SET price=? WHERE name=?", (data['price'], name))
            except:
               return self.errorMessage()
    
        return updated_item

    def delete(self, name):
        manageItem("DELETE FROM items WHERE name=?", (name,))
        return {'message': 'Item deleted'}, 400

    def errorMessage(self):
        return { 'message' : "An error occurred inserting the item" }, 500

class ItemList(Resource):
    def get(self):
        return {'items': items}, 200


