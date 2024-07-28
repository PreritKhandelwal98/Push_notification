# Real-Time Flight Status Notification System

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
  - [Frontend](#frontend)
  - [Backend](#backend)
  - [Notifications](#notifications)
  - [Additional Tools and Libraries](#additional-tools-and-libraries)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Frontend](#frontend-setup)
  - [Backend](#backend-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Screenshots](#screenshots)

## Overview

This project is a Real-Time Flight Status Notification System designed to provide passengers with up-to-date information on their flights, including delays, cancellations, and gate changes. The system sends notifications via SMS, email, and app notifications and integrates with airport systems to ensure accurate and timely information.

## Features

- **Real-time Updates:** Display current flight status including delays, cancellations, and gate changes.
- **Push Notifications:** Send notifications for flight status changes via SMS, email, or app notifications.
- **Integration with Airport Systems:** Pull data from airport databases for accurate information (mock data provided).

## Tech Stack

### Frontend

- **React.js:** Used for building the user interface.

### Backend

- **Python:** Used for backend logic and API development.
- **Socket.IO:** Used for real-time communication between server and clients.
- **Confluent Cloud:** Used for Kafka message brokering.
- **MongoDB:** Used as the primary database.

### Notifications

- **Gmail SMTP:** Used for sending email notifications.
- **Twilio:** Used for sending SMS notifications.
- **Firebase Cloud Messaging:** Used for app notifications (planned).

### Additional Tools and Libraries

- **Socket.IO Client:** For real-time communication with the server.
- **Confluent Kafka Python Client:** For producing and consuming Kafka messages.
- **PyMongo:** For interacting with MongoDB.
- **Requests:** For handling HTTP requests.
- **Threading:** For running background tasks in the backend.

## Setup Instructions

### Prerequisites

- Node.js and npm
- Python 3.x
- MongoDB
- Kafka with Confluent Cloud
- Gmail account for SMTP
- Twilio account for SMS

### Frontend Setup

1. Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Start the React application:
    ```bash
    npm start
    ```

### Backend Setup

1. Navigate to the `backend` directory:
    ```bash
    cd backend
    cd flight-status-backend
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the environment variables in a `.env` file:
    ```env
    # MongoDB URI
    MONGO_URI=mongodb://localhost:27017/flightstatus

    # Kafka Configuration
    KAFKA_BOOTSTRAP_SERVERS=your_kafka_bootstrap_servers
    KAFKA_SASL_MECHANISMS=PLAIN
    KAFKA_SECURITY_PROTOCOL=SASL_SSL
    KAFKA_SASL_USERNAME=your_kafka_username
    KAFKA_SASL_PASSWORD=your_kafka_password

    KAFKA_TOPIC=flight-notifications
    KAFKA_CONSUMER_GROUP=your_consumer_group

    # Email configuration
    EMAIL_SENDER=your_email@gmail.com
    EMAIL_PASSWORD=your_email_password
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587

    # Twilio configuration
    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_phone_number

    # Firebase configuration
    FIREBASE_CREDENTIALS_PATH=path/to/your/firebase/credentials.json
    ```

5. Run the backend services:
    ```bash
    python -m app.consumer_service
    python status_monitor.py
    ```

## Running the Application

1. Start the frontend and backend services as described in the setup instructions.
2. Open your browser and navigate to `http://localhost:3000` to view the flight status dashboard.

## Usage

- The flight status dashboard will display the current status of flights.
- Status updates will be received in real-time via WebSocket and displayed on the dashboard.
- Notifications will be sent via email and SMS for any status changes.

## Contributing

Feel free to fork this repository and submit pull requests for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact [prerit.web@gmail.com](mailto:prerit.web@gmail.com).

## Screenshots

<img width="754" alt="Screenshot 2024-07-28 160109" src="https://github.com/user-attachments/assets/6f90fec9-8c84-49d7-a802-02e897cd254c">

<img width="620" alt="Screenshot 2024-07-28 160137" src="https://github.com/user-attachments/assets/e926e458-7a7d-4913-b844-f4a2fab7fed9">

<img width="709" alt="Screenshot 2024-07-28 160205" src="https://github.com/user-attachments/assets/6f9d497c-610a-42ea-a6ec-b6b1a2ded3e1">

![WhatsApp Image 2024-07-28 at 16 07 41_e5060706](https://github.com/user-attachments/assets/515b6dcc-bec0-4af9-a599-514b4fb4d95d)


