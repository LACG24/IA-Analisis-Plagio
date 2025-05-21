def ida_star(start, goal, graph, h):
    bound = h[start]
    path = [start]

    def search(path, g, bound):
        node = path[-1]
        f = g + h[node]
        if f > bound:
            return f
        if node == goal:
            return "FOUND"
        min_bound = float('inf')
        for neighbor, cost in graph[node]:
            if neighbor not in path:
                path.append(neighbor)
                t = search(path, g + cost, bound)
                if t == "FOUND":
                    return "FOUND"
                if t < min_bound:
                    min_bound = t
                path.pop()
        return min_bound

    while True:
        t = search(path, 0, bound)
        if t == "FOUND":
            return path
        if t == float('inf'):
            return None
        bound = t
