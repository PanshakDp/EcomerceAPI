from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'codemart',
        'item': [
            {
                'name': 'shoe',
                'price': '5,555',
                'brand': 'catepillar'
            }
        ]
    }
]

# POST /store data


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>

@app.route("/store/<string:name>", methods=["GET"])
def get_store(name):
    # iterate thru the store
    for store in stores:
    # if the store name matches, return it
        if store["name"]==name:
            return jsonify(store)
    # if none matches, return error message
    return jsonify({"message": "store not found"})


@app.route("/store", methods=["GET"])
def get_stores():
    return jsonify({'stores': stores})


# GET /store/<string:name>/item {name:,price:, brand:}

@app.route("/store/<string:name>/item {name:,price:, brand:}", methods=["GET"])
def get_store_items():
    pass

# POST /store/<string:name>/item {name:,price:, brand:}


@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"],
                "brand": request_data["brand"]
            }
            store["item"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "store not found"})



app.run(debug=True)