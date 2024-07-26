import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/flightstatus')
    KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL', 'localhost:9092')
    KAFKA_TOPIC = 'flight_notifications'
