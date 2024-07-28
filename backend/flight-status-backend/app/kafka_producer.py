import json
import time
from confluent_kafka import Producer
from pymongo import MongoClient
from .config import (
    KAFKA_BOOTSTRAP_SERVERS, KAFKA_SASL_MECHANISMS, KAFKA_SECURITY_PROTOCOL,
    KAFKA_SASL_USERNAME, KAFKA_SASL_PASSWORD, MONGO_URI, KAFKA_TOPIC
)

class KafkaProducerClient:
    def __init__(self):
        self.config = {
            'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
            'sasl.mechanisms': KAFKA_SASL_MECHANISMS,
            'security.protocol': KAFKA_SECURITY_PROTOCOL,
            'sasl.username': KAFKA_SASL_USERNAME,
            'sasl.password': KAFKA_SASL_PASSWORD
        }
        self.producer = Producer(self.config)
        self.client = MongoClient(MONGO_URI)
        self.db = self.client['flightstatus']
        self.collection = self.db['flight_status']
        self.previous_statuses = {}

    def produce_message(self, topic, message):
        def delivery_report(err, msg):
            if err is not None:
                print(f"Message delivery failed: {err}")
            else:
                print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

        self.producer.produce(topic, value=json.dumps(message), callback=delivery_report)
        self.producer.flush()

    def check_and_publish_updates(self):
        while True:
            flights = self.collection.find({})
            for flight in flights:
                flight_id = flight['flight_id']
                current_status = flight['status']
                if self.previous_statuses.get(flight_id) != current_status:
                    message = {
                        'flight_id': flight['flight_id'],
                        'status': flight['status'],
                        'delay_minutes': flight['delay_minutes'],
                        'gate': flight['gate'],
                        'type': 'status_update',
                        'recipient': 'example@example.com',
                        'message': f"Flight {flight['flight_id']} status changed to {flight['status']}."
                    }
                    self.produce_message(KAFKA_TOPIC, message)
                    self.previous_statuses[flight_id] = current_status
            time.sleep(5)  # Poll every 5 seconds for updates

if __name__ == "__main__":
    producer_client = KafkaProducerClient()
    producer_client.check_and_publish_updates()
