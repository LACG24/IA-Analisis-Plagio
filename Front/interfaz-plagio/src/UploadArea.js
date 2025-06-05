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
        <div className="upload-wrapper">
        {showLabel && (<label className="upload-wrapper">
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
      <div className="upload-wrapper">
        <button
          onClick={() => setShowLabel(true)}
          className="btn-upload"
        >
          <Plus size={48} />
        </button>
        </div>
      <button onClick={onAnalyze} className="btn-analizar">
        Analizar
      </button>
      </div>
    </div>
  );
}
