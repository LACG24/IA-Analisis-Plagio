from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import torch
from backed import predecir_par
from werkzeug.utils import secure_filename


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/analizar', methods=['POST'])
def analizar():
    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    if not file1 or not file2:
        return jsonify({"error": "Faltan archivos"}), 400

    path1 = os.path.join(UPLOAD_FOLDER, secure_filename(file1.filename))
    path2 = os.path.join(UPLOAD_FOLDER, secure_filename(file2.filename))
    file1.save(path1)
    file2.save(path2)

    resultado = predecir_par(path1, path2)

    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

