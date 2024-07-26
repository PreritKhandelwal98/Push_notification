from kafka import KafkaProducer
import json
from app.config import Config

producer = KafkaProducer(
    bootstrap_servers=Config.KAFKA_BROKER_URL,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_notification(flight_number, status):
    notification = {
        'flight_number': flight_number,
        'status': status,
        'type': 'status_update'
    }
    producer.send(Config.KAFKA_TOPIC, notification)
