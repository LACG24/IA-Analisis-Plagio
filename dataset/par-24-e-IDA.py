def ida_star_alt(start, goal, graph, h):
    def dfs(node, g, bound, visited):
        f = g + h[node]
        if f > bound:
            return None, f
        if node == goal:
            return [node], f
        min_threshold = float('inf')
        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                result, t = dfs(neighbor, g + cost, bound, visited)
                visited.remove(neighbor)
                if result:
                    return [node] + result, t
                if t < min_threshold:
                    min_threshold = t
        return None, min_threshold

    threshold = h[start]
    while True:
        visited = set([start])
        result, new_threshold = dfs(start, 0, threshold, visited)
        if result:
            return result
        if new_threshold == float('inf'):
            return None
        threshold = new_threshold
