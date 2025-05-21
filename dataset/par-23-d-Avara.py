import heapq

def reconstruir_camino(padres, objetivo):
    camino = []
    while objetivo in padres:
        camino.append(objetivo)
        objetivo = padres[objetivo]
    camino.append(objetivo)
    return camino[::-1]

def busqueda_avara(inicio, meta, grafo, heuristica):
    frontera = [(heuristica[inicio], inicio)]
    explorados = set()
    padres = {}

    while frontera:
        _, actual = heapq.heappop(frontera)

        if actual in explorados:
            continue
        explorados.add(actual)

        if actual == meta:
            return reconstruir_camino(padres, actual)

        for vecino, _ in grafo[actual]:
            if vecino not in explorados:
                padres[vecino] = actual
                heapq.heappush(frontera, (heuristica[vecino], vecino))
    return None
