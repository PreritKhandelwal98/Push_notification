from flask import Blueprint, jsonify, request
from app.models import get_flight_status_collection
from app.notifications import send_notification
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/api/flight-status', methods=['GET'])
def get_flight_status():
    flight_status_collection = get_flight_status_collection()
    flight_status_list = flight_status_collection.find()
    result = []
    for flight in flight_status_list:
        result.append({
            'id': str(flight['_id']),
            'flight_number': flight['flight_number'],
            'status': flight['status'],
            'updated_at': flight['updated_at']
        })
    return jsonify(result)

@main.route('/api/flight-status', methods=['POST'])
def update_flight_status():
    data = request.json
    flight_number = data.get('flight_number')
    status = data.get('status')
    updated_at = datetime.utcnow()

    if not flight_number or not status:
        return jsonify({'error': 'Missing data'}), 400

    flight_status_collection = get_flight_status_collection()
    flight_status_collection.update_one(
        {'flight_number': flight_number},
        {'$set': {'status': status, 'updated_at': updated_at}},
        upsert=True
    )

    send_notification(flight_number, status)
    
    return jsonify({'message': 'Flight status updated'}), 200
