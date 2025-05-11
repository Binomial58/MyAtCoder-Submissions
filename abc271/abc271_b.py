N,Q=map(int, input().split())
L=[]
W=[]
for i in range(N):
    l=list(map(int, input().split()))
    L.append(l[1:])
for i in range(Q):
    s,t=map(int, input().split())
    W.append(L[s-1][t-1])
for w in W:
    print(w)