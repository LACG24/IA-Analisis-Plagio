from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import torch
from itertools import combinations
from werkzeug.utils import secure_filename
from backed import predecir_par
from modelo import comparar_funciones_combinado


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/analizar', methods=['POST'])
def analizar():
    archivos = request.files.getlist("files")

    if len(archivos) < 2:
        return jsonify({"error": "Se requieren al menos dos archivos"}), 400

    # Guardar todos los archivos
    rutas = []
    nombres = []
    for archivo in archivos:
        nombre = secure_filename(archivo.filename)
        ruta = os.path.join(UPLOAD_FOLDER, nombre)
        archivo.save(ruta)
        rutas.append(ruta)
        nombres.append(nombre)

    # Comparar cada par
    resultados = []
    for (ruta1, ruta2), (nombre1, nombre2) in zip(combinations(rutas, 2), combinations(nombres, 2)):
        resultado = predecir_par(ruta1, ruta2)
        resultados.append({
            "archivo1": nombre1,
            "archivo2": nombre2,
            "resultado": resultado
        })

    for ruta in rutas:
        if os.path.exists(ruta):
            os.remove(ruta)
        else:
            print(f"⚠️ Archivo no encontrado (ya eliminado?): {ruta}")

    # Unir todos los resultados en un solo string legible
    resumen = "\n".join(
        f"{r['archivo1']} vs {r['archivo2']} → {r['resultado']}"
        for r in resultados
    )
    print("resumen", resumen)
    return jsonify({"resultado": resultados})

@app.route('/comparar_similitud', methods=['POST'])
def comparar_similitud():
    archivos = request.files.getlist("files")

    if len(archivos) != 2:
        return jsonify({"error": "Debes subir exactamente dos archivos"}), 400

    # Guardar archivos temporalmente
    rutas = []
    for archivo in archivos:
        nombre = secure_filename(archivo.filename)
        ruta = os.path.join(UPLOAD_FOLDER, nombre)
        archivo.save(ruta)
        rutas.append(ruta)

    # Ejecutar comparación
    similitudes = comparar_funciones_combinado(rutas[0], rutas[1])

    # Borrar archivos temporales
    for ruta in rutas:
        os.remove(ruta)

    return jsonify({"similitudes_altas": similitudes})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

