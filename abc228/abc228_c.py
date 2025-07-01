import bisect
N,K=map(int, input().split())
P=[]
V=[i for i in range(N)]
for i in range(N):
    p=list(map(int, input().split()))
    P.append(sum(p))
P,V=zip(*sorted(zip(P, V),reverse=True))
k=P[K-1]
P,V=zip(*sorted(zip(P, V)))
a=bisect.bisect(P,k-301)
R=["No" for i in range(a)]
for i in range(N-a):
    R.append("Yes")
V,R=zip(*sorted(zip(V, R)))
for r in R:
    print(r)