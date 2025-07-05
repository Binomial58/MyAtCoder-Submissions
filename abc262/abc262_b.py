N,M=map(int, input().split())
V=[[]*i for i in range(N)]
for i in range(M):
    u,v=map(int, input().split())
    V[v-1].append(u)
    V[u-1].append(v)
W=set()
c=0
for a in range(N):
    for b in range(N):
        if a==b:
            break
        for c in range(N):
            if b==c:
                break
            if b+1 in V[a] and c+1 in V[a]:
                if a+1 in V[b] and c+1 in V[b]:
                    if a+1 in V[c] and b+1 in V[c]:
                        R=[a,b,c]
                        R.sort()
                        s=str(R[0])+":"+str(R[1])+":"+str(R[2])
                        W.add(s)
print(len(W))