import sys; input=sys.stdin.readline; out=[]
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
    d[a[j]^f].append(j)
  for j in range(q):
    k,l,r=map(int,input().split())
    l-=1
    t=divisors(k)
    ans=0
    while 1:
      y=(n,-1)
      for x in t:
        ind=bs(d[x^f],l)
        if ind<len(d[x^f]):
          y=min(y,(d[x^f][ind],x))
      if y[0]<r:
        ans+=k*(y[0]-l)
        while k%y[1]==0:
          k//=y[1]
        l=y[0]
        s=[]
        for x in t:
          if k%x==0:
            s.append(x)
        t=s
      else:
        ans+=k*(r-l)
        break
    out.append(ans)
print('\n'.join(map(str,out)))
