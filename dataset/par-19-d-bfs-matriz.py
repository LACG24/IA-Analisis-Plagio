from collections import deque

def propagar_virus(mapa, origen):
    filas, cols = len(mapa), len(mapa[0])
    marcados = [[False] * cols for _ in range(filas)]
    cola = deque([origen])
    marcados[origen[0]][origen[1]] = True

    movs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha, abajo, izquierda, arriba

    while cola:
        f, c = cola.popleft()
        print(f"Visitado: ({f}, {c})")

        for df, dc in movs:
            nf, nc = f + df, c + dc
            if 0 <= nf < filas and 0 <= nc < cols:
                if mapa[nf][nc] == 1 and not marcados[nf][nc]:
                    marcados[nf][nc] = True
                    cola.append((nf, nc))

# Datos de entrada
mapa = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 1]
]

propagar_virus(mapa, (0, 0))
