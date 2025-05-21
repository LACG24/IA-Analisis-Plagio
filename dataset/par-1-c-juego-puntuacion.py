from collections import defaultdict
from itertools import product
from math import pi
import copy

row_vals, col_vals = None, None

def compute_score(grid):
    result = 0
    for i in range(3):
        for j in range(3):
            if i + 1 < 3 and grid[i][j] == grid[i + 1][j]:
                result += row_vals[i][j]
            if j + 1 < 3 and grid[i][j] == grid[i][j + 1]:
                result += col_vals[i][j]
    return result

memoization = {}

def freeze(grid):
    return tuple(grid[0]), tuple(grid[1]), tuple(grid[2])

def search(depth, grid):
    if depth >= 9:
        return compute_score(grid)

    if freeze(grid) in memoization:
        return memoization[freeze(grid)]

    player = depth % 2
    res = 0 if player == 0 else 10 ** 10

    for i in range(3):
        for j in range(3):
            if grid[i][j] is None:
                grid[i][j] = player
                temp_score = search(depth + 1, grid)
                grid[i][j] = None

                if player == 0 and temp_score > res:
                    res = temp_score
                if player == 1 and temp_score < res:
                    res = temp_score

    memoization[freeze(grid)] = res
    return res

def main():
    global row_vals, col_vals
    r1 = list(map(int, input().split()))
    r2 = list(map(int, input().split()))
    row_vals = [r1, r2]

    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))
    col_vals = [c1 + [0], c2 + [0], c3 + [0]]

    board = [[None] * 3 for _ in range(3)]
    score1 = search(0, board)
    full_score = sum([sum(x) for x in row_vals + col_vals])
    print(score1)
    print(full_score - score1)

if __name__ == '__main__':
    main()
