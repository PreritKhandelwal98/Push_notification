from app.kafka_producer import KafkaProducerClient
from app.config import KAFKA_TOPIC

def send_notification(message):
    producer_client = KafkaProducerClient()
    producer_client.produce_message(KAFKA_TOPIC, message)
