import React, { useState } from 'react';
import './index.js'
import Header from './Header.js';
import UploadArea from './UploadArea.js';
import Results from './Result.js';
import CompararFunciones from './CompararFunciones.js';

function App() {
  const [files, setFiles] = useState([]);
  const [resultado, setResultado] = useState(null);
  const [resultadoF, setResultadoF] = useState(null);
  const [modoAnalisis, setModoAnalisis] = useState("completo"); // "completo" o "funciones"
  const [mostrarAnalisisCompleto, setMostrarAnalisisCompleto] = useState(false);
  const [mostrarComparacion, setMostrarComparacion] = useState(false);

  const handleFilesChange = (newFiles) => {
    setFiles(newFiles);
  };

  const resetApp = () => {
    setFiles([]);
    setResultado(null);
    setMostrarComparacion(false);
    setMostrarAnalisisCompleto(false);
  };

  const handleAnalyzeCompleto = () => {
    if (files.length < 2) {
      alert("Sube al menos dos archivos para analizar");
      return;
    }

    setMostrarAnalisisCompleto(true);
  };

  const handleAnalyzeFunciones = () => {
    if (files.length !== 2) {
      alert("Debes subir exactamente dos archivos para comparar funciones.");
      return;
    }
    setMostrarComparacion(true); // esto hace que <CompararFunciones files={files} /> se renderice
  };

  const handleAnalyze = () => {
    if (modoAnalisis === "completo") {
      handleAnalyzeCompleto();
    } else {
      handleAnalyzeFunciones();
    }
  };

  return (
    <div className="min-h-screen bg-white">
      <Header onReset={resetApp} />

      <div className="mb-4 p-4">
        <label className="mr-2 font-semibold">Modo de análisis:</label>
        <select
          value={modoAnalisis}
          onChange={(e) => setModoAnalisis(e.target.value)}
          className="border px-2 py-1 rounded"
        >
          <option value="completo">Archivo completo</option>
          <option value="funciones">Por funciones</option>
        </select>
      </div>

      {modoAnalisis === "completo" && mostrarAnalisisCompleto && (
        <Results files = {files} />
      )}

      {((modoAnalisis === "completo" && !mostrarAnalisisCompleto) ||
        (modoAnalisis === "funciones" && !mostrarComparacion)) && (
        <UploadArea
          onChange={handleFilesChange}
          onAnalyze={handleAnalyze}
          files={files}
          modo={modoAnalisis}
        />
      )}

      {modoAnalisis === "funciones" && mostrarComparacion && (
        <CompararFunciones files={files} />
      )}


    </div>
  );
}

export default App;
