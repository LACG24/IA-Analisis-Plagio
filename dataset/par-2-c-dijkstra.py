x1, y1, x2, y2 = map(int, input().split())
n = int(input())
circles = [list(map(int, input().split())) for _ in range(n)]

class Dijkstra:
    def __init__(self, graph, src):
        self.start = src
        self.size = len(graph)
        self.dist = [float("inf")] * self.size
        self.dist[src] = 0
        self.prev = [0] * self.size
        self.prev[src] = -1
        unvisited = list(range(self.size))
        unvisited.remove(src)
        now = src
        while unvisited:
            next_node = 0
            next_dist = float("inf")
            for node in unvisited:
                total = graph[now][node] + self.dist[now]
                self.dist[node] = min(self.dist[node], total)
                if self.dist[node] <= next_dist:
                    next_dist = self.dist[node]
                    next_node = node
            unvisited.remove(next_node)
            self.prev[next_node] = now
            now = next_node

import math

def solve(x1, y1, x2, y2, n, circles):
    circles.insert(0, [x1, y1, 0])
    circles.append([x2, y2, 0])
    def dist(i, j):
        xi, yi, ri = circles[i]
        xj, yj, rj = circles[j]
        d = math.hypot(xi - xj, yi - yj) - ri - rj
        return max(d, 0)
    g = [[0]*(n+2) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            g[i][j] = g[j][i] if i > j else dist(i, j)
    d = Dijkstra(g, 0)
    return d.dist[-1]

print(solve(x1, y1, x2, y2, n, circles))
