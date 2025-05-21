import sys; input=sys.stdin.readline
from collections import defaultdict
from bisect import bisect_left as bs
from math import isqrt
from random import getrandbits
f=getrandbits(20)
def divisors(n):
  d=[]
  for j in range(1,isqrt(n)+1):
    if n%j==0:
      d.append(j)
      if n//j!=j:
        d.append(n//j)
  return d
for i in range(int(input())):
  n,q=map(int,input().split())
  a=list(map(int,input().split()))
  d=defaultdict(list)
  for j in range(n):
    d[a[j]^f].append(j+1)
  for j in range(q):
    k,l,r=map(int,input().split())
    t=divisors(k)
    p=set([l])
    for x in t:
      ind=bs(d[x^f],l)
      if ind<len(d[x^f]) and d[x^f][ind]<=r:
        p.add(d[x^f][ind])
    p=sorted(list(p))+[r+1]
    ans=0
    for x in range(1,len(p)):
      while k%a[p[x-1]-1]==0:
        k//=a[p[x-1]-1]
      ans+=k*(p[x]-p[x-1])
    print(ans)