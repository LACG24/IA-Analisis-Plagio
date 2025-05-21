import sys
from bisect import bisect_left

input = sys.stdin.readline

MAX = 10**5 + 10
divisores = [[] for _ in range(MAX)]

# Preprocesar todos los divisores
for i in range(1, MAX):
    for j in range(i, MAX, i):
        divisores[j].append(i)

ubicaciones = [[] for _ in range(MAX)]

def procesar_consulta():
    tam, consultas = map(int, input().split())
    arreglo = list(map(int, input().split()))

    for idx, valor in enumerate(arreglo):
        ubicaciones[valor].append(idx)

    for _ in range(consultas):
        clave, izq, der = map(int, input().split())
        izq -= 1
        der -= 1
        puntos = []

        for d in divisores[clave]:
            posicion = bisect_left(ubicaciones[d], izq - 1)
            if posicion < len(ubicaciones[d]) and ubicaciones[d][posicion] <= der:
                puntos.append(ubicaciones[d][posicion])

        puntos.sort()
        respuesta = 0
        previo = izq

        for pos in puntos:
            respuesta += (pos - previo) * clave
            while clave % arreglo[pos] == 0:
                clave //= arreglo[pos]
            previo = pos

        if previo <= der:
            respuesta += (der - previo + 1) * clave

        print(respuesta)

    # Limpiar datos para la siguiente consulta
    for valor in arreglo:
        ubicaciones[valor].clear()

# Casos de prueba
for _ in range(int(input())):
    procesar_consulta()
