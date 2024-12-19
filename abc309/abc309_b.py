import copy
N=int(input())
A=[]
for i in range(N):
    A.append(list(input()))
B=copy.deepcopy(A)
for a in range(N-1):
    B[0][a+1]=A[0][a]
for b in range(N-1):
    B[b+1][N-1]=A[b][N-1]
for c in range(N-1):
    B[N-1][c]=A[N-1][c+1]
for d in range(N-1):
    B[d][0]=A[d+1][0]
for r in range(N):
    V=""
    for q in range(N):
       V+=B[r][q]
    print(V)