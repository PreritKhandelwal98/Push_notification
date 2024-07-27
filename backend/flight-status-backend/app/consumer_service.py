# consumer_service.py
import json
from app.kafka_consumer import KafkaConsumerClient
from app.notifications import send_email, send_sms, send_push_notification

def message_callback(message, topic):
    print(f"Received message on topic {topic}: {message}")
    notification = json.loads(message)

    if topic == 'email_notifications':
        send_email(notification['message'], notification['recipient'])
    elif topic == 'sms_notifications':
        send_sms(notification['message'], notification['recipient'])
    elif topic == 'app_notifications':
        send_push_notification(notification['message'], notification['recipient'])

consumer_client = KafkaConsumerClient()
consumer_client.start_consuming(
    ['email_notifications', 'sms_notifications', 'app_notifications'],
    message_callback
)
