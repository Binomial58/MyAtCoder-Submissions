N,H,X=map(int, input().split())
P=list(map(int, input().split()))
D=[a for a in P if a>=X-H]
m=min(D)
print(P.index(m)+1)