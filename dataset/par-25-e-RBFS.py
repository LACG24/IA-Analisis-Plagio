import math

class Nodo:
    def __init__(self, estado, g, h, padre=None):
        self.estado = estado
        self.g = g
        self.h = h
        self.f = g + h
        self.padre = padre

def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return camino[::-1]

def rbfs_alt(nodo, meta, grafo, limite_f):
    if nodo.estado == meta:
        return reconstruir_camino(nodo), nodo.f

    sucesores = []
    for vecino, costo in grafo[nodo.estado]:
        hijo = Nodo(vecino, nodo.g + costo, h[vecino], nodo)
        sucesores.append(hijo)

    if not sucesores:
        return None, math.inf

    while True:
        sucesores.sort(key=lambda n: n.f)
        mejor = sucesores[0]

        if mejor.f > limite_f:
            return None, mejor.f

        alternativo = sucesores[1].f if len(sucesores) > 1 else math.inf
        resultado, nuevo_f = rbfs_alt(mejor, meta, grafo, min(limite_f, alternativo))
        if resultado:
            return resultado, nuevo_f
        mejor.f = nuevo_f
