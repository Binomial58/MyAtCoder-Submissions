N,P,Q,R,S=map(int, input().split())
A=list(map(int, input().split()))
M=Q-P+1
for i in range(M):
    A[P-1+i],A[R-1+i]=A[R-1+i],A[P-1+i]
print(*A)