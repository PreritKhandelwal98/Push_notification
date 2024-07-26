from app import mongo

def get_flight_status_collection():
    return mongo.db.flight_status
