N=int(input())
A=[list(map(int, input().split())) for _ in range(N)]
for k in range(N):
    B=[]
    for j in range(N):
        if A[k][j]==1:
            B.append(j+1)
    print(*B)