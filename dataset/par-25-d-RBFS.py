import math

def busqueda_recursiva_mejor_primero(nodo, destino, grafo, heuristica, limite_f):
    if nodo == destino:
        return [nodo], 0

    hijos = [(vecino, costo + heuristica[vecino]) for vecino, costo in grafo[nodo]]

    if not hijos:
        return None, math.inf

    while True:
        hijos.sort(key=lambda x: x[1])
        mejor, f_mejor = hijos[0]

        if f_mejor > limite_f:
            return None, f_mejor

        alternativo = hijos[1][1] if len(hijos) > 1 else math.inf
        resultado, nuevo_f = busqueda_recursiva_mejor_primero(mejor, destino, grafo, heuristica, min(limite_f, alternativo))

        if resultado is not None:
            return [nodo] + resultado, nuevo_f

        hijos[0] = (mejor, nuevo_f)
