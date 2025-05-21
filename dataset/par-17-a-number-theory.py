from bisect import bisect
import sys
input = sys.stdin.readline
N = int(1e5) + 7
factors = [[] for _ in range(N)]
 
for i in range(1 , N):
    for j in range(i , N , i):
        factors[j].append(i)
pos = [[] for i in range(int(1e5) + 7)]
def solve():
    n , q = map(int, input().split())
    ls = list(map(int, input().split()))
    for i in range(n):
        pos[ls[i]].append(i)
    for _ in range(q):
        k , L , R = map(int, input().split())
        L -= 1 
        R -= 1 
        res = []
       
        for d in factors[k]:
            ind = bisect(pos[d] , L-1)
            if ind<len(pos[d]) and pos[d][ind] <= R :
                 res.append(pos[d][ind])
        res.sort()
        ans = 0
        last = L
        for i in res:
 
            ans+=(i-last)*k
            while not k%ls[i]:
                k//=ls[i]
            last=i
        if last<=R:
            ans+=(R-last+1)*k
        print(ans)
    for i in ls : 
        pos[i] = []
 
for _ in range(int(input())):
    solve()