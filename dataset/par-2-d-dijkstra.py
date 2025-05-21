import math

class Dijkstra:
    def __init__(self, matrix, source):
        self.n = len(matrix)
        self.dist = [float('inf')] * self.n
        self.dist[source] = 0
        self.prev = [-1] * self.n
        visited = [False] * self.n
        for _ in range(self.n):
            u = -1
            for v in range(self.n):
                if not visited[v] and (u == -1 or self.dist[v] < self.dist[u]):
                    u = v
            visited[u] = True
            for v in range(self.n):
                self.dist[v] = min(self.dist[v], self.dist[u] + matrix[u][v])

def compute_path(x_start, y_start, x_end, y_end, points):
    points = [[x_start, y_start, 0]] + points + [[x_end, y_end, 0]]
    size = len(points)

    def euclidean(i, j):
        xi, yi, ri = points[i]
        xj, yj, rj = points[j]
        d = math.hypot(xi - xj, yi - yj) - ri - rj
        return max(0, d)

    graph = [[euclidean(i, j) for j in range(size)] for i in range(size)]
    dijkstra = Dijkstra(graph, 0)
    return dijkstra.dist[-1]

# Input
x_s, y_s, x_t, y_t = map(int, input().split())
n_circles = int(input())
data = [list(map(int, input().split())) for _ in range(n_circles)]
print(compute_path(x_s, y_s, x_t, y_t, data))
