import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // For global, reset styles
import App from './App'; // Our main component

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);