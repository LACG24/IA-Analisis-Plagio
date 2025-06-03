import React from 'react';
import './result.css';

export default function Results({ archivos, resultado }) {
  if (!archivos || archivos.length === 0) {
    return <div>No hay archivos para mostrar.</div>;
  }

  return (
    <div className="results-container">
      <h2>Contenido de Archivos</h2>

      <div className="code-list">
        {archivos.map((item, i) => (
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

      <h2 className="mt-6">Resultado del análisis</h2>
      <div className="result-box">
      {Array.isArray(resultado) ? (
        resultado.map((r, i) => (
          <div key={i} className="mb-4">
            <strong>{r.archivo1} vs {r.archivo2}:</strong>
            <pre className="whitespace-pre-wrap text-sm mt-1">
              {r.resultado}
            </pre>
          </div>
        ))
      ) : (
        <p>No hay resultados para mostrar.</p>
      )}
    </div>
    </div>
  );
}
