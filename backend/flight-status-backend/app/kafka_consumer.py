from confluent_kafka import Consumer, KafkaException
from app.config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_SASL_MECHANISMS, KAFKA_SECURITY_PROTOCOL, KAFKA_SASL_USERNAME, KAFKA_SASL_PASSWORD, KAFKA_CONSUMER_GROUP

class KafkaConsumerClient:
    def __init__(self):
        self.config = {
            'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
            'sasl.mechanisms': KAFKA_SASL_MECHANISMS,
            'security.protocol': KAFKA_SECURITY_PROTOCOL,
            'sasl.username': KAFKA_SASL_USERNAME,
            'sasl.password': KAFKA_SASL_PASSWORD,
            'group.id': KAFKA_CONSUMER_GROUP,
            'auto.offset.reset': 'earliest'
        }
        self.consumer = Consumer(self.config)

    def start_consuming(self, topic, callback):
        self.consumer.subscribe([topic])

        try:
            while True:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaException._PARTITION_EOF:
                        continue
                    else:
                        print(f"Error: {msg.error()}")
                        break
                callback(msg.value().decode('utf-8'))
        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()
