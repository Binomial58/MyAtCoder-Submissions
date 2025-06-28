N,M=map(int, input().split())
V=[]
for i in range(M):
    v=list(map(int, input().split()))
    V+=v
for j in range(1,N+1):
    print(V.count(j))