import heapq

class Nodo:
    def __init__(self, estado, costo, heuristica, padre=None):
        self.estado = estado
        self.g = costo
        self.h = heuristica
        self.f = self.g + self.h
        self.padre = padre
    def __lt__(self, otro):
        return self.f < otro.f

def reconstruir_camino(nodo_final):
    resultado = []
    actual = nodo_final
    while actual:
        resultado.append(actual.estado)
        actual = actual.padre
    return resultado[::-1]

def busqueda_sma(inicio, meta, grafo, h, limite_memoria):
    frontera = []
    heapq.heappush(frontera, Nodo(inicio, 0, h[inicio]))

    while frontera:
        if len(frontera) > limite_memoria:
            frontera.pop()

        actual = heapq.heappop(frontera)

        if actual.estado == meta:
            return reconstruir_camino(actual)

        for vecino, costo in grafo[actual.estado]:
            hijo = Nodo(vecino, actual.g + costo, h[vecino], actual)
            heapq.heappush(frontera, hijo)

    return None
