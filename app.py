from flask import Flask, jsonify, request

app = Flask(__name__)


stores = [

    {
        'name': 'codemart',
        'items':[
            {
                'name':'shoe',
                'Price':'500'
            }
        ]
    },
    {
                'name': 'mikesoft',
                'items': [
                    {
                        'name': 'laptop bag',
                        'Price': '4500'
                    }
    ]
}
]
#POST store data:{name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'item':[]
}
    stores.append(new_store)
    return jsonify(new_store)


#Get /store/<sting:name>

@app.route('/store/<string:name>')
def get_store_name(name):
#iterate the store to get store name
    for store in stores:
        if store['name'] == name:
                return jsonify(store)

        return jsonify({"message":"store not found"})

#Post /store/<string:name/item{name:price}

@app.route('/store/<string:name>/item',methods = ['POST'])
def create_item_in_store(name):
#regust data
    request_data = request.get_json()
#iterate through the store
    for store in stores:
        if store['name'] == name:
            new_item ={
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({"message":"store not found"})



@app.route('/stores')
def get_stores():
    return jsonify({'stores':stores})

app.run(debug=True)