from flask_pymongo import PyMongo

mongo = PyMongo()

def get_flight_status_collection():
    return mongo.db.flight_status
