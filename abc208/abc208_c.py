import copy
N,K=map(int, input().split())
A=list(map(int, input().split()))
B=copy.deepcopy(A)
B.sort()
C=K//N
K-=N*C
k=B[K-1]
for a in A:
    if a<=k and K!=0:
        print(C+1)
    else:
        print(C)