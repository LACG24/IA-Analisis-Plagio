import os
import json

def leer_codigo(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generar_dataset(pares_archivos, tipo_plagio_por_defecto="1", salida="dataset.json"):
    dataset = []
    
    for codigo_1_path, codigo_2_path in pares_archivos:
        codigo_1 = leer_codigo(codigo_1_path)
        codigo_2 = leer_codigo(codigo_2_path)

        entrada = {
            "codigo_1": codigo_1,
            "codigo_2": codigo_2,
            "tipo_plagio": tipo_plagio_por_defecto
        }
        dataset.append(entrada)

    with open(salida, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print(f"✅ Dataset guardado en '{salida}' con {len(dataset)} pares.")

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de tuplas con los archivos a comparar (en pares)
    pares = [
        ("dataset/par-6-a-min-area.py", "dataset/par-6-b-min-area.py"),
        ("dataset/par-7-a-grundy-numbers.py", "dataset/par-7-b-grundy-numbers.py"),
        ("dataset/par-8-a-knapsack-pesos.py", "dataset/par-8-b-knapsack-pesos.py")
        # Agrega más pares aquí
    ]
    
    generar_dataset(pares_archivos=pares)
