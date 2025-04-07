N=int(input())
P=list(map(int, input().split()))
T=set(P)
A=[1]*N
for i in range(len(T)):
    c=0
    M=max(P)
    for j in range(N):
        if P[j]!=M and P[j]!=-1:
            A[j]+=1
        elif P[j]!=-1:
            P[j]=-1
            c+=1
    if c!=1:
        for k in range(N):
            if P[k]!=-1:
                A[k]=A[k]+c-1
for a in A:
    print(a)