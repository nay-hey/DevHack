import React from 'react';

const DataDashboard = ({ messages, table, chart, filename }) => {
  return (
    <div className="container mt-5">
      <h1 className="mb-4">Data Dashboard</h1>

      {messages && messages.map(({ category, message }, index) => (
        <div key={index} className={`alert alert-${category} alert-dismissible fade show`} role="alert">
          {message}
          <button type="button" className="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
      ))}

      <h2 className="mb-3">Descriptive Statistics</h2>
      {table && <div dangerouslySetInnerHTML={{ __html: table }}></div>}

      <h2 className="mt-5 mb-3">Scatter Plot</h2>
      {chart && <div dangerouslySetInnerHTML={{ __html: chart }}></div>}

      <p className="mt-3">File: {filename}</p>
    </div>
  );
}

export default DataDashboard;
