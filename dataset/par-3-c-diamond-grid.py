import math
H, W, R = map(int, input().split())
grid = [[0 if ch == "x" else 1 for ch in input()] for _ in range(H)]

for col in range(W):
    start = 0
    for row in range(H + 1):
        if row == H or grid[row][col] == 0:
            for i in range(math.ceil((row - start) / 2)):
                grid[start + i][col] = i + 1
                grid[row - i - 1][col] = i + 1
            start = row + 1

total = 0
D = (R - 1) * 2 + 1
for row in range(R - 1, H - R + 1):
    left = 0
    zeros = grid[row].count(0)
    for i in range(zeros + 1):
        right = grid[row].index(0, left) if i < zeros else W - 1
        width = right - left + 1
        if width < D:
            left = right + 1
            continue
        check = 0
        for j in range(width - D + 1):
            check = max(0, check - 1)
            l, r = left + j, left + j + D - 1
            valid = True
            high = True
            for k in range(check, D):
                h = k + 1 if k < R else 2 * R - k - 1
                val = grid[row][l + k]
                if val < h:
                    valid = False
                    break
                elif k <= R - 1 or (high and val >= R):
                    check = k
                else:
                    high = False
            if valid:
                total += 1
            else:
                check = 0
        left = right + 1

print(total)
