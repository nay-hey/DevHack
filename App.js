import React from 'react';
import UploadDataForm from './UploadDataForm';
import DataDashboard from './DataDashboard';

function App() {
  // Replace the following with your actual data or pass them as props
  const messages = [{ category: 'info', message: 'This is an information message.' }];
  const table = '<table><tr><td>Table Content</td></tr></table>';
  const chart = '<div>Your scatter plot content</div>';
  const filename = 'example.csv';

  return (
    <div className="App">
      {/* Use UploadDataForm for the initial upload form */}
      <UploadDataForm />

      {/* Use DataDashboard for displaying data dashboard */}
      <DataDashboard messages={messages} table={table} chart={chart} filename={filename} />
    </div>
  );
}

export default App;
