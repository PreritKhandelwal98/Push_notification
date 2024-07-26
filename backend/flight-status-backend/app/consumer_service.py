from app.kafka_consumer import KafkaConsumerClient
from app.config import KAFKA_TOPIC

def message_callback(message):
    print(f"Received message: {message}")

consumer_client = KafkaConsumerClient()
consumer_client.start_consuming(KAFKA_TOPIC, message_callback)
