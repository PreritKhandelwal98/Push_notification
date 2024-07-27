from app import create_app
from app.models import get_flight_status_by_id

app = create_app()

# Use app context for MongoDB access
with app.app_context():
    flight_status = get_flight_status_by_id("XYZ123")
    print(f"Flight Status: {flight_status}")
