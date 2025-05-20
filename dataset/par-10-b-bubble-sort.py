def bubble_sort_verbose(arr):
    n = len(arr)
    swap_count = 0
    print("Arreglo original:", arr)
    for i in range(n):
        print(f"\nIteración {i + 1}:")
        for j in range(0, n - i - 1):
            print(f"  Comparando {arr[j]} y {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                print(f"  Intercambiando {arr[j]} y {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
            print("  Estado actual:", arr)
        print(f"Fin de iteración {i + 1}: {arr}")
    print("\nArreglo ordenado:", arr)
    print("Total de intercambios:", swap_count)
    return arr

def menu():
    print("Menú de prueba para Bubble Sort")
    print("1. Usar arreglo por defecto")
    print("2. Ingresar arreglo manualmente")
    eleccion = input("Seleccione una opción: ")
    if eleccion == "1":
        datos = [64, 34, 25, 12, 22, 11, 90, 55, 32, 78]
    elif eleccion == "2":
        entrada = input("Ingrese los números separados por espacios: ")
        datos = list(map(int, entrada.strip().split()))
    else:
        print("Opción no válida")
        return
    bubble_sort_verbose(datos)

if __name__ == "__main__":
    menu()