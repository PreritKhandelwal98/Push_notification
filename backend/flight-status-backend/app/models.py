from pymongo import MongoClient
from .config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['flightstatus']
collection = db['flight_status']

def get_flight_status_by_id(flight_id):
    return collection.find_one({'flight_id': flight_id})
