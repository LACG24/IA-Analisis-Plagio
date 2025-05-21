from collections import deque

def recorrer_matriz(matriz, punto_inicial):
    n_filas, n_columnas = len(matriz), len(matriz[0])
    fue_visitado = [[False] * n_columnas for _ in range(n_filas)]
    cola = deque([punto_inicial])
    fue_visitado[punto_inicial[0]][punto_inicial[1]] = True

    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izq, der

    while cola:
        fila, columna = cola.popleft()
        print("Posición actual:", fila, columna)

        for dy, dx in movimientos:
            sig_fila, sig_col = fila + dy, columna + dx

            if 0 <= sig_fila < n_filas and 0 <= sig_col < n_columnas:
                if matriz[sig_fila][sig_col] == 1 and not fue_visitado[sig_fila][sig_col]:
                    fue_visitado[sig_fila][sig_col] = True
                    cola.append((sig_fila, sig_col))

# Ejemplo
matriz = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 1]
]

recorrer_matriz(matriz, (0, 0))
