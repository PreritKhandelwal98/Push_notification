# models.py
from app import mongo

def get_flight_status_collection():
    if mongo is None:
        raise ValueError("MongoDB has not been initialized. Ensure the app is created and initialized properly.")
    return mongo.flight_status
