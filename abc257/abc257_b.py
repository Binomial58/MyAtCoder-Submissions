N,K,Q=map(int, input().split())
A=list(map(int, input().split()))
L=list(map(int, input().split()))
for i in L:
    if A[i-1]!=N and A.count(A[i-1]+1)==0:
        A[i-1]+=1
print(*A)