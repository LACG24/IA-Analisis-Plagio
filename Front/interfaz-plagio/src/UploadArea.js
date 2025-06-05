import React from 'react';
import './index.js'
import { FileText, Plus } from 'lucide-react';
import { useState, useRef } from 'react';

export default function UploadArea({ files, onChange, onAnalyze }) {
    const fileInputRef = useRef(null);
    const [showLabel, setShowLabel] = useState(false);
  const handleFileChange = (e) => {
    const selectedFiles = Array.from(e.target.files);
    onChange((prevFiles) => [...prevFiles, ...selectedFiles]);

    if (fileInputRef.current) {
      fileInputRef.current.value = null;
    }
    setShowLabel(false);
  };  
    return (
    <div className="flex flex-col items-center gap-6 mt-10">
      <div className="flex gap-8">
        {files.map((file, i) => (
          <div key={i} className="flex flex-col items-center text-center">
            <FileText size={48} />
            <p className="mt-2 text-sm">{file.name}</p>
          </div>
        ))}
        <div className="flex gap-4 mt-4">
        <button
          onClick={() => setShowLabel(true)}
          className="flex flex-col items-center text-center hover:scale-105"
        >
          <Plus size={48} />
        </button>
        {showLabel && (<label className="cursor-pointer bg-gray-100 hover:bg-gray-200 px-4 py-2 rounded text-sm shadow">
        Subir archivos
        <input
          type="file"
          accept=".py"
          multiple
          onChange={handleFileChange}
          className="hidden"
        />
      </label>
        )}
      </div>
      <button onClick={onAnalyze} className="btn btn-primary">
        Analizar
      </button>
      </div>
    </div>
  );
}
