# kafka_producer.py
import json
from confluent_kafka import Producer
from app.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_SASL_MECHANISMS, KAFKA_SECURITY_PROTOCOL, KAFKA_SASL_USERNAME, KAFKA_SASL_PASSWORD

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

    def produce_message(self, topic, message):
        def delivery_report(err, msg):
            if err is not None:
                print(f"Message delivery failed: {err}")
            else:
                print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

        self.producer.produce(topic, value=json.dumps(message), callback=delivery_report)
        self.producer.flush()
