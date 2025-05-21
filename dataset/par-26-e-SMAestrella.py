import heapq

def reconstruir(nodo, padres):
    camino = []
    while nodo in padres:
        camino.append(nodo)
        nodo = padres[nodo]
    camino.append(nodo)
    return camino[::-1]

def sma_star_alt(inicio, objetivo, grafo, heuristica, limite):
    frontera = []
    g = {inicio: 0}
    padres = {}
    heapq.heappush(frontera, (heuristica[inicio], inicio))

    while frontera:
        if len(frontera) > limite:
            frontera.sort(reverse=True)
            frontera.pop()

        _, actual = heapq.heappop(frontera)

        if actual == objetivo:
            return reconstruir(actual, padres)

        for vecino, costo in grafo[actual]:
            nuevo_g = g[actual] + costo
            if vecino not in g or nuevo_g < g[vecino]:
                g[vecino] = nuevo_g
                padres[vecino] = actual
                f = nuevo_g + heuristica[vecino]
                heapq.heappush(frontera, (f, vecino))
    return None
