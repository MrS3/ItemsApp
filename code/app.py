from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'secret123'
api = Api(app)
items = []

class Item(Resource):
    def get(self, name):
        return next(filter(lambda x: x['name'] == name, items), {'item': None})

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return { 'message ', "An item with name '{}' already exist".format(name)} , 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item , 201


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000)

