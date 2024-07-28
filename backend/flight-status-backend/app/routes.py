import json
from flask import Blueprint, request, jsonify
from bson import ObjectId
from pymongo import MongoClient
from app.config import MONGO_URI

main = Blueprint('main', __name__)

client = MongoClient(MONGO_URI)
db = client['flight_status_db']
collection = db['flights']

@main.route('/api/flight-status', methods=['GET'])
def flight_status():
    flight_id = request.args.get('flight_id')
    if not flight_id:
        return jsonify({"error": "Flight ID is required"}), 400

    flight_status = collection.find_one({'flight_id': flight_id})
    
    if flight_status and '_id' in flight_status and isinstance(flight_status['_id'], ObjectId):
        flight_status['_id'] = str(flight_status['_id'])

    if flight_status:
        return jsonify(flight_status), 200
    else:
        return jsonify({"error": "Flight status not found"}), 404

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(JSONEncoder, self).default(obj)

def init_json_encoder(app):
    app.json_encoder = JSONEncoder
