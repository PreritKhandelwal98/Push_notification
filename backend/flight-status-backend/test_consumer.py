from app.consumer_service import consumer_client, message_callback
from app.config import KAFKA_TOPIC

if __name__ == "__main__":
    consumer_client.start_consuming(KAFKA_TOPIC, message_callback)
