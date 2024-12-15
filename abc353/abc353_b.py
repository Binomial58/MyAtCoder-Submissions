N,K=map(int, input().split())
A=list(map(int, input().split()))
R=K
C=0
for k in range(N):
    if A[k]<=R:
        R-=A[k]
    else:
        C+=1
        R=K
        R-=A[k]
C+=1
print(C)