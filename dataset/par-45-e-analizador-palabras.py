def analizar_archivo_linea_a_linea(ruta):
    total_lineas = 0
    total_palabras = 0
    total_letras = 0
    vocabulario = set()

    try:
        with open(ruta, encoding="utf-8") as archivo:
            for linea in archivo:
                total_lineas += 1
                palabras = linea.strip().split()
                total_palabras += len(palabras)
                total_letras += sum(len(p) for p in palabras)
                vocabulario.update(palabras)
    except:
        print("No se pudo leer el archivo.")
        return

    print(f"Archivo: {ruta}")
    print("Líneas:", total_lineas)
    print("Palabras:", total_palabras)
    print("Letras:", total_letras)
    print("Únicas:", len(vocabulario))

def main():
    while True:
        nombre = input("Archivo a procesar: ")
        analizar_archivo_linea_a_linea(nombre)
        if input("¿Procesar otro? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    main()
