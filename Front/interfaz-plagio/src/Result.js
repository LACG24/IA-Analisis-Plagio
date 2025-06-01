import React from 'react';
import './result.css';

export default function Results({ data }) {
  return (
    <div className="results-container">
      <h2>Contenido de Archivos</h2>
      <div className="code-list">
        {data.map((item, i) => (
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
    </div>
  );
}
