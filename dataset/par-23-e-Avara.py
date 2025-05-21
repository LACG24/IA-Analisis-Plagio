def best_first_manual(start, goal, graph, h):
    frontier = [(start, h[start])]
    came_from = {}
    explored = set()

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current, _ = frontier.pop(0)

        if current in explored:
            continue
        explored.add(current)

        if current == goal:
            return build(came_from, current)

        for neighbor, _ in graph[current]:
            if neighbor not in explored:
                came_from[neighbor] = current
                frontier.append((neighbor, h[neighbor]))
    return None

def build(path_map, node):
    path = []
    while node in path_map:
        path.append(node)
        node = path_map[node]
    path.append(node)
    return path[::-1]
