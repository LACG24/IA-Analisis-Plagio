import heapq

class Node:
    def __init__(self, state, g, h, parent=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
    def __lt__(self, other):
        return self.f < other.f

def sma_star(start, goal, graph, h, memory_limit):
    open_list = []
    heapq.heappush(open_list, Node(start, 0, h[start]))
    while open_list:
        if len(open_list) > memory_limit:
            open_list.pop()
        current = heapq.heappop(open_list)
        if current.state == goal:
            return reconstruct_path(current)
        for neighbor, cost in graph[current.state]:
            child = Node(neighbor, current.g + cost, h[neighbor], current)
            heapq.heappush(open_list, child)
    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path
