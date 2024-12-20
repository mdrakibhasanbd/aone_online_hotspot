import json

from flask import Blueprint, jsonify, request

from app.api.v1.database.dbcon import address_collection

address_bp = Blueprint('address', __name__)
@address_bp.route('/add_address', methods=['POST'])
def add_address():
    data = request.get_json()
    print(json.dumps(data, indent=4))
    # insert_documents(address_collection, [data])
    return jsonify({'message': 'Address added successfully'}), 201