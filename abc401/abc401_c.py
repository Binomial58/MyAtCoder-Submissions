n,k=map(int, input().split())
A=[1 for i in range(n+1)]
s=k
for i in range(k,n+1):
    A[i]=s%10**9
    s+=A[i]
    s-=A[i-k]
print(A[-1])