# test_producer.py
from app.notifications import send_email, send_sms, send_push_notification

# Test email notification
send_email("Test Email Message", "prerit.web@gmail.com")

# Test SMS notification
send_sms("Test SMS Message", "+917976271478")

# Test push notification
# send_push_notification("Test Push Message", "recipient_device_token")
