import time
import threading
from app import create_app, get_socketio
from app.models import get_flight_status_by_id
from app.notifications import send_notification

# Create the app and initialize SocketIO
app = create_app()
socketio = get_socketio()

FLIGHT_ID = "XYZ123"  # Replace with the desired flight ID
CHECK_INTERVAL = 5  # 5 seconds for testing purposes

def monitor_flight_status():
    previous_status = None
    while True:
        try:
            # Fetch the latest flight status from the database by flight_id
            flight_status = get_flight_status_by_id(FLIGHT_ID)
            if flight_status and flight_status['status'] != previous_status:
                message = f"Flight {flight_status['flight_id']} status changed to {flight_status['status']}."
                
                # Emit status update via Socket.IO
                socketio.emit('status_update', {
                    'message': message, 
                    'flight_id': flight_status['flight_id'], 
                    'status': flight_status['status']
                })
                
                # Send notifications
                notification_message = f"Flight {flight_status['flight_id']} status changed to {flight_status['status']}."
                recipient1 = 'prerit.web@gmail.com'
                recipient2 = '+917976271478'

                send_notification('email', notification_message, recipient1)
                send_notification('sms', notification_message, recipient2)

                previous_status = flight_status['status']
            
            time.sleep(CHECK_INTERVAL)  # Wait for the interval before next update
        except Exception as e:
            print(f"Exception occurred: {str(e)}")
            time.sleep(10)  # Wait before retrying in case of an error

if __name__ == "__main__":
    # Start the flight status monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor_flight_status)
    monitor_thread.start()

    # Start the SocketIO server
    socketio.run(app, host='0.0.0.0', port=5000)
