import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
MONGO_URI = os.getenv('MONGO_URI')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
KAFKA_SASL_MECHANISMS = os.getenv('KAFKA_SASL_MECHANISMS')
KAFKA_SECURITY_PROTOCOL = os.getenv('KAFKA_SECURITY_PROTOCOL')
KAFKA_SASL_USERNAME = os.getenv('KAFKA_SASL_USERNAME')
KAFKA_SASL_PASSWORD = os.getenv('KAFKA_SASL_PASSWORD')

#Specific work topic
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
KAFKA_TOPIC_EMAIL= os.getenv('KAFKA_TOPIC_EMAIL')
KAFKA_TOPIC_SMS= os.getenv('KAFKA_TOPIC_SMS')
KAFKA_TOPIC_APP= os.getenv('KAFKA_TOPIC_APP')

#consumer group
KAFKA_CONSUMER_GROUP = os.getenv('KAFKA_CONSUMER_GROUP')
