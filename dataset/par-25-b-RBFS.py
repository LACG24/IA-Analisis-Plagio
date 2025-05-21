import math

def rbfs(node, goal, graph, h, f_limit):
    if node == goal:
        return [node], 0
    successors = []
    for neighbor, cost in graph[node]:
        successors.append((neighbor, cost + h[neighbor]))
    if not successors:
        return None, math.inf
    while True:
        successors.sort(key=lambda x: x[1])
        best, best_f = successors[0]
        if best_f > f_limit:
            return None, best_f
        alternative = successors[1][1] if len(successors) > 1 else math.inf
        result, new_f = rbfs(best, goal, graph, h, min(f_limit, alternative))
        if result is not None:
            return [node] + result, new_f
        successors[0] = (best, new_f)
