import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from database import selectItem, manageItem
from models.item_model import ItemModel

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
            item = ItemModel.find_by_ItemName(name)
        except:
            return { 'message' : "An error occurred inserting the item" }, 500

        return ({'items': {'name': item[0], 'price': item[1]}} , 200) if item else ({ 'message': 'Item not found'},404)

    def post(self, name):
        data = Item.parser.parse_args()
        itemModel = ItemModel(name, data['price'])
        if  ItemModel.find_by_ItemName(itemModel.name):
            return {'message': 'Item already exist'}, 400

        try:
            itemModel.insertItem()
        except:
            return self.errorMessage()

        return itemModel.json() , 201
    
    def put(self, name):
        data = Item.parser.parse_args()
        updatedItemModel = ItemModel(name ,data['price'])
        itemModel = ItemModel.find_by_ItemName(name)
        if itemModel is None:
            try:
                updatedItemModel.insertItem()
            except:
               return self.errorMessage()
        else:
            try: 
                itemModel.updateItem(updatedItemModel.price)
            except:
               return self.errorMessage()
    
        return updatedItemModel.json()


    def delete(self, name):
        return ItemModel.manageItem("DELETE FROM items WHERE name=?", (name,))

    def errorMessage(self):
        return { 'message' : "An error occurred inserting the item" }, 500

class ItemList(Resource):
    def get(self):
        return {'items': items}, 200


