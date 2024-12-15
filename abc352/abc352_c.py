N=int(input())
L=[list(map(int, input().split()))for _ in range(N)]
S=0
D=[L[i][1]-L[i][0] for i in range(N)]
M=D.index(max(D))
for k in range(N):
    if k !=M:
        S+=L[k][0]
    else:
        S+=L[k][1]
print(S)