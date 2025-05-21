import heapq

def reconstruir_camino(origenes, nodo):
    camino = []
    while nodo in origenes:
        camino.append(nodo)
        nodo = origenes[nodo]
    camino.append(nodo)
    return camino[::-1]

def busqueda_a_estrella(inicio, meta, grafo, heuristica):
    abiertos = [(heuristica[inicio], 0, inicio)]
    padre = {}
    costo_acumulado = {inicio: 0}

    while abiertos:
        _, actual_g, actual = heapq.heappop(abiertos)

        if actual == meta:
            return reconstruir_camino(padre, actual)

        for vecino, costo in grafo[actual]:
            nuevo_g = actual_g + costo
            if vecino not in costo_acumulado or nuevo_g < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_g
                f = nuevo_g + heuristica[vecino]
                heapq.heappush(abiertos, (f, nuevo_g, vecino))
                padre[vecino] = actual
    return None
