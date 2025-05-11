N=int(input())
A=list(map(int, input().split()))
S=0
s=sum(A)
for i in range(N-1):
    s=s-A[i]
    S+=A[i]*(s)
print(S)