def a_star_custom(start, goal, graph, h):
    open_set = [(start, 0, h[start])]
    came_from = {}
    g_scores = {start: 0}

    while open_set:
        open_set.sort(key=lambda x: x[1] + x[2])
        current, g, _ = open_set.pop(0)

        if current == goal:
            return build_path(came_from, current)

        for neighbor, cost in graph[current]:
            tentative = g + cost
            if neighbor not in g_scores or tentative < g_scores[neighbor]:
                g_scores[neighbor] = tentative
                came_from[neighbor] = current
                open_set.append((neighbor, tentative, h[neighbor]))
    return None

def build_path(came_from, node):
    path = []
    while node in came_from:
        path.append(node)
        node = came_from[node]
    path.append(node)
    return path[::-1]
