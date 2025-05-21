import sys

class Canvas:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        row = [0] * self.width
        self.grid = [row[:] for _ in range(self.height)]

    def apply_drop(self, drop):
        cx, cy, shape = drop
        if shape == 1:
            self.mark(cx, cy)
            self.mark(cx+1, cy)
            self.mark(cx-1, cy)
            self.mark(cx, cy+1)
            self.mark(cx, cy-1)
        elif shape == 2:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    self.mark(cx + dx, cy + dy)
        elif shape == 3:
            offsets = [
                (0, -2),
                (-1, -1), (0, -1), (1, -1),
                (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
                (-1, 1), (0, 1), (1, 1),
                (0, 2)
            ]
            for dx, dy in offsets:
                self.mark(cx + dx, cy + dy)

    def mark(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] += 1

    def show(self):
        for line in self.grid:
            print(line)

if __name__ == '__main__':
    drops = []
    for entry in sys.stdin:
        drops.append([int(v) for v in entry.strip().split(',')])

    canvas = Canvas()
    for d in drops:
        canvas.apply_drop(d)

    empty = 0
    max_val = 0
    for row in canvas.grid:
        empty += row.count(0)
        max_val = max(max(row), max_val)
    print(empty)
    print(max_val)
