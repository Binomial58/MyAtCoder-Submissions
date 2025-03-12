N,K=map(int, input().split())
A=list(map(int, input().split()))
B=[]
if K>N:
    K=N
for i in range(N-K):
    B.append(A[K+i])
for _ in range(K):
    B.append(0)
print(*B)