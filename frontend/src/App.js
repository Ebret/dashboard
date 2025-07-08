import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [helloMessage, setHelloMessage] = useState('');
  const [allData, setAllData] = useState([]);

  useEffect(() => {
    // Fetch hello message
    fetch('http://localhost:5000/graphql', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify({
        query: '{ hello }'
      })
    })
      .then(r => r.json())
      .then(data => setHelloMessage(data.data.hello));

    // Fetch all data
    fetch('http://localhost:5000/graphql', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify({
        query: '{ allData { id name } }'
      })
    })
      .then(r => r.json())
      .then(data => setAllData(data.data.allData));

  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>{helloMessage}</p>
        <h2>All Data from Oracle DB:</h2>
        <ul>
          {allData.map(item => (
            <li key={item.id}>{item.id}: {item.name}</li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;