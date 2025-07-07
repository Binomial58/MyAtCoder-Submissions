N=int(input())
A=list(map(int, input().split()))
S=0
for i in range(N):
    S+=A[i]*(2**(N-i-1))
print(S)