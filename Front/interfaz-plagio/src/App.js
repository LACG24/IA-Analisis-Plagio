import React, { useState } from 'react';
import Header from './Header.js';
import UploadArea from './UploadArea.js';
import Results from './Result.js';

function App() {
  const [files, setFiles] = useState([]);
  const [resultado, setResultado] = useState(null);

  const handleFilesChange = (newFiles) => {
    setFiles(newFiles);
  };

 const handleAnalyze = () => {
  if (files.length < 2) {
    alert("Sube dos archivos para comparar");
    return;
  }

  const formData = new FormData();
  files.forEach(file => {
    formData.append("files", file);
  });


  // Leer contenido de archivos antes de enviarlos
  const leerArchivos = files.map(file => {
    return new Promise(resolve => {
      const reader = new FileReader();
      reader.onload = () => {
        resolve({ name: file.name, content: reader.result });
      };
      reader.readAsText(file);
    });
  });

  Promise.all(leerArchivos).then(archivosLeidos => {
    fetch("http://127.0.0.1:5000/analizar", {
      method: "POST",
      body: formData,
    })
      .then(res => res.json())
      .then(data => {
        setResultado({ archivos: archivosLeidos, texto: data.resultado });
      })
      .catch(error => {
        console.error("Error al enviar archivos:", error);
      });
  });
};

  const resetApp = () => {
    setFiles([]);
    setResultado(null);
  };

  return (
    <div className="min-h-screen bg-white">
      <Header onReset={resetApp} />
      {resultado ? (
        <Results archivos={resultado.archivos}  resultado={resultado.texto}/>
      ) : (
        <UploadArea onChange={handleFilesChange} onAnalyze={handleAnalyze} files={files} />
      )}
    </div>
  );
}

export default App;
