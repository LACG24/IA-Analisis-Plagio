def solve():
  from collections import deque
  from heapq import heappush, heappop
  from math import inf, ceil 
  
  n = int(input())
  edges = []
  for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))
    
  nodes = [0] * (n + 1)
  print('? 1 1 1', flush=True)
  a = int(input())
  if a == 1 or a == -1:
    nodes[1] = a
    for i in range(2, n + 1):
      print(f'? 1 1 {i}', flush=True)
      nodes[i] = int(input()) - a
    
    print('!', *nodes[1:])
    return
  
  if a == 0:
    for i in range(2, n + 1):
      print(f'? 1 1 {i}', flush=True)
      nodes[i] = int(input())
    
    print(f'? 2 1', flush=True)
    print('? 1 1 1', flush=True)
    a = int(input())
    nodes[1] = 1 if a == 2 else -1
    print('!', *nodes[1:])
    return
  
  if a == 2 or a == -2:
    nodes[1] = -1 if a == 2 else 1
    print(f'? 2 1', flush=True)
    for i in range(2, n + 1):
      print(f'? 1 1 {i}', flush=True)
      nodes[i] = int(input())
    
    print('!', *nodes[1:])
    
    
  
  

    
if __name__ == '__main__':
  t = int(input())
  for _ in range(t):
    solve()