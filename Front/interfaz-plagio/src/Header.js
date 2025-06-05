import React from 'react';
import "./index.css"

export default function Header({ onReset }) {
  return (
    <div className="header-container">
    <header className="bg-[#00334e] text-white px-6 py-4 flex justify-between items-center">
      <h1 className="text-2xl font-bold">Detector de Plagio</h1>
      <button onClick={onReset} className="btn btn-secondary">
        Nuevo intento
      </button>
    </header>
    </div>
  );
}
