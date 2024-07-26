from pymongo import MongoClient
from app.mock_data import get_mock_flight_status
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client.get_database()
flight_status_collection = db.flight_status

def initialize_db():
    # Insert mock flight status data
    flight_status = get_mock_flight_status()
    flight_status_collection.insert_one(flight_status)
    print("Database initialized with mock data")

if __name__ == "__main__":
    initialize_db()
