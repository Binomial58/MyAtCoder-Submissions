N,K=map(int, input().split())
A=list(map(int, input().split()))
R=[i for i in range(1,N+1)]
V=[]
c=0
i=0
while c!=N:
    while True:
        if R[i] in A and R[i+1] not in V:
            i+=1
        else:
            break
    if R[i] not in V:
        V.append(R[i])
        c+=1
        i-=1
        if i<0 or R[i] in V:
            i=max(V)
print(*V)