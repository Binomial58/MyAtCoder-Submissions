N,D,H=map(int, input().split())
G=[]
m=0
for i in range(N):
    d=list(map(int, input().split()))
    G.append(d)
for g in G:
    m=max(m,(H*g[0]-D*g[1])/(g[0]-D))
print(m)