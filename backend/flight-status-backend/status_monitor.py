from app import create_app, mongo
from app.notifications import send_notification
from app.mock_data import get_mock_flight_status
import time

# Create a Flask app instance
app = create_app()

def monitor_flight_status():
    previous_status = None
    with app.app_context():  # Ensure that the Flask app context is available
        while True:
            flight_status = get_mock_flight_status()
            if flight_status and flight_status != previous_status:
                # Notify about the status change
                message = f"Flight {flight_status['flight_id']} status changed to {flight_status['status']}."
                send_notification(message)
                previous_status = flight_status
            time.sleep(10)  # Check every 10 seconds for testing

if __name__ == "__main__":
    monitor_flight_status()
