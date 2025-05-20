
RAV = int(input())
 
while RAV > 0:
 RAV -= 1
 
 NAV = int(input())
 a = sorted(list(map(int,input().split(' '))))
 
 flg = False
 res = False
 i = j = 0
 while i < NAV and not res:
  while j < NAV and a[j] == a[i]:
   j += 1
 
  if j-i >= 4:
   res = True
  elif j-i >= 2:
   res = flg
   flg = True if j < NAV and a[i] == a[j] - 1 else flg
  else:
   flg = False if j < NAV and a[i] != a[j] - 1 else flg
 
  i = j
     
 if res:
  print("Yes")
 else:
  print("No")