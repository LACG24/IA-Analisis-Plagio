def es_valido(nx, ny, sistema, activo): 
    filas, columnas = len(sistema), len(sistema[0])
    return (
        0 <= nx < filas and
        0 <= ny < columnas and
        sistema[nx][ny] == 1 and
        not activo[nx][ny]
    )

def obtener_direcciones():
    # Devuelve los desplazamientos fila/columna para moverse en las 4 direcciones cardinales
    mov_filas = [-1, 1, 0, 0]   # arriba, abajo
    mov_columnas = [0, 0, -1, 1]  # izquierda, derecha
    return mov_filas, mov_columnas

def propagar_senal(sistema, inicio):
    filas, columnas = len(sistema), len(sistema[0])
    activo = [[False] * columnas for _ in range(filas)]
    cola = [inicio]
    activo[inicio[0]][inicio[1]] = True

    dx, dy = obtener_direcciones()

    while cola:
        x, y = cola[0]
        cola = cola[1:]
        print(f"Señal activa en nodo: ({x}, {y})")

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if es_valido(nx, ny, sistema, activo):
                activo[nx][ny] = True
                cola.append((nx, ny))

# Matriz que representa el sistema
sistema = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 1]
]

# Nodo de inicio de la señal
propagar_senal(sistema, (0, 0))
