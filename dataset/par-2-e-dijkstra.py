import math
import heapq

def dijkstra(start, adj):
    n = len(adj)
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, cost in adj[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                heapq.heappush(heap, (dist[v], v))
    return dist

def distance(p1, p2):
    x1, y1, r1 = p1
    x2, y2, r2 = p2
    d = math.hypot(x1 - x2, y1 - y2) - r1 - r2
    return max(d, 0)

def main():
    xs, ys, xt, yt = map(int, input().split())
    n = int(input())
    nodes = [tuple(map(int, input().split())) for _ in range(n)]
    nodes = [(xs, ys, 0)] + nodes + [(xt, yt, 0)]
    size = len(nodes)

    adj = [[] for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            d = distance(nodes[i], nodes[j])
            adj[i].append((j, d))
            adj[j].append((i, d))

    dist = dijkstra(0, adj)
    print(dist[-1])

main()
