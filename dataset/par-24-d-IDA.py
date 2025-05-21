def ida_estrella(inicio, meta, grafo, heuristica):
    limite = heuristica[inicio]
    recorrido = [inicio]

    def expandir(ruta, costo, limite):
        actual = ruta[-1]
        f = costo + heuristica[actual]
        if f > limite:
            return f
        if actual == meta:
            return "ENCONTRADO"
        min_prox = float('inf')
        for vecino, peso in grafo[actual]:
            if vecino not in ruta:
                ruta.append(vecino)
                resultado = expandir(ruta, costo + peso, limite)
                if resultado == "ENCONTRADO":
                    return "ENCONTRADO"
                if resultado < min_prox:
                    min_prox = resultado
                ruta.pop()
        return min_prox

    while True:
        resultado = expandir(recorrido, 0, limite)
        if resultado == "ENCONTRADO":
            return recorrido
        if resultado == float('inf'):
            return None
        limite = resultado
