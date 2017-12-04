import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from database import selectItem, manageItem
from item_model import ItemModel

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
        itemModel = ItemModel(name, data['price'])
        
        if  ItemModel.find_by_ItemName(itemModel.name):
            return {'message': 'Item already exist'}, 400
        
        try:
            itemModel.manageItem(itemModel)
        except:
            return self.errorMessage()

        return item , 201
    
    def put(self, name):
        data = Item.parser.parse_args()
        updated_item = {'name': name, 'price': data['price']}
        itemModel = ItemModel.find_by_ItemName(name)

        if itemModel is None:
            try:
                itemModel.manageItem(updated_item)
            except:
               return self.errorMessage()
        else:
            try: 
                itemModel.updateItem(data['price'])
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


