N,K=map(int, input().split())
A=list(map(int, input().split()))
S=1
for i in range(N):
    S*=A[i]
    if len(str(S))>=K+1:
        S=1
print(S)