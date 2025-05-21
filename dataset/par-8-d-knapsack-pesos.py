N = int(input())
P_list = list(map(int, input().split()))
X_list = list(map(int, input().split()))

child_list = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    child_list[P_list[i - 2]].append(i)

color1 = [0] + X_list
color2 = [0] * (N + 1)

def solve_knapsack(L, M):
    min_sum = sum(min(color1[j], color2[j]) for j in L)
    if min_sum > M:
        return -1
    extra = M - min_sum
    possible = set([0])
    for j in L:
        diff = abs(color1[j] - color2[j])
        updated = set(possible)
        for s in possible:
            if s + diff <= extra:
                updated.add(s + diff)
        possible = updated
    total = sum(color1[j] + color2[j] for j in L)
    return total - max(possible) - min_sum

res = "POSSIBLE"

for i in range(N, 0, -1):
    if not child_list[i]:
        continue
    elif len(child_list[i]) == 1:
        j = child_list[i][0]
        if min(color1[j], color2[j]) > X_list[i - 1]:
            res = "IMPOSSIBLE"
            break
        elif max(color1[j], color2[j]) > X_list[i - 1]:
            color2[i] = max(color1[j], color2[j])
        else:
            color2[i] = min(color1[j], color2[j])
    else:
        c2 = solve_knapsack(child_list[i], X_list[i - 1])
        if c2 < 0:
            res = "IMPOSSIBLE"
            break
        color2[i] = c2

print(res)
