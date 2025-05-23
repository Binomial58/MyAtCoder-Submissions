N,M=map(int, input().split())
P=[]
T=[[0*i for i in range(N)]for i in range(N)]
for j in range(N):
    T[j][j]=1
for i in range(M):
    K=list(map(int, input().split()))
    P.append(K[1:])
for p in P:
    for a in p:
        for b in p:
            T[a-1][b-1]+=1
for t in T:
    if 0 in t:
        print("No")
        exit()
print("Yes")