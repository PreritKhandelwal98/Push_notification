import os
import json
from app.kafka_producer import KafkaProducerClient
from app.config import KAFKA_TOPIC
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Kafka producer client
producer_client = KafkaProducerClient()

def send_email(message, recipient):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = os.getenv('EMAIL_SENDER')
    password = os.getenv('EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = "Flight Status Update"

    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, msg.as_string())

    print(f"Email sent to {recipient}")

def send_sms(message, recipient):
    from twilio.rest import Client

    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=recipient
    )

    print(f"SMS sent to {recipient}")

def send_push_notification(message, recipient):
    import firebase_admin
    from firebase_admin import credentials, messaging

    cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

    message = messaging.Message(
        notification=messaging.Notification(
            title='Flight Status Update',
            body=message
        ),
        token=recipient  # This should be the device token
    )

    response = messaging.send(message)
    print(f"Push notification sent: {response}")

def send_notification(notification_type, message, recipient):
    try:
        if notification_type == 'email':
            send_email(message, recipient)
            print(f"Email sent to {recipient} with message: {message}")
            return "Email sent successfully"
        elif notification_type == 'sms':
            send_sms(message, recipient)
            print(f"SMS sent to {recipient} with message: {message}")
            return "SMS sent successfully"
        elif notification_type == 'app':
            send_push_notification(message, recipient)
            print(f"App notification sent to {recipient} with message: {message}")
            return "App notification sent successfully"
    except Exception as e:
        print(f"Failed to send {notification_type} notification: {str(e)}")
        return f"Failed to send {notification_type} notification: {str(e)}"


