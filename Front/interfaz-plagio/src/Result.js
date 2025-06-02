import React from 'react';
import './result.css';

export default function Results({ archivos, resultado }) {
  if (!archivos || archivos.length === 0) {
    return <div>No hay archivos para mostrar.</div>;
  }
  return (
    <div className="results-container">
      <h2>Contenido de Archivos</h2>

      {/* Mostrar el contenido de cada archivo */}
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

      {/* Mostrar el resultado del análisis */}
      <h2 className="mt-6">Resultado del análisis</h2>
      <div className="result-box">
        {resultado.split('\n').map((line, i) => (
          <p key={i}>{line}</p>
        ))}
      </div>
    </div>
  );
}
