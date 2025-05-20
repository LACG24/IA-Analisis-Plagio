t = int(input())
 
while t > 0:
 t -= 1
 
 n = int(input())
 a = sorted(list(map(int,input().split(' '))))
 
 flag = False
 res = False
 i = j = 0
 while i < n and not res:
  while j < n and a[j] == a[i]:
   j += 1
 
  if j-i >= 4:
   res = True
  elif j-i >= 2:
   res = flag
   flag = True if j < n and a[i] == a[j] - 1 else flag
  else:
   flag = False if j < n and a[i] != a[j] - 1 else flag
 
  i = j
     
 if res:
  print("Yes")
 else:
  print("No")