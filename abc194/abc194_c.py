N=int(input())
A=list(map(int, input().split()))
S=0
for i in range(N):
    S+=(N-1)*A[i]**2
t=sum(A)
for j in range(N-1):
    t=t-A[j]
    S-=2*A[j]*t
print(S)