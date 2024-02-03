
import React, { useState } from 'react';
import DataDashboard from './DataDashboard';  // Adjust the path accordingly

const UploadDataForm = () => {
    const [dashboardData, setDashboardData] = useState(null);
  
    const handleFormSubmit = async (event) => {
      event.preventDefault();
  
      const formData = new FormData(event.target);
  
      try {
        const response = await fetch('/dashboard', {
          method: 'POST',
          body: formData,
        });
  
        const data = await response.json();
        // Handle the response data, e.g., update state
        setDashboardData(data);
      } catch (error) {
        // Handle errors
        console.error('Error submitting form:', error);
      }
    };
  
  return (
    <div>
    {dashboardData ? (
      <DataDashboard
        messages={dashboardData.messages}
        table={dashboardData.table}
        chart={dashboardData.chart}
        filename={dashboardData.filename}
      />
    ) : (
    <div style={{
      fontFamily: 'Arial, sans-serif',
      backgroundColor: '#f4f4f4',
      margin: 0,
      padding: 0,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100vh',
    }}>
      <form style={{
        backgroundColor: '#fff',
        padding: '20px',
        borderRadius: '8px',
        boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
        width: '300px',
        textAlign: 'center',
      }} action="/dashboard" method="post" encType="multipart/form-data">
        <h1 style={{ color: '#333' }}>Upload Your Data</h1>
        <input type="file" name="file" accept=".csv" style={{ marginBottom: '20px' }} />
        <button type="submit" style={{
          backgroundColor: '#4caf50',
          color: '#fff',
          padding: '10px 20px',
          border: 'none',
          borderRadius: '4px',
          cursor: 'pointer',
          fontSize: '16px',
        }}>Generate Dashboard</button>
      </form>
    </div>
    )}
    </div>
  );
}

export default UploadDataForm;
