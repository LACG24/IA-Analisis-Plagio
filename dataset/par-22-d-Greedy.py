import heapq

def reconstruir(caminos, destino):
    resultado = []
    nodo = destino
    while nodo in caminos:
        resultado.append(nodo)
        nodo = caminos[nodo]
    resultado.append(nodo)
    return resultado[::-1]

def busqueda_greedy(inicio, objetivo, grafo, heuristica):
    abiertos = [(heuristica[inicio], inicio)]
    padres = {}

    while abiertos:
        _, actual = heapq.heappop(abiertos)
        if actual == objetivo:
            return reconstruir(padres, actual)

        for vecino, _ in grafo[actual]:
            if vecino not in padres:
                padres[vecino] = actual
                heapq.heappush(abiertos, (heuristica[vecino], vecino))
    return None
