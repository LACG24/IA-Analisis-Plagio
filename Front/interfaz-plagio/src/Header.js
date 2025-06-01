import React from 'react';

export default function Header({ onReset }) {
  return (
    <header className="bg-[#00334e] text-white px-6 py-4 flex justify-between items-center">
      <h1 className="text-2xl font-bold">Detector de Plagio</h1>
      <button onClick={onReset} className="bg-gray-200 text-black rounded px-3 py-1 text-sm hover:bg-white">
        Nuevo intento
      </button>
    </header>
  );
}
