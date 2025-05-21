def procesar_texto(nombre):
    try:
        with open(nombre, encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except:
        print("Error al leer archivo.")
        return

    estadisticas = {
        "lineas": len(lineas),
        "palabras": 0,
        "letras": 0,
        "unicas": set()
    }

    for linea in lineas:
        tokens = linea.split()
        estadisticas["palabras"] += len(tokens)
        estadisticas["letras"] += sum(len(p) for p in tokens)
        estadisticas["unicas"].update(tokens)

    print(f"Archivo: {nombre}")
    print("Líneas:", estadisticas["lineas"])
    print("Palabras:", estadisticas["palabras"])
    print("Letras:", estadisticas["letras"])
    print("Distintas:", len(estadisticas["unicas"]))

def main_analizador():
    while True:
        nombre = input("Archivo: ")
        procesar_texto(nombre)
        if input("¿Analizar otro? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    main_analizador()
