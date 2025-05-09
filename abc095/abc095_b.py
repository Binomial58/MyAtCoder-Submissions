N,X=map(int, input().split())
M=[]
S=N
for _ in range(N):
    m=int(input())
    M.append(m)
    X-=m
print(S+X//min(M))