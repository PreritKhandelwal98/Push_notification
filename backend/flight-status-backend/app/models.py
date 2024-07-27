from app import mongo

def get_flight_status_by_id(flight_id):
    from app import mongo
    flight_status = mongo.db.flight_status.find_one({"flight_id": flight_id})
    return flight_status

