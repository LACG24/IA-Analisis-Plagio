def evaluate(board):
    res = 0
    for y in range(3):
        for x in range(3):
            if y < 2 and board[y][x] == board[y + 1][x]:
                res += B[y][x]
            if x < 2 and board[y][x] == board[y][x + 1]:
                res += C[y][x]
    return res

def flatten(board):
    return tuple(map(tuple, board))

def play(turn, board):
    if turn == 9:
        return evaluate(board)
    if flatten(board) in memo:
        return memo[flatten(board)]

    player = turn % 2
    best = -float('inf') if player == 0 else float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = player
                val = play(turn + 1, board)
                board[i][j] = None
                if player == 0:
                    best = max(best, val)
                else:
                    best = min(best, val)
    memo[flatten(board)] = best
    return best

# Input
B = [list(map(int, input().split())) for _ in range(2)]
C = [list(map(int, input().split())) + [0] for _ in range(3)]
total_score = sum(sum(row) for row in B + C)

memo = {}
initial = [[None]*3 for _ in range(3)]
score = play(0, initial)

print(score)
print(total_score - score)
