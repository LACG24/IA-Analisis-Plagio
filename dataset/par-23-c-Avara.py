import heapq

def best_first_search(start, goal, graph, h):
    open_set = []
    heapq.heappush(open_set, (h[start], start))
    visited = set()
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)

        if current in visited:
            continue
        visited.add(current)

        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                came_from[neighbor] = current
                heapq.heappush(open_set, (h[neighbor], neighbor))
    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]
