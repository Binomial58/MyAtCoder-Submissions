N,M,Q=map(int, input().split())
S=[]
T=[]
for _ in range(N):
    s={0}
    S.append(s)
for q in range(Q):
    k=list(map(int, input().split()))
    if k[0]==1 and -1 not in S[k[1]-1]:
        S[k[1]-1].add(k[2])
    elif k[0]==2:
        S[k[1]-1]={-1}
    elif k[0]==3:
        if k[2]in S[k[1]-1] or S[k[1]-1]=={-1}:
            T.append("Yes")
        else:
            T.append("No")
for t in T:
    print(t)