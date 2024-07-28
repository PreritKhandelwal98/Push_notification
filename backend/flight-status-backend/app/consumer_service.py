import json
from .kafka_consumer import KafkaConsumerClient
from .notifications import send_email, send_sms, send_push_notification
from .config import KAFKA_TOPIC

def message_callback(message, topic):
    print(f"Received message on topic {topic}: {message}")
    try:
        notification = json.loads(message)
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON message: {e}")
        return

    if notification['type'] == 'email':
        send_email(notification['message'], notification['recipient'])
    elif notification['type'] == 'sms':
        send_sms(notification['message'], notification['recipient'])
    elif notification['type'] == 'app':
        send_push_notification(notification['message'], notification['recipient'])

consumer_client = KafkaConsumerClient()
consumer_client.start_consuming([KAFKA_TOPIC], message_callback)
