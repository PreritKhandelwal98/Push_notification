from flask import Blueprint, request, jsonify
from app.notifications import send_notification

main = Blueprint('main', __name__)

@main.route('/notify', methods=['POST'])
def notify():
    data = request.json
    message = data.get('message', '')
    send_notification(message)
    return jsonify({'status': 'Message sent'}), 200
