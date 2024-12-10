N,K,X=map(int, input().split())
A=list(map(int, input().split()))
B=[]
for i in range(K):
    B.append(A[i])
B.append(X)
for k in range(K,N):
    B.append(A[k])
print(*B)