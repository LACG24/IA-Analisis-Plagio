import sys
from collections import defaultdict
from bisect import bisect_left
from math import isqrt
from random import getrandbits

input = sys.stdin.readline
RANDOM_MASK = getrandbits(20)

def obtener_divisores(valor):
    lista = []
    for i in range(1, isqrt(valor) + 1):
        if valor % i == 0:
            lista.append(i)
            if valor // i != i:
                lista.append(valor // i)
    return lista

casos = int(input())
for _ in range(casos):
    tamano, consultas = map(int, input().split())
    datos = list(map(int, input().split()))
    indices = defaultdict(list)
    
    for idx, num in enumerate(datos):
        indices[num ^ RANDOM_MASK].append(idx + 1)

    for _ in range(consultas):
        clave, izq, der = map(int, input().split())
        divisores = obtener_divisores(clave)
        puntos = set([izq])

        for d in divisores:
            lista = indices[d ^ RANDOM_MASK]
            pos = bisect_left(lista, izq)
            if pos < len(lista) and lista[pos] <= der:
                puntos.add(lista[pos])
        
        puntos = sorted(puntos) + [der + 1]
        resultado = 0

        for i in range(1, len(puntos)):
            actual = puntos[i - 1]
            while clave % datos[actual - 1] == 0:
                clave //= datos[actual - 1]
            resultado += clave * (puntos[i] - actual)

        print(resultado)
