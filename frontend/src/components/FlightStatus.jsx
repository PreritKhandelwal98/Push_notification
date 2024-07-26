import { useEffect, useState } from 'react';

const FlightStatus = () => {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    const fetchFlightStatus = async () => {
      const response = await fetch('/api/flight-status');
      const data = await response.json();
      setFlights(data);
    };

    fetchFlightStatus();
    const interval = setInterval(fetchFlightStatus, 10000); // Update every 10 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h1>Flight Status</h1>
      <ul>
        {flights.map((flight) => (
          <li key={flight.id}>{flight.status}</li>
        ))}
      </ul>
    </div>
  );
};

export default FlightStatus;
