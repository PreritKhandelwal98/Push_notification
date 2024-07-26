# app/mock_data.py

import random

def get_mock_flight_status():
    # Example statuses
    statuses = ['On Time', 'Delayed', 'Cancelled', 'Boarding','Gate Changed']
    # Simulate flight status change
    return {
        'flight_id': 'FL123',
        'status': random.choice(statuses)
    }
