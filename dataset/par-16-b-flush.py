n=int(input(''))
for i in range(n):
    k=int(input(''))
    for i in range(k-1):
        l=[int(x) for x in input().split()]
    print("? 1 1 1",flush=True)
    f=int(input(''))
    ans=[]
    if f==1 or f==-1:
        ans.append(f)
        for i in range(2,k+1):
            print("? 1 1 ",i,flush=True)
            x=int(input(''))
            ans.append(x-f)
    else:
        if f==0:
            print("? 2 1",flush=True)
            print("? 1 1 1",flush=True)
            x=int(input(''))
            ans.append(-1*x//2)
            print("? 2 1",flush=True)
            for i in range(2,k+1):
                print(f"? 1 1 {i}",flush=True)
                x=int(input(''))
                ans.append(x)
        else:
            ans.append(f//2)
            print("? 2 1",flush=True)
            for i in range(2,k+1):
             print(f"? 1 1 {i}",flush=True)
             x=int(input(''))
             ans.append(x)
            print("? 2 1",flush=True)
    print("!",end=' ',flush=True)
    for i in ans:
        print(i,end=' ',flush=True)
    print('',flush=True)


