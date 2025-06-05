import React, { useEffect, useState } from 'react';
import './result.css';

function CompararFunciones({ files }) {
  const [resultado, setResultado] = useState(null);

  useEffect(() => {
    if (files.length !== 2) return;

    const formData = new FormData();
    files.forEach(file => {
      formData.append("files", file);
    });

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
      fetch("http://127.0.0.1:5000/comparar_similitud", {
        method: "POST",
        body: formData,
      })
        .then(res => res.json())
        .then(data => {
          setResultado({ archivos: archivosLeidos, texto: data.similitudes_altas });
        })
        .catch(error => {
          console.error("Error al comparar funciones:", error);
        });
    });
  }, [files]);

  if (!resultado) return <p>Cargando análisis...</p>;

  return (
    <div className="results-container">
      <h2>Contenido de Archivos</h2>

      <div className="code-list">
        {resultado.archivos.map((item, i) => (
          <div key={i} className="code-box">
            <div className="filename">{item.name}</div>
            <div className="code-content">
              <pre>
                <code>{item.content}</code>
              </pre>
            </div>
          </div>
        ))}
      </div>

      <strong className="mt-6">Resultado del análisis por funciones</strong>
      <div className="result-box">
        {Array.isArray(resultado.texto) && resultado.texto.length > 0 ? (
          resultado.texto.map((r, i) => (
            <pre key={i} className="mb-2">
              Función {r.func1} vs {r.func2} → Similitud: {r.sim_combinada.toFixed(4)}
            </pre>
          ))
        ) : (
          <p>No hay similitudes altas encontradas.</p>
        )}
      </div>
    </div>
  );
}

export default CompararFunciones;
