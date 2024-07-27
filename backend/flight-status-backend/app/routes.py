import json
from flask import Blueprint, request, jsonify
from bson import ObjectId
from app.models import get_flight_status_by_id

main = Blueprint('main', __name__)

@main.route('/api/flight-status', methods=['GET'])
def flight_status():
    flight_id = request.args.get('flight_id')
    if not flight_id:
        return jsonify({"error": "Flight ID is required"}), 400

    flight_status = get_flight_status_by_id(flight_id)
    
    # Convert ObjectId to string if present
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
