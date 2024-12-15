N,K=map(int, input().split())
A=list(map(int, input().split()))
B=[]
for k in range(N):
    if A[k]%K==0:
        B.append(A[k]//K)
print(*B)