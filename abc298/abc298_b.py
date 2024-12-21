import copy
N=int(input())
A=[list(map(int, input().split()))for _ in range(N)]
B=[list(map(int, input().split()))for _ in range(N)]
C=copy.deepcopy(A)
for k in range(4):
    for i in range(N):
        for j in range(N):
            C[i][j]=A[N-1-j][i]
    count=0
    for i in range(N):
        for j in range(N):
            if C[i][j]==1 and B[i][j]!=1:
                count+=1
    if count==0:
        print("Yes")
        exit()
    A=copy.deepcopy(C)
print("No")