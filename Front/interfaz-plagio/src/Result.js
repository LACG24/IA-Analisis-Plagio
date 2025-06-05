import React, { useEffect, useState } from 'react';
import './result.css';

export default function Results({ files }) {
  const [resultado, setResultado] = useState(null);

  useEffect(() => {
    if (!files || files.length < 2) {
      alert("Sube al menos dos archivos para analizar");
      return;
    }

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
              <pre><code>{item.content}</code></pre>
            </div>
          </div>
        ))}
      </div>

      <h2 className="mt-6">Resultado del análisis</h2>
      <div className="result-box">
        {Array.isArray(resultado.texto) ? (
          resultado.texto.map((r, i) => (
            <div key={i} className="mb-4">
              <strong>{r.archivo1} comparado con {r.archivo2}:</strong>
              {Object.entries(r.resultado).map(([tipo, valor]) => (
                <pre key={tipo} className="whitespace-pre-wrap text-sm mt-1">
                  {tipo}: {valor}
                </pre>
              ))}
            </div>
          ))
        ) : (
          <p>No hay resultados para mostrar.</p>
        )}
      </div>
    </div>
  );
}
