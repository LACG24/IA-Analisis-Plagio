def greedy_manual(start, goal, graph, h):
    frontier = [(start, h[start])]
    came_from = {}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current, _ = frontier.pop(0)

        if current == goal:
            return reconstruct(came_from, current)

        for neighbor, _ in graph[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                frontier.append((neighbor, h[neighbor]))
    return None

def reconstruct(came_from, node):
    path = []
    while node in came_from:
        path.append(node)
        node = came_from[node]
    path.append(node)
    return path[::-1]
