import json

from flask import Blueprint, jsonify, request

from app.api.v1.database.dbcon import address_collection, JSONEncoder

address_bp = Blueprint('address', __name__)
@address_bp.route('/add_address', methods=['POST'])
def add_address():
    data = request.get_json()
    print(json.dumps(data, indent=4))
    address_collection.insert_one(data)
    return jsonify({'message': 'Address added successfully'}), 201

@address_bp.route('/get_address', methods=['GET'])
def get_address():
    addresses = list(address_collection.find())
    return json.dumps(addresses, cls=JSONEncoder)