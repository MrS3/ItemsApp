from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
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

        return ({'items': {'name': item.name, 'price': item.price}} , 200) if item else ({ 'message': 'Item not found'},404)

    def post(self, name):
        data = Item.parser.parse_args()
        itemModel = ItemModel(name, data['price'])
        if  ItemModel.find_by_ItemName(itemModel.name):
            return {'message': 'Item already exist'}, 400

        try:
            itemModel.save_to_database()
        except:
            return self.errorMessage()

        return itemModel.json() , 201
    
    def put(self, name):
        data = Item.parser.parse_args()
        itemModel = ItemModel.find_by_ItemName(name)
       
        if itemModel is None:
             itemModel = ItemModel(name, data['price'])
        else:
             itemModel.price = data['price']
       
        itemModel.save_to_database()
        return itemModel.json()

    def delete(self, name):
        item = ItemModel.find_by_ItemName(name)
        if item:
            item.delete_from_database()
            return { 'message' : 'Item deleted'}
        return {'message': 'Item not exist'}

    def errorMessage(self):
        return { 'message' : "An error occurred inserting the item" }, 500

class ItemList(Resource):
    def get(self):
        return ItemModel.fetchAllItems()


