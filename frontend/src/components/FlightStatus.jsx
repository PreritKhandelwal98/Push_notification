import { useEffect, useState } from 'react';
import io from 'socket.io-client';
import './FlightStatus.css';  // Import the CSS file for styles

const SOCKET_SERVER_URL = 'http://localhost:5000';

const FlightStatus = () => {
  const [flight, setFlight] = useState(null);
  const [notification, setNotification] = useState(null);
  const [animate, setAnimate] = useState(false);

  useEffect(() => {
    const fetchFlightStatus = async () => {
      try {
        const response = await fetch(`${SOCKET_SERVER_URL}/api/flight-status?flight_id=XYZ123`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setFlight(data);
      } catch (error) {
        console.error("Failed to fetch flight status:", error);
      }
    };

    fetchFlightStatus();

    const socket = io(SOCKET_SERVER_URL);

    socket.on('connect', () => {
      console.log('Connected to the WebSocket server');
    });

    socket.on('status_update', (data) => {
      console.log('Status update received:', data);
      setNotification(data.message);
      setFlight((prevFlight) => ({
        ...prevFlight,
        status: data.status,
      }));
      setAnimate(true);
      setTimeout(() => setAnimate(false), 2000); // Animation lasts for 2 seconds
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div>
      <h1>Flight Status</h1>
      {flight ? (
        <div>
          <h2>Flight ID: {flight.flight_id}</h2>
          <p className={`status ${animate ? 'animate' : ''}`}>Status: {flight.status}</p>
        </div>
      ) : (
        <p>Loading flight status...</p>
      )}
    </div>
  );
};

export default FlightStatus;
