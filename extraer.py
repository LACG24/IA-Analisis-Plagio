import os
import csv

ruta_dataset = 'Dataset_1'  # Cambia esto si tu carpeta tiene otro nombre
archivo_csv = 'pares1.csv'
pares = []

for carpeta_tarea in os.listdir(ruta_dataset):
    ruta_tarea = os.path.join(ruta_dataset, carpeta_tarea)
    if not os.path.isdir(ruta_tarea):
        continue

    ruta_original = os.path.join(ruta_tarea, 'original')
    if not os.path.exists(ruta_original):
        continue

    # 1. Mapeamos los archivos originales por nombre base completo
    mapa_originales = {}
    for archivo in os.listdir(ruta_original):
        if archivo.endswith('.py'):
            base = archivo.replace('.py', '')  # ← conserva nombres como decimal_converter_1
            ruta_rel = os.path.join(ruta_tarea, 'original', archivo).replace('\\', '/')
            mapa_originales[base] = ruta_rel

    # 2. Buscamos plagios por tipo
    for tipo in ['1', '2', '3']:
        ruta_tipo = os.path.join(ruta_tarea, f'tipo{tipo}')
        if not os.path.exists(ruta_tipo):
            continue

        for archivo_plagio in os.listdir(ruta_tipo):
            if archivo_plagio.endswith(f'_tipo{tipo}.py'):
                base = archivo_plagio.replace(f'_tipo{tipo}.py', '')
                ruta_plagio = os.path.join(ruta_tarea, f'tipo{tipo}', archivo_plagio).replace('\\', '/')

                if base in mapa_originales:
                    ruta_original = mapa_originales[base]
                    pares.append([ruta_original, ruta_plagio, tipo])
                else:
                    print(f'⚠️ No se encontró original para: {archivo_plagio} (base: {base})')

# Guardar como CSV
with open(archivo_csv, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['archivo_original', 'archivo_plagiado', 'tipo_plagio'])
    writer.writerows(pares)

print(f'✅ CSV generado con {len(pares)} pares en {archivo_csv}')
