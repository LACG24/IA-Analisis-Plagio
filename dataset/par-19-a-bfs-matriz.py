from collections import deque

def bfs(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    # Direcciones: arriba, abajo, izquierda, derecha
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        x, y = queue.popleft()
        print(f"Visitando: ({x}, {y})")

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:  # dentro de la matriz
                if not visited[nx][ny] and grid[nx][ny] == 1:  # celda válida
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# Ejemplo de uso
grid = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 1]
]

start = (0, 0)  # Comenzamos desde la esquina superior izquierda
bfs(grid, start)
