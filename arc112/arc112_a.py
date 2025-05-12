T=int(input())
C=[]
for i in range(T):
    L,R=map(int, input().split())
    if (L!=0 and R!=0) and L==R:
        C.append(0)
    else:
        n=R-2*L+1
        if n<=0:
            C.append(0)
        else:
            C.append(int(0.5*n*(n+1)))
for c in C:
    print(c)