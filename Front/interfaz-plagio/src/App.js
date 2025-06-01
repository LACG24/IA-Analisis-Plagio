import React, { useState } from 'react';
import Header from './Header.js';
import UploadArea from './UploadArea.js';
import Results from './Result.js';

function App() {
  const [files, setFiles] = useState([]);
  const [results, setResults] = useState(null);

  const handleFilesChange = (newFiles) => {
    setFiles(newFiles);
  };

  const handleAnalyze = async () => {
  const readFiles = await Promise.all(
    files.map(async (file) => {
      const content = await file.text();
      return { name: file.name, content };
    })
  );

  setResults(readFiles);
};


  const resetApp = () => {
    setFiles([]);
    setResults(null);
  };

  return (
    <div className="min-h-screen bg-white">
      <Header onReset={resetApp} />
      {results ? (
        <Results data={results} />
      ) : (
        <UploadArea onChange={setFiles} onAnalyze={handleAnalyze} files={files} />
      )}
    </div>
  );
}

export default App;